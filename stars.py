import pygame as pg
import random


class Stars:
    def __init__(self, ancho_ventana, alto_ventana, ventana, color, velocidad, tamanio):
        self.ancho_ventana = ancho_ventana
        self.alto_ventana = alto_ventana
        self.ventana = ventana
        self.color = color
        self.velocidad = velocidad
        self.tamanio = tamanio
        self.crear_lista_estrellas()

    def crear_lista_estrellas(self):
        self.stars = []
        for _ in range (50):
            x = random.randint(1, self.ancho_ventana - 1)
            y = random.randint(1, self.alto_ventana)
            self.stars.append([x, y])  
            
    def dibujar_estrellas(self): 
        for star in self.stars:
            pg.draw.circle(self.ventana, self.color, (star[0], star[1]), self.tamanio, 1)
            
    def mover_estrellas(self):
        for star in self.stars:
            star[1] += self.velocidad
            if star[1] > self.alto_ventana:
                star[1] = 0
     
    def update(self):
        self.dibujar_estrellas()
        self.mover_estrellas()
 
        