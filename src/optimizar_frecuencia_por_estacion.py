# src/optimizar_frecuencia_por_estacion.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_clean_data(filepath):
    df = pd.read_csv(filepath, delimiter=',')
    return df

def convert_time_to_seconds(time_obj):
    return time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second

def convert_seconds_to_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f'{hours:02}:{minutes:02}'

def calcular_frecuencia_optima_por_estacion(df, capacidad_tren=100):
    df['FRECUENCIA_OPTIMA'] = df['VIAJEROS_SUBIDOS'].apply(
        lambda x: max(1, round(x / capacidad_tren))
    )
    return df

def plot_frecuencia_optima_heatmap(df):
    # Agrupar por hora y estación para asegurarnos de que cada combinación sea única
    df_grouped = df.groupby(['HORA_INICIO_LEGIBLE', 'NOMBRE_ESTACION'])['FRECUENCIA_OPTIMA'].sum().reset_index()
    
    # Rellenar los valores faltantes con ceros y asegurar que los valores sean enteros
    df_pivot = df_grouped.pivot(index="HORA_INICIO_LEGIBLE", columns="NOMBRE_ESTACION", values="FRECUENCIA_OPTIMA").fillna(0)
    df_pivot = df_pivot.astype(int)  # Convertir a enteros
    
    # Verificar las columnas y las filas antes de hacer el heatmap
    print("Datos después del pivoteo:")
    print(df_pivot.head())
    
    plt.figure(figsize=(15, 8))
    sns.heatmap(df_pivot, annot=False, cmap="YlGnBu", cbar_kws={'label': 'Frecuencia Óptima'})
    plt.title('Frecuencia Óptima de Trenes por Estación y Franja Horaria')
    plt.xlabel('Estación')
    plt.ylabel('Hora de Inicio')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    filepath = '../data/viajeros_limpios.csv'
    df = load_clean_data(filepath)
    
    df['HORA_INICIO'] = pd.to_datetime(df['HORA_INICIO'], format='%H:%M:%S').dt.time
    df['HORA_INICIO_SEGUNDOS'] = df['HORA_INICIO'].apply(convert_time_to_seconds)
    
    df_horario_estacion = df.groupby(['HORA_INICIO_SEGUNDOS', 'NOMBRE_ESTACION']).agg(
        {'VIAJEROS_SUBIDOS': 'sum', 'VIAJEROS_BAJADOS': 'sum'}).reset_index()
    
    df_horario_estacion = calcular_frecuencia_optima_por_estacion(df_horario_estacion)
    
    df_horario_estacion['HORA_INICIO_LEGIBLE'] = df_horario_estacion['HORA_INICIO_SEGUNDOS'].apply(convert_seconds_to_time)
    
    plot_frecuencia_optima_heatmap(df_horario_estacion)
    
    df_horario_estacion.to_csv('../data/frecuencia_optima_por_estacion.csv', index=False)
