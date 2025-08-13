import sqlite3 # Importacion del modulo sqlite3 para manejo de la base de datos.


# Clase para realizar la conexion y el cierre de la base de datos.
class IngresoDB:
    def __init__(self,ruta_db):
        try:
            self.conn = sqlite3.connect(ruta_db) # Conexion con la base de datos.
            self.cursor = self.conn.cursor() # Cursor el cual nos ayuda con el manejo de la base de datos. 
        # Manejo de errores.
        except sqlite3.DatabaseError as error:
            print(f'Error inesperado en la base de datos : {error}.')
            return

    def cierre_db(self):
        try:
            self.conn.close() # Cierre de la base de datos.
        # Manejo de errores.
        except sqlite3.OperationalError as error:
            print(f'Error de operacion en la base de datos : {error}.')

# Clase para el calculo del peso.
class calculatorRegistration:
    def __init__(self,conexion):
        try:
            self.conexion = conexion # Pasa la conexion con la base de datos.
            if not self.conexion:
                print('No se encontro la conexion con la base de datos.')
                return
        # Manejo de errores.
        except sqlite3.OperationalError as error:
            print(f'error de operacion en la base de datos : {error}.')
    
    def calculator_weight(self):
        peso = float(input('Ingresa tu peso: ')) # Ingreso del peso actual.
        altura = float(input('Ingresa tu altura: ')) # Ingreso de la altura actual.
        # Validador de campos.
        if not peso or not altura:
            print('Todos los campos deben estar completos.')
            return
        self.peso_final = round(peso / (altura ** 2), 1) # Se hace el calculo del peso y se redondea a un decimal.
        # Opciones para revisar si el peso esta bajo, normal o sobrepeso.
        if self.peso_final < 18.5:
            print(f'Estas bajo de peso : {self.peso_final}.')
        elif self.peso_final >= 25.0:
            print(f'Estas obeso : {self.peso_final}')
        elif self.peso_final <= 24.9:
            print(f'Tienes un buen peso : {self.peso_final}.')
    
    def weight_record(self):
        try:
            # Ingreso de informacion adicional a la base de datos.
            nombre = str(input('Ingresa tu nombre y apellido para el registo: ')).strip()
            año = str(input('Ingresa el año en el que vas a registrar tu peso: ')).strip()
            mes = str(input('Ingresa el mes para dejarlo registrado junto a tu peso: ')).strip()
            if not all([nombre,año,mes]): # Validador de campos.
                print('Los campos deben estar completos.')
                return
            # Ingreso de la informacion obtenida a la base de datos.
            self.conexion.cursor.execute('''INSERT INTO peso_mes (nombre,año,mes,peso) VALUES (?,?,?,?)''',(nombre, año, mes, self.peso_final))
            self.conexion.conn.commit()
            print('Datos ingresados con exito.')
        # Manejo de errores.
        except sqlite3.Error as error:
            print(f'Error inesperado en la base de datos : {error}.')
        except Exception as error:
            print(f'Error inesperado en el programa : {error}.')
    