import os
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

def obtener_coordenadas(nombre_estacion):
    try:
        location = geocode(nombre_estacion + ", Catalunya, Spain")
        if location:
            return pd.Series([location.latitude, location.longitude])
        else:
            return pd.Series([None, None])
    except Exception as e:
        print(f"Error con la estación {nombre_estacion}: {e}")
        return pd.Series([None, None])

if __name__ == "__main__":
    # Usamos el archivo existente 'viajeros_limpios.csv' que contiene 'NOMBRE_ESTACION'
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, '../data/viajeros_limpios.csv')

    # Cargar el archivo CSV y extraer las estaciones únicas
    viajeros_df = pd.read_csv(csv_path)
    estaciones_df = viajeros_df[['NOMBRE_ESTACION']].drop_duplicates().reset_index(drop=True)

    # Configurar el geocodificador
    geolocator = Nominatim(user_agent="train-optimization")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)  # Puedes incrementar el delay si es necesario

    # Lista para guardar resultados progresivamente
    resultados = []

    # Aplicar la función a cada estación
    for index, row in estaciones_df.iterrows():
        nombre_estacion = row['NOMBRE_ESTACION']
        print(f"Procesando estación {index + 1}/{len(estaciones_df)}: {nombre_estacion}")
        lat_long = obtener_coordenadas(nombre_estacion)
        resultados.append([nombre_estacion] + lat_long.tolist())

        # Guardar resultados intermedios cada 10 estaciones
        if (index + 1) % 10 == 0:
            temp_df = pd.DataFrame(resultados, columns=['NOMBRE_ESTACION', 'LATITUD', 'LONGITUD'])
            temp_df.to_csv(os.path.join(base_dir, '../data/estaciones_coordenadas_temp.csv'), index=False)
    
    # Guardar el resultado final
    final_df = pd.DataFrame(resultados, columns=['NOMBRE_ESTACION', 'LATITUD', 'LONGITUD'])
    final_df.to_csv(os.path.join(base_dir, '../data/estaciones_coordenadas.csv'), index=False)
