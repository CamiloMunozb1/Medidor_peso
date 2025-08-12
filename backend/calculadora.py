import sqlite3
import webbrowser

class IngresoDB:
    def __init__(self,ruta_db):
        try:
            self.conn = sqlite3.connect(ruta_db)
            self.cursor = self.conn.cursor()
        except sqlite3.DatabaseError as error:
            print(f'Error inesperado en la base de datos : {error}.')
            return

    def cierre_db(self):
        try:
            self.conn.close()
        except sqlite3.OperationalError as error:
            print(f'Error de operacion en la base de datos : {error}.')

class calculator_registration:
    def __init__(self,conexion):
        try:
            self.conexion = conexion
            if not conexion:
                print('No se encontro la conexion con la base de datos.')
                return
        except sqlite3.OperationalError as error:
            print(f'error de operacion en la base de datos : {error}.')
    
    def calculator_weight(self):
        peso = float(input('Ingresa tu peso: '))
        altura = float(input('Ingresa tu altura: '))
        if not peso or not altura:
            print('Todos los campos deben estar completos.')
            return
        self.peso_final = round(peso / (altura ** 2), 1)
        if self.peso_final <= 18.5:
            print(f'Estas bajo de peso : {self.peso_final}.')
        elif self.peso_final >= 25.0:
            print(f'Estas obeso : {self.peso_final}')
            webbrowser.open('https://www.youtube.com/watch?v=BKvH_qAEWkA')
        elif self.peso_final <= 24.9:
            print(f'Tienes un buen peso : {self.peso_final}.')
    
    def weight_record(self):
        try:
            año = str(input('Ingresa el año en el que vas a registrar tu peso: ')).strip()
            mes = str(input('Ingresa el mes para dejarlo registrado junto a tu peso: ')).strip()
            if not año or not mes:
                print('Los campos deben estar completos.')
                return
            self.conexion.cursor.execute('''INSERT INTO peso_mes (año,mes,peso) VALUES (?,?,?)''',(año,mes,self.peso_final))
            self.conexion.conn.commit()
            print('Datos ingresados con exito.')
        except sqlite3.Error as error:
            print(f'Error inesperado en la base de datos : {error}.')
        except Exception as error:
            print(f'Error inesperado en el programa : {error}.')
    