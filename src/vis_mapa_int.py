import os
import pandas as pd
import folium
from folium.plugins import HeatMap
import ipywidgets as widgets
from IPython.display import display

def cargar_datos():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    coords_path = os.path.join(base_dir, '../data/estaciones_coordenadas.csv')
    coords_df = pd.read_csv(coords_path)

    freq_path = os.path.join(base_dir, '../data/frecuencia_optima_por_estacion.csv')
    freq_df = pd.read_csv(freq_path)

    data = pd.merge(freq_df, coords_df, on='NOMBRE_ESTACION')
    data = data.dropna(subset=['LATITUD', 'LONGITUD'])

    return data

def crear_mapa_hora(data, hora):
    hora_str = f"{hora:02}:00"
    data_hora = data[data['HORA_INICIO_LEGIBLE'] == hora_str]

    mapa = folium.Map(location=[41.3851, 2.1734], zoom_start=8)

    heat_data = [[row['LATITUD'], row['LONGITUD'], row['FRECUENCIA_OPTIMA']] for index, row in data_hora.iterrows()]
    HeatMap(heat_data).add_to(mapa)

    return mapa

def mostrar_mapa_interactivo(data):
    hora_slider = widgets.IntSlider(value=0, min=0, max=23, step=1, description='Hora:', continuous_update=False)

    def actualizar_mapa(change):
        mapa = crear_mapa_hora(data, change['new'])
        mapa.save(f"mapa_hora_{change['new']:02}.html")
        display(mapa)

    hora_slider.observe(actualizar_mapa, names='value')

    display(hora_slider)
    mapa_inicial = crear_mapa_hora(data, hora_slider.value)
    mapa_inicial.save("mapa_hora_inicial.html")
    display(mapa_inicial)

if __name__ == "__main__":
    data = cargar_datos()
    mostrar_mapa_interactivo(data)
