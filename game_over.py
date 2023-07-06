import pygame as pg


class GameOver:
    def __init__(self, screen, ancho, alto, score):
        self.screen = screen
        self.rect = self.screen.get_rect()
        self.ancho = ancho
        self.alto = alto
        self.superficie_transparente = pg.Surface((ancho, alto), pg.SRCALPHA)
        self.superficie_transparente.fill((0, 0, 0, 100))  # Establecer el color gris transparente (R, G, B, A)
        self.score = score
        
        self.font1 = pg.font.SysFont('Stencil', 35)
        self.game_over = self.font1.render('GAME OVER', True, 'White')
        
        self.font2 = pg.font.SysFont('Stencil', 20)
        self.space_txt = self.font2.render('Press ENTER', True, 'Yellow')
        
        self.font3 = pg.font.SysFont('Stencil', 35)
        self.score_txt = self.font3.render(f'SCORE: {self.score}', True, 'White')

        self.perdiste = False       
        

    def blit_game_over(self):
        if self.perdiste:
            self.screen.blit(self.superficie_transparente, (0, 0))
            self.superficie_transparente.blit(self.game_over, (self.ancho/2 - 90, self.alto/2 - 100))
            self.superficie_transparente.blit(self.space_txt, (self.ancho/2 - 57, self.alto/2))
            self.superficie_transparente.blit(self.score_txt, (self.ancho/2 - 90, self.alto/2 - 200)) 
        