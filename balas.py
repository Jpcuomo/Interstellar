import pygame as pg

class Balas:
    def __init__(self, screen, rect_ship, bullet_speed, path, objeto):
        self.screen = screen
        self.rect_ship = rect_ship
        
        pg.mixer.music.set_volume(0.3)
        self.sonido_inicio = pg.mixer.Sound("sonidos/explosiones/sfx_wpn_cannon4.wav")
        self.sonido_inicio.set_volume(0.1)
        self.sonido_inicio.play()
        self.sonido_inicio.stop()
        
        
        self.path = path
        self.bullet_image = pg.image.load(path)
        self.bullet_image = pg.transform.scale(self.bullet_image, (3,20))
        self.bullet_rect = self.bullet_image.get_rect()
        self.bullet_rect.midtop = self.rect_ship.midtop
        self.y = float(self.bullet_rect.y)
        self.objeto = objeto
       
        self.bullet_speed = bullet_speed
        self.dict_balas = self.crear_dict_balas()
        self.lista_balas = self.crear_lista_balas()
                
    def crear_dict_balas(self):
        dict_balas = {}
        dict_balas['imagen'] = self.bullet_image
        dict_balas['rect'] = self.bullet_rect
        dict_balas['disparar'] = False
        return dict_balas

    def crear_lista_balas(self):
        lista_balas = []
        for _ in range(10):
            lista_balas.append(self.dict_balas)
        return lista_balas

    '''Metodo usado solo para balas del jugador''' 
    def disparar_bala(self):
        for bala in self.lista_balas:
            if not bala['disparar']:
                bala['rect'].midtop = self.rect_ship.midtop
                bala['disparar'] = True

    def mover_bala(self):
        for bala in self.lista_balas:
            if bala['disparar'] and bala['rect'].y > 0 and self.objeto == 'jugador':
                bala['rect'].y -= self.bullet_speed
            elif bala['disparar'] and bala['rect'].y > 0 and self.objeto == 'alien':
                bala['rect'].y += self.bullet_speed
            elif bala['rect'].y <= 0 or bala['rect'].y >= 820:
                bala['disparar'] = False
                
    def blit_balas(self):
        self.mover_bala()
        for bala in self.lista_balas:
            if bala['disparar']:
                #pg.draw.rect(self.screen, 'Yellow', bala['rect'], width=2)
                self.screen.blit(self.bullet_image, bala['rect'])
                
