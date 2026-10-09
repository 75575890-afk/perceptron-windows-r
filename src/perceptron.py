"""Perceptrón simple implementado desde cero con NumPy."""
import numpy as np
from src.excepciones import ModeloNoEntrenadoError


class Perceptron:
    """Clasificador binario: predice 1 si X·w + b >= 0, si no 0."""

<<<<<<< HEAD
    def __init__(self, tasa_aprendizaje=0.01, epocas=50):
        if tasa_aprendizaje <= 0:
            raise ValueError('La tasa de aprendizaje debe ser positiva')
        if epocas <= 0:
            raise ValueError('Las épocas deben ser positivas')
=======
    def __init__(self, tasa_aprendizaje=0.01, epocas=50, decaimiento=0.0):
>>>>>>> 4113b5eb7dba1a7c62b55e903b2ce6cf81296a11
        self.tasa = tasa_aprendizaje
        self.epocas = epocas
        self.decaimiento = decaimiento
        self.w = None
        self.b = 0.0
        self.errores_por_epoca = []

    def entrenar(self, X, y):
        """Ajusta los pesos con la regla del Perceptrón. Devuelve self."""
        self.w = np.zeros(X.shape[1])
        self.b = 0.0
        self.errores_por_epoca = []
        for epoca in range(self.epocas):
            tasa = self.tasa / (1 + self.decaimiento * epoca)
            errores = 0
            for xi, yi in zip(X, y):
                y_pred = 1 if xi @ self.w + self.b >= 0 else 0
                error = yi - y_pred
                self.w = self.w + tasa * error * xi
                self.b = self.b + tasa * error
                errores += int(error != 0)
            self.errores_por_epoca.append(errores)
        return self

    def predecir(self, X):
        """Devuelve un array de 0 y 1, uno por fila de X."""
<<<<<<< HEAD
        if self.w is None:
            raise ModeloNoEntrenadoError('El modelo no está entrenado')
=======
>>>>>>> 4113b5eb7dba1a7c62b55e903b2ce6cf81296a11
        return np.where(X @ self.w + self.b >= 0, 1, 0)