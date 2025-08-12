from backend.calculadora import IngresoDB, calculator_registration
from dotenv import load_dotenv
import os

load_dotenv()
ruta_db = os.getenv('RUTA_DB')
conexion = IngresoDB(ruta_db)

while True:
    print('''
            Bienvenido a tu calculadora de peso:
            1. Ingresa a la calculadora y registra tu peso.
            2. Mira los registros guardados.
            3. Salir
        ''')
    usuario = str(input('ingresa la opcion que quieras: ')).strip()
    if not usuario:
        print('Los campos deben estar completos.')
        break
    try:
        if usuario == '1':
            calculator = calculator_registration(conexion)
            calculator.calculator_weight()
            calculator.weight_record()
        elif usuario == '2':
            print('Nueva funcion.')
            break
        elif usuario == '3':
            print('Gracias por visitar tu calculadora de peso.')
            break
        else:
            print('Debes ingresar un valor valido entre 1-3.')
        input('\n teclea enter para continuar...')
    except ValueError:
        print('Error de digitacion en el programa ingresa una opcion valida.')
    except Exception as error:
        print(f'Error inesperado en el programa : {error}.')