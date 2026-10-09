"""Entrena y evalúa los modelos de Perceptrón.

Uso:
    python main.py --datos datos/pacientes.csv --objetivo diagnostico
"""
import argparse
import sys

from src.datos import cargar_datos, limpiar, estandarizar, dividir
from src.excepciones import DatosInvalidosError
from src.perceptron import Perceptron
from src.metricas import accuracy, error_clasificacion, matriz_confusion

FEATURES_BASE = ["radio", "textura", "perimetro", "area"]
FEATURES_MODELO_3 = ["concavidad", "puntos_concavos", "area", "textura"]
EPOCAS = 30


def evaluar_modelo(nombre, df, features, objetivo, modelo):
    """Prepara los datos, entrena el modelo e imprime sus métricas."""
    datos = limpiar(df, features)
    X = estandarizar(datos[features].to_numpy(dtype=float))
    y = datos[objetivo].to_numpy()
    X_tr, X_te, y_tr, y_te = dividir(X, y)
    modelo.entrenar(X_tr, y_tr)
    y_pred = modelo.predecir(X_te)
    print(nombre)
    print("  accuracy:", round(accuracy(y_te, y_pred), 3))
    print("  error:", round(error_clasificacion(y_te, y_pred), 3))
    print("  matriz:", matriz_confusion(y_te, y_pred).tolist())
    print("  errores por época:", modelo.errores_por_epoca[:10], "...")


def main():
    parser = argparse.ArgumentParser(description="Clasificador con Perceptrón")
    parser.add_argument("--datos", default="datos/pacientes.csv")
    parser.add_argument("--objetivo", default="diagnostico")
    parser.add_argument("--features", nargs="+", default=FEATURES_MODELO_3)
    args = parser.parse_args()

    df = cargar_datos(args.datos, args.objetivo)
    faltantes = [f for f in args.features if f not in df.columns]
    if faltantes:
        raise DatosInvalidosError(f"Columnas inexistentes: {', '.join(faltantes)}")

    evaluar_modelo(
        "Modelo 1 (tasa 0.01)", df, FEATURES_BASE, args.objetivo,
        Perceptron(tasa_aprendizaje=0.01, epocas=EPOCAS),
    )
    evaluar_modelo(
        "Modelo 2 (tasa 0.5, decaimiento 0.1)", df, FEATURES_BASE, args.objetivo,
        Perceptron(tasa_aprendizaje=0.5, epocas=EPOCAS, decaimiento=0.1),
    )
    nombre3 = "Modelo 3 (tasa 0.01, features: " + ", ".join(args.features) + ")"
    evaluar_modelo(
        nombre3, df, args.features, args.objetivo,
        Perceptron(tasa_aprendizaje=0.01, epocas=EPOCAS),
    )


if __name__ == "__main__":
    try:
        main()
    except (DatosInvalidosError, ValueError) as e:
        print("Error:", e)
        sys.exit(1)
