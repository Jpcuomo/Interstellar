import pygame as pg
import sys

from nivel_uno import NivelUno
from nivel_dos import NivelDos
from portada import Portada
import pantalla_iniciales
import base_de_datos_puntuacion
from high_scores import HighScores

        
pg.init()
pg.mixer.init()
pg.mixer.music.set_volume(0.7)

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
flag_texto_inicio = True


base_de_datos_puntuacion.crear_base_datos()

# Instancia de portada
portada = Portada(screen, ANCHO, ALTO)
    

dicc_jugador = {'iniciales':'', 'puntaje':0} 

nivel_uno = NivelUno(dicc_jugador['iniciales'], dicc_jugador['puntaje'])
nivel_dos = NivelDos(dicc_jugador['iniciales'], dicc_jugador['puntaje'])
    
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
            if event.key == pg.K_RETURN:
                dicc_jugador['iniciales'] = pantalla_iniciales.pantalla_ingreso_iniciales(screen, dicc_jugador)
                
                flag_texto_inicio = False # Da la orden para mostrar MISSION I al inicio de la partida
                mostrar_portada = False
                portada.sonido_inicio.stop()
                flag_nivel_uno = True
                nivel_uno.resumen.blit_resumen()
                flag_nivel_dos = True
                nivel_dos = NivelDos(dicc_jugador['iniciales'], dicc_jugador['puntaje'])
                nivel_dos.resumen.blit_resumen()
            
    if mostrar_portada:
        portada.blit_portada()
         
    # Condición para dar inicio a nivel I
    if not mostrar_portada and flag_nivel_uno:
        nivel_uno = NivelUno(dicc_jugador['iniciales'], dicc_jugador['puntaje'])
        nivel_uno.RELOJ = pg.time.Clock()
        nivel_uno.musica_nivel_I.play(-1) # Activa música de partida
        perdiste = nivel_uno.run()
        #print(perdiste)
        dicc_jugador['puntaje'] = nivel_uno.colision_bala_jugador_con_alien()        
        flag_nivel_uno = False
        high_scores = HighScores(ANCHO, ALTO)
        if perdiste:
            high_scores.dibujar_puntajes()
        mostrar_portada = True
        
    # Condición para dar inicio a nivel II
    elif nivel_uno.ganaste and not flag_nivel_uno and flag_nivel_dos:
        nivel_dos = NivelDos(dicc_jugador['iniciales'], dicc_jugador['puntaje'])
        nivel_dos.RELOJ = pg.time.Clock()
        nivel_dos.musica_nivel_II.play(-1)
        nivel_dos.run()
        dicc_jugador['puntaje'] = nivel_dos.colision_bala_jugador_con_alien()
        flag_nivel_dos = False
        high_scores = HighScores(ANCHO, ALTO)
        high_scores.dibujar_puntajes()
        mostrar_portada = True
        
    pg.display.flip() 
        
pg.quit()

    