import pygame as pg
import sqlite3
import re

class HighScores:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.ventana = pg.display.set_mode((ancho, alto))
     
        
    # Definir la función para dibujar los puntajes
    def dibujar_puntajes(self):
        self.ventana.fill(('Black'))  # Limpiar la pantalla
        fuente = pg.font.Font(None, 30)  # Fuente para los textos
        
        for i, (iniciales, puntaje) in enumerate(self.puntajes):
            texto = f"{iniciales}: {puntaje}"
            render_texto = fuente.render(texto, True, ('White'))
            posicion_y = 100 + i * 50
            self.ventana.blit(render_texto, (self.ancho // 2 - render_texto.get_width() // 2, posicion_y))
