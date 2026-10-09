# Changelog
## [1.0.0]

### Agregado
- Excepciones propias `DatosInvalidosError` y `ModeloNoEntrenadoError` en `src/excepciones.py`. `cargar_datos` valida que el archivo exista, que esté la columna objetivo y que sea binaria.
- `Perceptron` lanza `ValueError` si la tasa o las épocas no son positivas, y `predecir` lanza `ModeloNoEntrenadoError` si el modelo no está entrenado.
- Métricas `error_clasificacion` y `matriz_confusion`, impresas para cada modelo.
- Parámetro `decaimiento` en `Perceptron`: la tasa se reduce al inicio de cada época.
- Modelo 3 y argumento `--features` para elegir las columnas; avisa si alguna no existe.

### Cambiado
- `main.py` muestra `Error: <mensaje>` sin traceback y termina con código 1.
- El Modelo 2 usa tasa 0.5 con decaimiento 0.1.
- `main.py` refactorizado: función `evaluar_modelo`, constante `EPOCAS` y sin código duplicado.
- README con la sección Resultados.

## [0.9.1]

### Corregido
- `estandarizar` ya no divide entre cero cuando una columna tiene desviación 0 (por ejemplo, `textura` en `hospital_b.csv`). Ahora usa 1 como desviación en esos casos. (#1)

## [0.9.0]

### Agregado
- Carga, limpieza, estandarización y división de los datos.
- Perceptrón simple con entrenamiento por épocas.
- Modelos 1 y 2 en `main.py`, evaluados con accuracy.
