import os
import pandas as pd
import folium
from folium.plugins import HeatMap
import ipywidgets as widgets
from IPython.display import display, clear_output

# Función para cargar y combinar los datos
def cargar_datos():
    base_dir = os.getcwd()  # Obtener el directorio actual
    coords_path = os.path.join(base_dir, 'data/estaciones_coordenadas.csv')
    coords_df = pd.read_csv(coords_path)

    freq_path = os.path.join(base_dir, 'data/frecuencia_optima_por_estacion.csv')
    freq_df = pd.read_csv(freq_path)

    data = pd.merge(freq_df, coords_df, on='NOMBRE_ESTACION')
    data = data.dropna(subset=['LATITUD', 'LONGITUD'])  # Filtrar filas con coordenadas NaN

    return data

# Función para crear un mapa de calor para una hora específica
def crear_mapa_hora(data, hora):
    hora_str = f"{hora:02}:00"
    data_hora = data[data['HORA_INICIO_LEGIBLE'] == hora_str]

    mapa = folium.Map(location=[41.3851, 2.1734], zoom_start=8)
    heat_data = [[row['LATITUD'], row['LONGITUD'], row['FRECUENCIA_OPTIMA']] for index, row in data_hora.iterrows()]
    HeatMap(heat_data).add_to(mapa)

    return mapa

# Función para mostrar el mapa interactivo con el deslizador de hora
def mostrar_mapa_interactivo(data):
    hora_slider = widgets.IntSlider(value=0, min=0, max=23, step=1, description='Hora:', continuous_update=False)
    output = widgets.Output()  # Crear un widget de salida

    def actualizar_mapa(change):
        with output:
            clear_output(wait=True)  # Limpiar la salida antes de mostrar el nuevo mapa
            mapa = crear_mapa_hora(data, change['new'])
            display(mapa)

    hora_slider.observe(actualizar_mapa, names='value')

    display(hora_slider)
    display(output)
    
    # Mostrar el mapa inicial
    with output:
        mapa_inicial = crear_mapa_hora(data, hora_slider.value)
        display(mapa_inicial)

# Cargar los datos combinados y filtrados
data = cargar_datos()

# Mostrar el mapa interactivo
mostrar_mapa_interactivo(data)
