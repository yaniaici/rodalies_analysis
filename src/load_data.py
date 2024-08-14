import pandas as pd

def load_data(filepath):
    """
    Carga los datos desde un archivo CSV y muestra las primeras filas.
    
    Args:
    filepath (str): Ruta al archivo CSV.
    
    Returns:
    pd.DataFrame: DataFrame con los datos cargados.
    """
    # Especificar el delimitador correcto
    df = pd.read_csv(filepath, delimiter=';')
    print(f"Datos cargados desde {filepath}. Aquí tienes las primeras filas:")
    print(df.head())
    return df

if __name__ == "__main__":
    # Ruta al archivo CSV
    filepath = '../data/viajeros.csv'
    # Cargar los datos
    df = load_data(filepath)
