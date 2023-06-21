import pygame as pg

class GameOver:
    def __init__(self, screen, ancho, alto):
        self.screen = screen
        self.rect = self.screen.get_rect()
        self.ancho = ancho
        self.alto = alto
        self.superficie_transparente = pg.Surface((ancho, alto), pg.SRCALPHA)
        self.superficie_transparente.fill((0, 0, 0, 100))  # Establecer el color gris transparente (R, G, B, A)
        
        self.font1 = pg.font.SysFont('Stencil', 35)
        self.game_over = self.font1.render('GAME OVER', True, 'White')
        
        self.font2 = pg.font.SysFont('Stencil', 20)
        self.space_txt = self.font2.render('Press SPACE', True, 'White')

        self.perdiste = False       
        
        # self.sonido_inicio = pg.mixer.Sound("sonidos/04 underground cavern.ogg")
        # self.sonido_inicio.set_volume(0.1)
        # self.sonido_inicio.play()
        # self.sonido_inicio.stop() 

    def blit_game_over(self):
        if self.perdiste:
            self.screen.blit(self.superficie_transparente, (0, 0))
            self.superficie_transparente.blit(self.game_over, (self.ancho/2 - 90, self.alto/2 - 100))
            self.superficie_transparente.blit(self.space_txt, (self.ancho/2 - 57, self.alto/2))