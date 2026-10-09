# Changelog

## [0.9.1]

### Corregido
- `estandarizar` ya no divide entre cero cuando una columna tiene desviación 0 (por ejemplo, `textura` en `hospital_b.csv`). Ahora usa 1 como desviación en esos casos. (#1)

## [0.9.0]

### Agregado
- Carga, limpieza, estandarización y división de los datos.
- Perceptrón simple con entrenamiento por épocas.
- Modelos 1 y 2 en `main.py`, evaluados con accuracy.
