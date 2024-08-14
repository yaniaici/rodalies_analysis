import pandas as pd

def clean_data(df):
    """
    Limpia los datos eliminando nulos y transformando columnas.

    Args:
    df (pd.DataFrame): DataFrame con los datos cargados.

    Returns:
    pd.DataFrame: DataFrame limpio.
    """
    # Eliminar filas con valores nulos (opcional, dependiendo del contexto)
    df = df.dropna()
    
    # Separar la columna 'TRAMO_HORARIO' en dos columnas 'HORA_INICIO' y 'HORA_FIN'
    df[['HORA_INICIO', 'HORA_FIN']] = df['TRAMO_HORARIO'].str.split(' - ', expand=True)
    
    # Convertir las nuevas columnas de tiempo a un formato manejable
    df['HORA_INICIO'] = pd.to_datetime(df['HORA_INICIO'], format='%H:%M').dt.time
    df['HORA_FIN'] = pd.to_datetime(df['HORA_FIN'], format='%H:%M').dt.time
    
    print("Datos limpios:")
    print(df.head())
    
    return df

if __name__ == "__main__":
    # Cargar los datos con el delimitador correcto
    filepath = '../data/viajeros.csv'
    print(f"Cargando datos desde {filepath}...")
    df = pd.read_csv(filepath, delimiter=';')
    
    # Limpiar los datos
    df_clean = clean_data(df)
    
    # Guardar los datos limpios en un nuevo archivo CSV (opcional)
    df_clean.to_csv('../data/viajeros_limpios.csv', index=False)
