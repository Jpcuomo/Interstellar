import pygame as pg
from alien1 import Alien1
import random

class Alien_fleet:
    def __init__(self, screen, speed, ancho, alto, bala_inst, prob_disparo):
        self.screen = screen
        self.speed = speed
        self.ancho = ancho
        self.alto = alto
        self.alien_spacing_x = 50  # Espacio entre aliens
        self.alien_spacing_y = 60
        self.alien_rows = 3  # Número de filas de aliens
        self.alien_columns = 8  # Número de columnas de aliens
        self.alien_width = 50  # Ancho de cada alien
        self.alien_height = 5  # Alto de cada alien
        self.lista_aliens = self.crear_lista_aliens()
        self.direccion = 1
        self.bala_alien = bala_inst
        self.prob_disparo = prob_disparo
        
        pg.mixer.music.set_volume(0.1)
        self.sonido_bala_alien = pg.mixer.Sound("sonidos/explosiones/sfx_wpn_laser7.wav")
        self.sonido_bala_alien.set_volume(0.2)
        self.sonido_bala_alien.play()
        self.sonido_bala_alien.stop()

    def crear_lista_aliens(self):
        self.lista_aliens = []
        for row in range(self.alien_rows):
            for column in range(self.alien_columns):
                x = self.alien_spacing_x + column * (self.alien_width +self. alien_spacing_x)
                y = self.alien_spacing_y + row * (self.alien_height + self.alien_spacing_y)
                alien = Alien1(self.screen, x, y)
                self.lista_aliens.append(alien.dict_alien)
        return self.lista_aliens

    def mover_flota(self):
        for alien in self.lista_aliens:
            alien['rect'].x += self.speed * self.direccion
            
        if self.lista_aliens[-1]['rect'].right >= self.ancho - 50 or self.lista_aliens[0]['rect'].left <= 50:
            self.direccion *= -1
            if alien in self.lista_aliens[17:]:
                self.lista_aliens[random.randint(16,len(self.lista_aliens)-1)]['rect'].y += random.randint(50, 200)
            elif alien in self.lista_aliens[8:16]:
                self.lista_aliens[random.randint(8,16)]['rect'].y += 50
            elif alien in self.lista_aliens[:8]:
                self.lista_aliens[random.randint(8,16)]['rect'].y += 50
        self.lista_aliens[random.randint(0,len(self.lista_aliens)-1)]['rect'].y += 5
        
    def update_bala_alien(self):
        # código de actualización de las naves enemigas
        # Verificar si una nave enemiga debe disparar
        for alien in self.lista_aliens:
            if alien['mostrar'] and random.random() < self.prob_disparo:  # Probabilidad de disparo del 1%
                self.disparar_bala_alien(alien)
                self.sonido_bala_alien.play()
        
    def disparar_bala_alien(self, alien):
        # Crear una bala en la posición del alien y agregarla a la lista de balas enemigas
        nueva_bala = {
            'rect': pg.Rect(alien['rect'].centerx, alien['rect'].bottom, 3, 20),
            'disparar': True
        }
        self.bala_alien.lista_balas.append(nueva_bala)
        
    def draw(self):
        self.mover_flota()
        for i, alien in enumerate(self.lista_aliens):
            if alien['mostrar']:
                
                #pg.draw.rect(self.screen, 'Yellow', alien['rect'], width=2)
                self.screen.blit(alien['surface'], alien['rect'])