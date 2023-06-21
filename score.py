import pygame as pg
import colores

class Score:
    def __init__(self, screen, screen_width, score, global_score, ganaste):
        self.screen = screen 
        self.screen_rect = screen.get_rect()
        self.score = score
        self.global_score = global_score
        self.ganaste = ganaste
        
        self.font = pg.font.SysFont('Stencil', 35)
        self.rect_pos = (screen_width/2, 15)
        self.text = self.font.render(f'SCORE: {self.score}', True, colores.WHITE)
        self.rect_txt = self.text.get_rect() 
        self.rect_txt.midtop = self.rect_pos
        
        self.font = pg.font.SysFont('Stencil', 25)
        self.rect_pos = (screen_width/3, 15)
        self.text2 = self.font.render(f'GLOBAL SCORE: {self.score}', True, colores.WHITE)
        self.rect_txt2 = self.text2.get_rect() 
        self.rect_txt2.midtop = self.rect_pos
        
    def blit_score(self):
        self.screen.blit(self.text, self.rect_txt)
        if self.ganaste:
            self.screen.blit(self.text2, self.rect_txt2)
