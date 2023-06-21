import pygame as pg
import colores
import sys

class Text:
    def __init__(self, screen, screen_width, score, minutos, segundos) -> None:
        self.screen = screen 
        self.screen_rect = screen.get_rect()
        self.score = score
        self.minutos = minutos
        self.segundos = segundos
        self.font = pg.font.SysFont('Stencil', 30)
        self.rect_pos = (screen_width/2, 20)
        self.update_text()
        
    def update_text(self):
        self.tiempo_formateado = '{:02}:{:02}'.format(self.minutos, int(self.segundos))
        self.text = self.font.render('                            SCORE: {}                       TIME: {}'
                                     .format(self.score, self.tiempo_formateado), True, colores.WHITE)
        self.rect_txt = self.text.get_rect() 
        self.rect_txt.midtop = self.rect_pos
        
        
    def blit_header_txt(self):
        self.screen.blit(self.text, self.rect_txt)
