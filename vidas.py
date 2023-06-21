import pygame as pg

class Vida:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.imagen_vida = pg.image.load('imagenes/ship0.png')
        self.imagen_vida = pg.transform.scale(self.imagen_vida, (37,30))
        self.vida_rect = self.imagen_vida.get_rect()
        self.vida_rect.x = x
        self.vida_rect.y = y
        self.dict_vida = {}
        self.dict_vida['imagen'] = self.imagen_vida
        self.dict_vida['rect'] = self.vida_rect
        self.dict_vida['mostrar'] = True
    
    
    def blit_vida(self):
        if self.dict_vida['mostrar']:
            self.screen.blit(self.dict_vida['imagen'], self.dict_vida['rect'])