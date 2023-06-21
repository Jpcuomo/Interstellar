import sqlite3
import pygame as pg
import re

def leer_puntaje_global():
    with open("puntaje_actual.txt", "r") as archivo:
        try:
            contenido = archivo.read()
            puntaje = int(contenido)
        except:
            print('Error de archivo')
        else:
            return puntaje
    
def ingresar_obtener_iniciales():
    # Obtener el nombre del jugador
    while True:
        iniciales = input("Ingresa tus iniciales: ")
        if re.match(r'^[a-zA-Z]{1}[a-zA-Z]{1}[a-zA-Z]{1}$', iniciales):
            return iniciales
        else:
            print('Iniciales')
    

def gestionar_base_datos():
    puntaje = leer_puntaje_global()
    iniciales = ingresar_obtener_iniciales()
    with sqlite3.connect("puntuaciones.db") as conexion:
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

        # INSERT
        try:
            conexion.execute("insert into jugadores(iniciales,puntaje) values (?,?)", (iniciales, puntaje))
            conexion.commit()# Actualiza los datos realmente en la tabla
        except:
            print("Error")

        # SELECT
        cursor = conexion.execute("SELECT * FROM jugadores order by puntaje desc limit 3")
        for fila in cursor:
            print(fila)

  

def obtener_mejores_puntajes():
    
    # Obtener los puntajes desde la base de datos
    with sqlite3.connect("puntuaciones.db") as conexion:
        cursor = conexion.execute("SELECT iniciales, puntaje FROM jugadores ORDER BY puntaje DESC LIMIT 3")
        puntajes = cursor.fetchall()
        return puntajes



