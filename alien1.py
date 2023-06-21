import pygame as pg


class Alien1:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.alien_image = pg.image.load('imagenes/alien1.png')
        self.alien_image = pg.transform.scale(self.alien_image, (70,30))
        self.alien_rect = self.alien_image.get_rect()
        self.alien_rect.x = x
        self.alien_rect.y = y
        self.dict_alien = self.crear_dicc_alien()
   
        
    def crear_dicc_alien(self):
        self.dict_alien = {}
        self.dict_alien['surface'] = self.alien_image
        self.dict_alien['rect'] = self.alien_rect
        self.dict_alien['mostrar'] = True
        self.dict_alien['dispara'] = True
        self.dict_alien['valor1'] = 10
        self.dict_alien['valor2'] = 20  
        self.dict_alien['valor3'] = 30     
        return self.dict_alien
        