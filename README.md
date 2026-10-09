# Clasificador de tumores con Perceptrón — versión 1.0.0

Proyecto base de la **Evaluación Parcial** de Construcción de Software. Un Perceptrón implementado desde cero
con NumPy clasifica tumores de mama como **malignos (0)** o **benignos (1)** a partir de medidas de las células.

## Datos

- `datos/pacientes.csv`: 569 pacientes, 10 medidas y la columna `diagnostico`.
  Proviene del dataset *Breast Cancer Wisconsin (Diagnostic)* (UCI). Se borraron algunos valores para practicar la limpieza.
- `datos/hospital_b.csv`: 60 pacientes de otro hospital. Se usa para reproducir el error del Issue de la Tarea 1.

## Estructura

```text
├── datos/                 # archivos CSV
├── src/
│   ├── datos.py           # cargar, limpiar, estandarizar y dividir
│   ├── perceptron.py      # clase Perceptron
│   ├── excepciones.py     # DatosInvalidosError y ModeloNoEntrenadoError
│   └── metricas.py        # accuracy y otras métricas
├── main.py                # entrena y evalúa los modelos
├── .github/workflows/ci.yml
├── CHANGELOG.md
└── requirements.txt
```

## Cómo ejecutarlo

```bash
pip install -r requirements.txt
python main.py --datos datos/pacientes.csv --objetivo diagnostico
```

## Integrantes

| Nombre | Código | Rol |
|---|---|---|
| Eduardo Puma Ccorimanya | 75575890 | Líder. Configuración del repositorio, Tarea 1 (hotfix 0.9.1), Tarea 6 (refactor) y Tarea 7 (release 1.0.0) |
| Rebeca Yasbet Rocca Ramos | 73576076 | Tarea 2: excepciones propias y validaciones |
| Junior Jeferson Sottec Velasque | 77157107 | Tarea 3: métricas (error y matriz de confusión) |
| Ruth Estefani Huaman Mamani | 73231557 | Tarea 4: decaimiento de la tasa (Modelo 2) |
| Ramiro Castillo Mamani | 71936868 | Tarea 5: Modelo 3 con `--features` |

## Resultados

| Modelo | Configuración | Accuracy | Error | Matriz [[TN, FP], [FN, TP]] |
|---|---|---|---|---|
| 1 | tasa 0.01, features base | 0.867 | 0.133 | [[34, 4], [11, 64]] |
| 2 | tasa 0.5, decaimiento 0.1, features base | 0.876 | 0.124 | [[37, 1], [13, 62]] |
| 3 | tasa 0.01, concavidad, puntos_concavos, area, textura | 0.92 | 0.08 | [[35, 3], [6, 69]] |

Features base: `radio`, `textura`, `perimetro`, `area`. Clase 0 = maligno, 1 = benigno.

### Análisis

**¿Por qué los Modelos 1 y 2 daban igual antes de la Tarea 4, si sus tasas eran distintas?**
Los pesos empiezan en 0 y cada actualización es `tasa · error · x`. Con una tasa fija, `w` y `b` terminan multiplicados por el mismo factor, y eso no cambia el signo de `X·w + b`, que es lo único que usa el Perceptrón para predecir. Por eso los dos modelos daban la misma accuracy (0.867) y los mismos errores por época. Con el decaimiento la tasa cambia en cada época, se rompe esa proporción y el Modelo 2 pasa a 0.876.

**¿Qué cambió con las features del Modelo 3 y por qué?**
Las features base son redundantes: `radio`, `perimetro` y `area` miden el tamaño de la célula. El Modelo 3 reemplaza `radio` y `perimetro` por `concavidad` y `puntos_concavos`, que miden la forma irregular del contorno y aportan información nueva. Las clases quedan más separables: la accuracy sube a 0.92 y los falsos negativos bajan de 11 a 6.

**Los errores por época nunca llegan a 0: ¿qué dice eso sobre los datos?**
Que no son linealmente separables: no existe un hiperplano que deje todos los malignos de un lado y todos los benignos del otro. El Perceptrón solo converge a 0 errores cuando los datos son separables; si no, sigue corrigiendo sin terminar (Modelo 1 entre 63 y 74 errores por época, Modelo 3 entre 36 y 44).

**¿Qué error es más grave, un falso positivo o un falso negativo?**
La clase positiva (1) es benigno, así que un falso positivo es un tumor maligno clasificado como benigno: el paciente no recibe tratamiento. Es el error más grave. Un falso negativo (benigno clasificado como maligno) solo lleva a exámenes adicionales. Por eso, aunque el Modelo 3 tiene la mejor accuracy, el Modelo 2 es el que menos falsos positivos comete (1 frente a 4 y 3).
