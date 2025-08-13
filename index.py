# Importacion de modulos donde van las funcionalidades.
from backend.data.calculadora import IngresoDB, calculatorRegistration
from backend.data.registros import RegistrosDB
# Importacion de modulos para carga y lectrua de variables de entorno.
from dotenv import load_dotenv
import os

load_dotenv() # Carga de variables de entorno.
ruta_db = os.getenv('RUTA_DB') # Lectura de la variable de entorno cargada.
conexion = IngresoDB(ruta_db) # Conexion con la ruta de la base de datos.

while True:
    # Menu de opciones de usuario.
    print('''
            Bienvenido a tu calculadora de peso:
            1. Ingresa a la calculadora y registra tu peso.
            2. Mira los registros guardados.
            3. Salir
        ''')
    # Entrada para las opciones de usuario.
    usuario = str(input('ingresa la opcion que quieras: ')).strip()
    # Validador de campo.
    if not usuario:
        print('Los campos deben estar completos.') 
        break
    try:
        # Opciones de usuario para acceder a las funcionalidades.
        if usuario == '1':
            calculator = calculatorRegistration(conexion)
            calculator.calculator_weight()
            calculator.weight_record()
        elif usuario == '2':
            records = RegistrosDB(conexion)
            records.show_records()
        elif usuario == '3':
            print('Gracias por visitar tu calculadora de peso.')
            break
        else:
            print('Debes ingresar un valor valido entre 1-3.')
        input('\n teclea enter para continuar...')
    # Manejo de errores.
    except ValueError:
        print('Error de digitacion en el programa ingresa una opcion valida.')
    except Exception as error:
        print(f'Error inesperado en el programa : {error}.')