# src/eda.py
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
    print("Columnas en el DataFrame después de cargar:")
    print(df.columns)
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

def plot_viajeros_por_estacion(df):
    """
    Realiza un gráfico de barras que muestra el número de viajeros subidos por estación.
    
    Args:
    df (pd.DataFrame): DataFrame con los datos limpios.
    """
    plt.figure(figsize=(12, 6))
    sns.barplot(x='NOMBRE_ESTACION', y='VIAJEROS_SUBIDOS', data=df, estimator=sum, errorbar=None)
    plt.xticks(rotation=90)
    plt.title('Total de Viajeros Subidos por Estación')
    plt.xlabel('Estación')
    plt.ylabel('Total de Viajeros Subidos')
    plt.tight_layout()
    plt.show()

def plot_viajeros_por_horario(df):
    """
    Realiza un gráfico de línea que muestra el número de viajeros subidos y bajados por franja horaria.
    
    Args:
    df (pd.DataFrame): DataFrame con los datos limpios.
    """
    # Convertir la hora al formato datetime
    df['HORA_INICIO'] = pd.to_datetime(df['HORA_INICIO'], format='%H:%M:%S').dt.time
    
    # Convertir la hora en segundos desde la medianoche
    df['HORA_INICIO_SEGUNDOS'] = df['HORA_INICIO'].apply(convert_time_to_seconds)
    
    df_horario = df.groupby('HORA_INICIO_SEGUNDOS').agg({'VIAJEROS_SUBIDOS': 'sum', 'VIAJEROS_BAJADOS': 'sum'}).reset_index()

    plt.figure(figsize=(12, 6))
    sns.lineplot(x='HORA_INICIO_SEGUNDOS', y='VIAJEROS_SUBIDOS', data=df_horario, marker='o', label='Viajeros Subidos')
    sns.lineplot(x='HORA_INICIO_SEGUNDOS', y='VIAJEROS_BAJADOS', data=df_horario, marker='o', label='Viajeros Bajados')
    plt.title('Viajeros Subidos y Bajados por Franja Horaria')
    plt.xlabel('Hora de Inicio (segundos desde medianoche)')
    plt.ylabel('Número de Viajeros')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Cargar datos limpios
    filepath = '../data/viajeros_limpios.csv'
    df = load_clean_data(filepath)
    
    # Gráfico de viajeros subidos por estación
    plot_viajeros_por_estacion(df)
    
    # Gráfico de viajeros subidos y bajados por franja horaria
    plot_viajeros_por_horario(df)
