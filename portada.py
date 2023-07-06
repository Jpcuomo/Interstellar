import pygame as pg


class Portada:
    def __init__(self, screen, ancho, alto):
        self.screen = screen
        self.rect = self.screen.get_rect()
        self.ancho = ancho
        self.alto = alto
        self.fondo = pg.Surface((self.ancho, self.alto))
    
        
        self.font1 = pg.font.SysFont('Stencil', 50)
        self.interstellar = self.font1.render('INTERSTELLAR', True, 'White')
        
        self.font2 = pg.font.SysFont('Stencil', 20)
        self.space_txt = self.font2.render('Press ENTER', True, 'Yellow')

        
        self.sonido_inicio = pg.mixer.Sound("sonidos/explosiones/03 ship interior.ogg")
        self.sonido_inicio.set_volume(0.3)
        

    def blit_portada(self):
        self.screen.blit(self.fondo, self.rect)
        self.screen.blit(self.space_txt, (500 - (self.space_txt.get_width()/2), self.alto/2 + 200))
        self.screen.blit(self.interstellar, (500 - (self.interstellar.get_width()/2), self.alto/2 - 200))