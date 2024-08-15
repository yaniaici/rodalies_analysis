# Proyecto de Optimización de Frecuencia de Trenes y Visualización en Mapa Interactivo

Este proyecto tiene como objetivo optimizar la frecuencia de trenes en la red de Rodalies de Catalunya y visualizar la distribución de la demanda en un mapa interactivo. Utilizando datos de pasajeros, el proyecto genera un análisis de la demanda y propone ajustes en la frecuencia de los trenes, mostrando los resultados en un mapa de calor interactivo.

## Estructura del Proyecto

```
train-optimization/
│
├── data/
│   ├── estaciones_coordenadas.csv          # Coordenadas geográficas de las estaciones
│   ├── frecuencia_optima_por_estacion.csv  # Frecuencia óptima de trenes por estación y hora
│   ├── viajeros.csv                        # Datos originales de pasajeros
│   ├── viajeros_limpios.csv                # Datos limpios y procesados de pasajeros
│
├── notebooks/
│   ├── Mapa_Interactivo_Trenes.ipynb       # Jupyter Notebook que genera el mapa interactivo
│
├── src/
│   ├── __init__.py                         # Archivo de inicialización del paquete
│   ├── load_data.py                        # Script para cargar los datos de pasajeros
│   ├── clean_data.py                       # Script para limpiar y procesar los datos
│   ├── eda.py                              # Script para el análisis exploratorio de datos (EDA)
│   ├── optimizar_frecuencia.py             # Script para calcular la frecuencia óptima global
│   ├── optimizar_frecuencia_por_estacion.py # Script para calcular la frecuencia óptima por estación
│   ├── load_data_stations.py               # Script para obtener coordenadas de las estaciones
│   ├── vis_mapa_int.py                     # Script para generar el mapa interactivo (alternativa al Notebook)
│
├── requirements.txt                        # Dependencias del proyecto
└── README.md                               # Documentación del proyecto
```

## Dependencias

Asegúrate de tener un entorno virtual configurado y activo. Luego, instala las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

## Descripción de los Scripts

### 1. `load_data.py`

Carga los datos de pasajeros desde un archivo CSV (`viajeros.csv`) y muestra una vista preliminar de las primeras filas del DataFrame.

**Uso:**

```bash
python src/load_data.py
```

### 2. `clean_data.py`

Limpia los datos cargados, maneja valores nulos, y transforma las columnas del horario en un formato más manejable. Los datos limpios se guardan en `viajeros_limpios.csv`.

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

Calcula la frecuencia óptima de trenes para cada estación individualmente en cada franja horaria. Los resultados se visualizan en un gráfico de calor (heatmap), mostrando las estaciones y horas con mayor demanda.

**Uso:**

```bash
python src/optimizar_frecuencia_por_estacion.py
```

**Salida:**

- `frecuencia_optima_por_estacion.csv`: Archivo CSV con la frecuencia óptima por franja horaria y estación.

### 6. `load_data_stations.py`

Obtiene las coordenadas geográficas (latitud y longitud) de cada estación de tren utilizando una API de geocodificación. Los resultados se guardan en `estaciones_coordenadas.csv`.

**Uso:**

```bash
python src/load_data_stations.py
```

**Salida:**

- `estaciones_coordenadas.csv`: Archivo CSV con las coordenadas de las estaciones.

### 7. `vis_mapa_int.py`

Genera un mapa interactivo de Catalunya que muestra la frecuencia óptima de trenes en cada estación y franja horaria. Permite seleccionar diferentes horas del día para ver cómo varía la demanda.

**Uso:**

```bash
python src/vis_mapa_int.py
```

### 8. `Mapa_Interactivo_Trenes.ipynb`

Este Jupyter Notebook integra todas las funcionalidades para cargar los datos, obtener las coordenadas de las estaciones, y generar un mapa interactivo. El mapa muestra la frecuencia de trenes a lo largo del día y permite seleccionar la hora mediante un deslizador.

**Ejecución:**

- Abre el Notebook en Jupyter Notebook o JupyterLab y ejecuta las celdas en orden.

## Visualizaciones

### 1. **Gráfico de Barras:**
   - Muestra el total de viajeros subidos por estación. Identifica las estaciones con mayor demanda.

### 2. **Gráfico de Línea:**
   - Muestra el número de viajeros subidos y bajados por franja horaria. Ayuda a identificar las horas pico en el sistema.

### 3. **Mapa Interactivo:**
   - Muestra la frecuencia óptima de trenes por estación y franja horaria en un mapa de Catalunya, con la posibilidad de seleccionar diferentes horas del día.

---

**Autor:** Yani Aici 

---