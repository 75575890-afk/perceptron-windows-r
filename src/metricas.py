import numpy as np

def accuracy(y, y_pred):
    # Esta función ya estaba, solo asegúrate de que esté bien
    return np.mean(y == y_pred)

def error_clasificacion(y, y_pred):
    # Tarea 3.1: El error es 1 menos la exactitud
    return 1 - accuracy(y, y_pred)

def matriz_confusion(y, y_pred):
    # Tarea 3.1: Devuelve [[TN, FP], [FN, TP]]
    # TN: Verdadero Negativo (era 0, dijo 0)
    # FP: Falso Positivo (era 0, dijo 1)
    # FN: Falso Negativo (era 1, dijo 0)
    # TP: Verdadero Positivo (era 1, dijo 1)
    
    tn = np.sum((y == 0) & (y_pred == 0))
    fp = np.sum((y == 0) & (y_pred == 1))
    fn = np.sum((y == 1) & (y_pred == 0))
    tp = np.sum((y == 1) & (y_pred == 1))
    
    return [[tn, fp], [fn, tp]]