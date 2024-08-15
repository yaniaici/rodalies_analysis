import os
import subprocess

# Arte ASCII de Rodalies
def mostrar_logo():
    print(r"""
  _____   ____  _____          _      _____ ______  _____            _   _          _  __     ______________ _____  
 |  __ \ / __ \|  __ \   /\   | |    |_   _|  ____|/ ____|     /\   | \ | |   /\   | | \ \   / /___  /  ____|  __ \ 
 | |__) | |  | | |  | | /  \  | |      | | | |__  | (___      /  \  |  \| |  /  \  | |  \ \_/ /   / /| |__  | |__) |
 |  _  /| |  | | |  | |/ /\ \ | |      | | |  __|  \___ \    / /\ \ | . ` | / /\ \ | |   \   /   / / |  __| |  _  / 
 | | \ \| |__| | |__| / ____ \| |____ _| |_| |____ ____) |  / ____ \| |\  |/ ____ \| |____| |   / /__| |____| | \ \ 
 |_|  \_\\____/|_____/_/    \_\______|_____|______|_____/  /_/    \_\_| \_/_/    \_\______|_|  /_____|______|_|  \_\
                                                                                                                    
                                                                                                                    
                                       
                                       
""")

# Funciones para ejecutar los scripts
def ejecutar_script(script_name):
    script_path = os.path.join('src', script_name)
    subprocess.run(['python', script_path])

def cargar_datos():
    ejecutar_script('load_data.py')
    ejecutar_script('clean_data.py')

def visualizar_eda():
    ejecutar_script('eda.py')

def optimizar_frecuencia():
    ejecutar_script('optimizar_frecuencia_por_estacion.py')

def visualizar_mapa():
    notebook_path = os.path.join('notebooks', 'Notebook.ipynb')
    subprocess.run(['jupyter', 'notebook', notebook_path])

# Menú principal
def menu():
    mostrar_logo()
    print("Bienvenido al sistema de análisis de Rodalies de Catalunya")
    print("Selecciona una opción:")
    print("1. Cargar y limpiar datos")
    print("2. Visualizar Análisis Exploratorio de Datos (EDA)")
    print("3. Optimizar la frecuencia de trenes")
    print("4. Visualizar el mapa interactivo")
    print("5. Salir")

    opcion = input("Ingresa el número de la opción que deseas: ")

    if opcion == '1':
        print("Cargando y limpiando datos...")
        cargar_datos()
    elif opcion == '2':
        print("Visualizando Análisis Exploratorio de Datos...")
        visualizar_eda()
    elif opcion == '3':
        print("Optimizando la frecuencia de trenes...")
        optimizar_frecuencia()
    elif opcion == '4':
        print("Abriendo el mapa interactivo en Jupyter Notebook...")
        visualizar_mapa()
    elif opcion == '5':
        print("Saliendo del programa. ¡Hasta luego!")
        exit()
    else:
        print("Opción no válida. Por favor, intenta nuevamente.")
        menu()

# Iniciar el menú principal
if __name__ == "__main__":
    menu()
