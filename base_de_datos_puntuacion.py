import sqlite3


def crear_base_datos():
    with sqlite3.connect("jugadores.db") as conexion:
        # Crear la tabla si no existe
        try:
            sentencia = ''' create  table jugadores
            (
            id integer primary key autoincrement,
            iniciales text,
            puntaje real
            )
            '''
            conexion.execute(sentencia)
            print("Se creó la tabla jugadores")
        except sqlite3.OperationalError:
            print("La tabla jugadores ya existe")


def insertar_datos(dicc_puntajes:dict):
    with sqlite3.connect("jugadores.db") as conexion:  
        try:
            conexion.execute("insert into jugadores(iniciales,puntaje) values (?,?)", (dicc_puntajes['iniciales'], dicc_puntajes['puntaje']))
            conexion.commit()# Actualiza los datos realmente en la tabla
        except:
            print("Error")


def obtener_mejores_puntajes()->list:
    with sqlite3.connect("jugadores.db") as conexion:
        try:
            cursor = conexion.execute("select * from jugadores order by puntaje desc limit 10")
            lista_puntajes = cursor.fetchall()
        except:
            print("Error de registros")
        return lista_puntajes

  
