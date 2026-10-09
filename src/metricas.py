"""Métricas para evaluar un clasificador binario."""
import numpy as np


def accuracy(y, y_pred):
    """Proporción de predicciones correctas (entre 0 y 1)."""
    return float(np.mean(np.asarray(y) == np.asarray(y_pred)))


def error_clasificacion(y, y_pred):
    """Proporción de predicciones incorrectas (entre 0 y 1)."""
    raise NotImplementedError("Tarea 3: implementar error_clasificacion")


def matriz_confusion(y, y_pred):
    """Devuelve la matriz 2x2 [[TN, FP], [FN, TP]] como array de NumPy."""
    raise NotImplementedError("Tarea 3: implementar matriz_confusion")
