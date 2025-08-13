import sqlite3 # Importacion del modulo sqlite3 para manejo de la base de datos.
import pandas as pd # Importacion del modulo pandas para mostar los datos.

# Clase para realizar la conexion con la base de datos.
class Ingreso_DB:
    def __init__(self,ruta_db):
        try:
            self.conn = sqlite3.connect(ruta_db) # Conexion con la base de datos.
            self.cursor = self.conn.cursor() # Cursor el cual nos ayuda a manejar la base de datos.
        except sqlite3.DatabaseError as error:
            print(f'Error inesperado en la base de datos : {error}.')
    
    def cierre_db(self):
        try:
            self.conn.close() # Cierre de la base de datos.
        except sqlite3.OperationalError as error:
            print(f'Error operacional en la base de datos : {error}.')

# Clase para revisar los registros de la base de datos
class RegistrosDB:
    def __init__(self,conexion):
        try:
            self.conexion = conexion # Conexion con la base de datos.
            if not self.conexion:
                print('No se encontro la conexion con la base de datos.')
                return
        except sqlite3.OperationalError as error:
            print(f'Error operacional en la base de datos : {error}')
    
    def show_records(self):
        try:
            # Query para la revision de los datos de la tabla.
            query = '''
                SELECT
                    nombre,
                    año,
                    mes,
                    peso
                FROM peso_mes
                '''
            resultado_pd = pd.read_sql_query(query, self.conexion.conn) # Lectura de la consulta.
            # Se revisa si el dataframe esta vacio o no.
            if not resultado_pd.empty:
                # Impresion de los resultados.
                print(resultado_pd)
            else:
                print('No se encontraron registros en la base de datos.')
        except sqlite3.OperationalError as error:
            print(f'Error operacional en la base de datos : {error}.')
        except Exception as error:
            print(f'Error inespeado en el programa : {error}.')