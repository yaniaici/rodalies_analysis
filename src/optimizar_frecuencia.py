# src/optimizar_frecuencia.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_clean_data(filepath):
    """
    Carga y retorna los datos limpios desde un archivo CSV.
    
    Args:
    filepath (str): Ruta al archivo CSV.
    
    Returns:
    pd.DataFrame: DataFrame con los datos limpios.
    """
    df = pd.read_csv(filepath, delimiter=',')
    return df

def convert_time_to_seconds(time_obj):
    """
    Convierte un objeto time a segundos desde la medianoche.
    
    Args:
    time_obj (datetime.time): Objeto de tiempo.
    
    Returns:
    int: Tiempo en segundos desde la medianoche.
    """
    return time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second

def convert_seconds_to_time(seconds):
    """
    Convierte segundos desde la medianoche a un objeto de hora legible.
    
    Args:
    seconds (int): Segundos desde la medianoche.
    
    Returns:
    str: Hora en formato HH:MM.
    """
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f'{hours:02}:{minutes:02}'

def calcular_frecuencia_optima(df_horario, capacidad_tren=100):
    """
    Calcula la frecuencia óptima de trenes basada en la demanda.
    
    Args:
    df_horario (pd.DataFrame): DataFrame con la demanda por franja horaria.
    capacidad_tren (int): Número máximo de pasajeros por tren.
    
    Returns:
    pd.DataFrame: DataFrame con la columna FRECUENCIA_OPTIMA añadida.
    """
    df_horario['FRECUENCIA_OPTIMA'] = df_horario['VIAJEROS_SUBIDOS'].apply(
        lambda x: max(1, round(x / capacidad_tren))
    )
    return df_horario

def plot_frecuencia_optima(df_horario):
    """
    Grafica la frecuencia óptima de trenes por franja horaria.
    
    Args:
    df_horario (pd.DataFrame): DataFrame con la frecuencia óptima calculada.
    """
    # Convertir segundos desde la medianoche a formato HH:MM
    df_horario['HORA_INICIO_LEGIBLE'] = df_horario['HORA_INICIO_SEGUNDOS'].apply(convert_seconds_to_time)
    
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='HORA_INICIO_LEGIBLE', y='FRECUENCIA_OPTIMA', data=df_horario, marker='o')
    plt.title('Frecuencia Óptima de Trenes por Franja Horaria')
    plt.xlabel('Hora de Inicio')
    plt.ylabel('Frecuencia Óptima de Trenes (trenes por franja horaria)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Cargar datos limpios
    filepath = '../data/viajeros_limpios.csv'
    df = load_clean_data(filepath)
    
    # Convertir la hora al formato datetime
    df['HORA_INICIO'] = pd.to_datetime(df['HORA_INICIO'], format='%H:%M:%S').dt.time
    
    # Convertir la hora en segundos desde la medianoche
    df['HORA_INICIO_SEGUNDOS'] = df['HORA_INICIO'].apply(convert_time_to_seconds)
    
    # Agregar por franja horaria
    df_horario = df.groupby('HORA_INICIO_SEGUNDOS').agg({'VIAJEROS_SUBIDOS': 'sum', 'VIAJEROS_BAJADOS': 'sum'}).reset_index()
    
    # Calcular la frecuencia óptima de trenes
    df_horario = calcular_frecuencia_optima(df_horario)
    
    # Graficar la frecuencia óptima de trenes con horas legibles
    plot_frecuencia_optima(df_horario)
    
    # Guardar los resultados
    df_horario.to_csv('../data/frecuencia_optima.csv', index=False)
