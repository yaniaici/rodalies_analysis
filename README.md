# Proyecto de Optimización de la Frecuencia de Trenes

Este proyecto tiene como objetivo optimizar la frecuencia de trenes en función del volumen de viajeros en diferentes estaciones de cercanías en Barcelona. Utilizamos técnicas de análisis de datos y visualización para identificar patrones de demanda y proponer ajustes en la frecuencia de los trenes.

## Estructura del Proyecto

```
train-optimization/
│
├── data/
│   ├── viajeros.csv                      # Archivo CSV con los datos originales de viajeros
│   ├── viajeros_limpios.csv              # Archivo CSV con los datos limpios y transformados
│   ├── frecuencia_optima.csv             # Archivo CSV con la frecuencia óptima por franja horaria (global)
│   ├── frecuencia_optima_por_estacion.csv# Archivo CSV con la frecuencia óptima por franja horaria y estación
│
├── venv/                                 # Entorno virtual de Python
│
├── src/                                  # Carpeta con los scripts Python
│   ├── __init__.py                       # Archivo para indicar que 'src' es un paquete de Python
│   ├── load_data.py                      # Script para cargar y explorar los datos
│   ├── clean_data.py                     # Script para limpiar los datos
│   ├── eda.py                            # Script para el análisis exploratorio de datos (EDA)
│   ├── optimizar_frecuencia.py           # Script para optimizar la frecuencia global de trenes
│   ├── optimizar_frecuencia_por_estacion.py # Script para optimizar la frecuencia por estación
│
├── requirements.txt                      # Archivo con las dependencias del proyecto
└── README.md                             # Documentación del proyecto
```

## Dependencias

Asegúrate de tener un entorno virtual configurado y activo. Luego, instala las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

## Descripción de los Scripts

### 1. `load_data.py`

Este script carga los datos desde un archivo CSV y muestra una vista preliminar de las primeras filas del DataFrame.

**Uso:**

```bash
python src/load_data.py
```

### 2. `clean_data.py`

Limpia los datos cargados, maneja valores nulos y transforma las columnas del horario en un formato más manejable. Los datos limpios se guardan en `viajeros_limpios.csv`.

**Uso:**

```bash
python src/clean_data.py
```

### 3. `eda.py`

Realiza un análisis exploratorio de datos (EDA) y genera visualizaciones para identificar patrones en el comportamiento de los viajeros. Esto incluye gráficos del número de viajeros por estación y por franja horaria.

**Uso:**

```bash
python src/eda.py
```

### 4. `optimizar_frecuencia.py`

Calcula la frecuencia óptima de trenes en función del volumen total de pasajeros subidos en cada franja horaria. La frecuencia óptima se ajusta según la capacidad de los trenes (por defecto, 100 pasajeros por tren).

**Uso:**

```bash
python src/optimizar_frecuencia.py
```

**Salida:**

- `frecuencia_optima.csv`: Archivo CSV con la frecuencia óptima por franja horaria.

### 5. `optimizar_frecuencia_por_estacion.py`

Este script va un paso más allá al calcular la frecuencia óptima de trenes para cada estación individualmente en cada franja horaria. Los resultados se visualizan en un gráfico de calor (heatmap), mostrando las estaciones y horas con mayor demanda.

**Uso:**

```bash
python src/optimizar_frecuencia_por_estacion.py
```

**Salida:**

- `frecuencia_optima_por_estacion.csv`: Archivo CSV con la frecuencia óptima por franja horaria y estación.

## Visualizaciones

### 1. **Gráfico de Barras:**
   - Muestra el total de viajeros subidos por estación. Identifica las estaciones más críticas en términos de volumen de pasajeros.

### 2. **Gráfico de Línea:**
   - Muestra el número de viajeros subidos y bajados por franja horaria. Ayuda a identificar las horas pico en el sistema.

### 3. **Heatmap (Frecuencia por Estación):**
   - Muestra la frecuencia óptima de trenes para cada estación y franja horaria, permitiendo una planificación más detallada y eficiente.

---

**Autor:** Yani Aici 

---