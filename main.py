import pygame as pg
import sqlite3
import re
import sys

from game_over import GameOver
from high_scores import HighScores
from nivel_uno import NivelUno
from nivel_dos import NivelDos
from pantalla_resumen import PantallaResumen
from portada import Portada
from tiempo import Time

        
pg.init()
pg.mixer.init()

RELOJ = pg.time.Clock()
FPS = 60

ANCHO = 1000
ALTO = 820
TAMANIO = (ANCHO, ALTO)
VENTANA = (TAMANIO)

screen = pg.display.set_mode(VENTANA)
screen_rect = screen.get_rect()
pg.display.set_caption('Interstellar')

# Banderas
mostrar_portada = True
flag_nivel_uno = False
flag_nivel_dos = False


portada = Portada(screen, ANCHO, ALTO)

flag_texto_inicio = True

mostrar_portada = True

nivel_uno = NivelUno()
nivel_dos = NivelDos()

running = True
portada.sonido_inicio.play(-1)
while running:
    RELOJ.tick(FPS)
    '''Gestiona los eventos'''
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running =  False
            sys.exit()

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                flag_texto_inicio = False # Da la orden para mostrar MISSION I al inicio de la partida
                mostrar_portada = False
                portada.sonido_inicio.stop()
                
                flag_nivel_uno = True
                nivel_uno.resumen.blit_resumen()
                flag_nivel_dos = True
                
            
    if mostrar_portada:
        portada.blit_portada()
        
        
    if not mostrar_portada and flag_nivel_uno:
        nivel_uno.RELOJ = pg.time.Clock()
        nivel_uno.musica_nivel_I.play(-1) # Activa música de partida
        nivel_uno.run()
        flag_nivel_uno = False
    elif nivel_uno.ganaste and not flag_nivel_uno and flag_nivel_dos:
        nivel_dos.RELOJ = pg.time.Clock()
        nivel_dos.resumen.blit_resumen() # Muestra resumen de puntos
        nivel_dos.musica_nivel_II.play(-1)
        nivel_dos.run()
        flag_nivel_dos = False
        
    if nivel_uno.game_over:
        mostrar_portada = True
        portada.blit_portada()
        
    pg.display.flip() 
        
pg.quit()

    
