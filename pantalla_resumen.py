import pygame as pg

class PantallaResumen:
    def __init__(self, screen, ancho, alto, score, segundos, global_score, ganaste):
        self.screen = screen
        self.ancho = ancho
        self.alto = alto
        
        self.score = score
        self.segundos = segundos
        self.global_score = global_score
        
        if ganaste:
            self.time_score = (self.segundos // 1) * 10
        else:
            self.time_score = 0
            
        self.level_score = int(self.score + self.time_score)
        self.global_score = self.global_score + self.level_score

        
        self.superficie_transparente = pg.Surface((self.ancho, self.alto), pg.SRCALPHA)
        self.superficie_transparente.fill((0, 0, 0, 100))  # Establecer el color gris transparente (R, G, B, A)
        
        self.font1 = pg.font.SysFont('Stencil', 35)
        self.game_score_txt = self.font1.render(f'Mission Score:  {self.score}', True, 'White')
        
        self.font2 = pg.font.SysFont('Stencil', 35)
        self.time_score_txt = self.font2.render(f'Time Bonus:        {int(self.time_score)}', True, 'White')
        
        self.font3 = pg.font.SysFont('Stencil', 35)
        self.level_score_txt = self.font3.render(f'Level Score:       {self.level_score}', True, 'White')
         
        self.font4 = pg.font.SysFont('Stencil', 35)
        self.global_score_txt = self.font4.render(f'Global Score:    {self.global_score}', True, 'White')
        
        self.font5 = pg.font.SysFont('Stencil', 35)
        self.line = self.font5.render(f'----------------------------------------', True, 'White')
        
        self.font6 = pg.font.SysFont('Stencil', 20)
        self.space_txt = self.font6.render('Press SPACE', True, 'White')
        
        self.resumen_flag = False
        
    def blit_resumen(self):
        if self.resumen_flag:
            self.screen.blit(self.superficie_transparente, (0, 0))
            self.superficie_transparente.blit(self.game_score_txt, (self.ancho/2 - 190, self.alto/2 - 200))
            self.superficie_transparente.blit(self.time_score_txt, (self.ancho/2 - 190, self.alto/2 - 150))
            self.superficie_transparente.blit(self.level_score_txt, (self.ancho/2 - 190, self.alto/2 - 100))
            #self.superficie_transparente.blit(self.line, (self.ancho/2 - 190, self.alto/2 - 70))
            #self.superficie_transparente.blit(self.global_score_txt, (self.ancho/2 - 190, self.alto/2 - 45))
            self.superficie_transparente.blit(self.space_txt, (self.ancho/2 - 80, self.alto/2 + 130))