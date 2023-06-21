import pygame as pg
import colores

class Time:
    def __init__(self, screen, screen_width, minutos, segundos):
        self.screen = screen 
        self.screen_rect = screen.get_rect()
        self.minutos = minutos
        self.segundos = segundos
        self.font = pg.font.SysFont('Stencil', 25)
        self.rect_pos = (screen_width*0.85, 17)
        self.flag_tiempo = True
        self.update_text()
        
        
    def update_text(self):
        if self.flag_tiempo:
            self.tiempo_formateado = '{:02}:{:02}'.format(self.minutos, int(self.segundos))
            self.text = self.font.render('TIME: {}'.format(self.tiempo_formateado), True, colores.WHITE)
            self.rect_txt = self.text.get_rect() 
            self.rect_txt.midtop = self.rect_pos
        
        
    def blit_tiempo(self):
        self.screen.blit(self.text, self.rect_txt)
