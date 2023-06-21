import pygame as pg
import colores
import sqlite3
import re
import sys

from alien_fleet import Alien_fleet
from balas import Balas
from explosion import Explosion
from game_over import GameOver
from high_scores import HighScores
from pantalla_resumen import PantallaResumen
from portada import Portada
from score import Score
from ship import Ship
from stars import Stars
from tiempo import Time
from vidas import Vida



class NivelUno:
    '''Clase principal que maneja las generalidades del juego Interstellar'''
    def __init__(self) -> None:
        pg.init()
        pg.mixer.init()

        self.musica_nivel_I = pg.mixer.Sound("sonidos/explosiones/06 pirates attack.ogg")
        self.musica_nivel_I.play(-1)
        self.musica_nivel_I.set_volume(0.2)
        self.musica_nivel_I.stop()

        self.ANCHO = 1000
        self.ALTO = 820
        self.screen_size = ((self.ANCHO, self.ALTO))

        self.screen = pg.display.set_mode(self.screen_size)
        self.screen_rect = self.screen.get_rect()

        self.bg_image = pg.image.load('imagenes/stars.png')
        self.bg_image = pg.transform.scale(self.bg_image, (self.ANCHO,self.ALTO))
        pg.display.set_caption('** Interstellar **')

        # Rectangulo limite inferior de pantalla
        self.rect_inferior = pg.Rect(0, self.ALTO, self.ANCHO, 2)

        self.FPS = 60
        self.score = 0
        self.minutos = 0
        self.segundos = 40
        self.global_score = 0
        self.contador_colisiones = 0
        self.RELOJ = pg.time.Clock()

        self.BEGINING_TEXT = pg.USEREVENT + 0
        font = pg.font.Font(None, 36)
        self.text = font.render("MISSION I", True, (255, 255, 255))
        pg.time.set_timer(self.BEGINING_TEXT, 3000)
        self.mostrar_texto_inicio = True

        self.mostrar_portada = True

        self.ganaste = False


        '''Instancias de clases #####################################################################'''
        self.ship = Ship(self.screen, self.screen_rect, 3)
        self.puntaje = Score(self.screen, self.ANCHO, self.score, self.global_score, self.ganaste)
        self.resumen = PantallaResumen(self.screen, self.ANCHO, self.ALTO, self.score, self.segundos, self.global_score, self.ganaste)
        self.tiempo = Time(self.screen, self.ANCHO, self.minutos, self.segundos)

        self.stars1 = Stars(self.ANCHO, self.ALTO, self.screen, colores.GRIS, 0.5, 1)
        self.stars2 = Stars(self.ANCHO, self.ALTO, self.screen, colores.GRIS, 0.07, 1)
        self.stars3 = Stars(self.ANCHO, self.ALTO, self.screen, colores.GRIS, 0.1, 1)

        self.path_bala_jugador = 'imagenes/PlayerLaser.png'
        self.path_bala_alien = 'imagenes/EnemyLaser.png'
        self.bala_jugador = Balas(self.screen, self.ship.rect_ship, 2, self.path_bala_jugador, 'jugador')
        self.bala_alien = Balas(self.screen, self.ship.rect_ship, 5, self.path_bala_alien, 'alien')

        self.alien_fleet = Alien_fleet(self.screen, 1, self.ANCHO, self.ALTO, self.bala_alien, 0.002)

        self.explosion_nave = None
        self.explosion_alien = None

        self.vida1 = Vida(self.screen, 40 , 12)
        self.vida2 = Vida(self.screen, 95, 12)
        self.vida3 = Vida(self.screen, 150, 12)

        self.game_over = GameOver(self.screen, self.ANCHO, self.ALTO)
        self.portada = Portada(self.screen, self.ANCHO, self.ALTO)

        self.high_scores = HighScores(self.ANCHO, self.ALTO)

        '''Instancias de clases #####################################################################'''


    def update_time(self):
        '''Calcula el tiempo transcurrido dentro del juego'''
        '''Muestra el tiempo formateado en pantalla'''
        self.segundos -= self.RELOJ.get_time() / 1000
        if self.segundos >= 60:
            self.minutos -= 1
            self.segundos = 0
        self.tiempo.minutos = self.minutos
        self.tiempo.segundos = self.segundos
        self.tiempo.update_text()


    def fin_de_tiempo(self):
        '''Finaliza la partida cuando el tiempo es 0:00'''
        if self.tiempo.tiempo_formateado == '00:00' and self.tiempo.flag_tiempo:
            self.explosion_nave = Explosion(self.ship.dict_ship['rect'].x, self.ship.dict_ship['rect'].y)
            self.explosion_nave.active = True
            self.game_over.perdiste = True
            self.vida1.dict_vida['mostrar'] = False
            self.vida2.dict_vida['mostrar'] = False
            self.vida3.dict_vida['mostrar'] = False
            self.ship.dict_ship['mostrar'] = False
            self.bala_jugador.dict_balas['disparar'] = False
            self.tiempo.flag_tiempo = False
            self.guardar_puntaje_global(self.global_score)


    def colision_bala_jugador_con_alien(self):
        '''Maneja las colisiones entre las balas del jugador y las aliens'''
        nuevos_aliens = [] # Almacena los aliens que no han sido alcanzados por una bala
        for bala in self.bala_jugador.lista_balas:
            for alien in self.alien_fleet.lista_aliens:
                if bala['disparar'] and alien['mostrar'] and bala['rect'].colliderect(alien['rect']) and  self.ship.dict_ship['mostrar']:
                    if alien in self.alien_fleet.lista_aliens[:8]:
                        self.score += alien['valor3']
                    elif alien in self.alien_fleet.lista_aliens[8:17]:
                            self.score += alien['valor2']
                    elif alien in self.alien_fleet.lista_aliens[17:]:
                            self.score += alien['valor1']
                    self.explosion_alien = Explosion(alien['rect'].x, alien['rect'].y)
                    self.explosion_alien.active = True
                    self.explosion_alien.sonido_explosion_alien.play()
                    self.puntaje = Score(self.screen, self.ANCHO, self.score, self.global_score, self.ganaste)
                    self.resumen = PantallaResumen(self.screen, self.ANCHO, self.ALTO, self.score, self.segundos, self.global_score, alien['mostrar'])
                    bala['disparar'] = False
                    alien['mostrar'] = False
                if alien['mostrar']: # Si el alien sigue siendo visible se agrega a la lista nuevos_aliens
                    nuevos_aliens.append(alien)
        self.lista_aliens = nuevos_aliens
        if len(nuevos_aliens) == 0 and alien['mostrar'] == False: # Si mate a todos los aliens:
            self.tiempo.flag_tiempo = False # Frena el tiempo
            self.ganaste = True
            self.resumen.resumen_flag = True # Habilita que se muestre la pantalla reumen
            self.global_score = self.resumen.global_score
            self.musica_nivel_I.stop() # Apaga música de partida
            self.guardar_puntaje_global(self.global_score)
            return self.ganaste
        
            

    def guardar_puntaje_global(self, global_score):
        '''Guarda en un txt el puntaje global de la partida al eliminar
        a todos los aliens'''
        try:
            with open('puntaje_actual.txt', 'w') as archivo:
                archivo.write(str(global_score))
        except:
            print('Error!!!')


    def colision_alien_piso(self):
        '''Termina el juego cuando una de las aliens llega al final de la pantalla'''
        contador = 0
        for alien in self.alien_fleet.lista_aliens:

            if alien['rect'].bottom >= self.rect_inferior.top and alien['mostrar'] and self.ship.dict_ship['mostrar']:
                contador += 1
                print('Fuiste invadido!!')
                if contador == 1:
                    self.explosion_nave = Explosion(self.ship.dict_ship['rect'].x, self.ship.dict_ship['rect'].y)
                    self.explosion_nave.active = True
                    self.explosion_nave.sonido_explosion_nave.play()
                    self.game_over.perdiste = True
                    self.vida1.dict_vida['mostrar'] = False
                    self.vida2.dict_vida['mostrar'] = False
                    self.vida3.dict_vida['mostrar'] = False
                    self.game_over.perdiste = True
                    self.ship.dict_ship['mostrar'] = False
                    self.bala_jugador.dict_balas['disparar'] = False
                    self.tiempo.flag_tiempo = False
                    self.musica_nivel_I.stop() # Apaga música de partida


    def colision_nave_y_alien(self):
        '''Maneja las colisiones entre la nave del jugador y las naves enemigas'''
        for alien in self.alien_fleet.lista_aliens:
            if alien['rect'].colliderect(self.ship.dict_ship['rect']) and alien['mostrar'] and  self.ship.dict_ship['mostrar']:
                self.contador_colisiones += 1
                self.explosion_nave = Explosion(self.ship.dict_ship['rect'].x, self.ship.dict_ship['rect'].y)
                self.explosion_nave.active = True
                self.explosion_alien = Explosion(alien['rect'].x, alien['rect'].y)
                self.explosion_alien.active = True
                self.explosion_nave.sonido_explosion_nave.play()
                self.ship.dict_ship['mostrar'] = False
                alien['mostrar'] = False
                if self.contador_colisiones == 1:
                    self.vida3.dict_vida['mostrar'] = False
                elif self.contador_colisiones == 2:
                    self.vida2.dict_vida['mostrar'] = False
                elif self.contador_colisiones == 3:
                    self.vida1.dict_vida['mostrar'] = False
                print('Haz colisionado!!')
                # Si la nave colisiona se reinicia su posicion
                self.ship.dict_ship['mostrar'] = True
                self.ship.dict_ship['rect'].midbottom = self.screen_rect.midbottom
                self.ship.dict_ship['rect'].y -= 30

        if not self.vida1.dict_vida['mostrar'] and not self.vida2.dict_vida['mostrar'] and not self.vida3.dict_vida['mostrar']:
            self.game_over.perdiste = True
            self.ship.dict_ship['mostrar'] = False
            self.bala_jugador.dict_balas['disparar'] = False
            self.tiempo.flag_tiempo = False
            self.musica_nivel_I.stop() # Apaga música de partida


    def colision_bala_alien_con_jugador(self):
        for bala in self.bala_alien.lista_balas:
            if bala['disparar'] and bala['rect'].colliderect(self.ship.dict_ship['rect']) and self.ship.dict_ship['mostrar']:
                self.contador_colisiones += 1
                self.explosion_nave = Explosion(self.ship.dict_ship['rect'].x, self.ship.dict_ship['rect'].y)
                self.explosion_nave.active = True
                self.explosion_nave.sonido_explosion_nave.play()
                self.ship.dict_ship['mostrar'] = False
                bala['disparar'] = False
                if self.contador_colisiones == 1:
                    self.vida3.dict_vida['mostrar'] = False
                    print('1')
                elif self.contador_colisiones == 2:
                    self.vida2.dict_vida['mostrar'] = False
                    print('2')
                elif self.contador_colisiones == 3:
                    self.vida1.dict_vida['mostrar'] = False
                    print('3')
                # Si la nave colisiona se reinicia su posicion
                self.ship.dict_ship['mostrar'] = True
                self.ship.dict_ship['rect'].midbottom = self.screen_rect.midbottom
                self.ship.dict_ship['rect'].y -= 30

        if not self.vida1.dict_vida['mostrar'] and not self.vida2.dict_vida['mostrar'] and not self.vida3.dict_vida['mostrar']:
            self.game_over.perdiste = True
            self.ship.dict_ship['mostrar'] = False
            self.bala_jugador.dict_balas['disparar'] = False
            self.tiempo.flag_tiempo = False
            self.musica_nivel_I.stop() # Apaga música de partida


    def run(self):
        '''Loop principal'''
        self.running = True
        while self.running:
            self.update_screen() # Actualiza visualizaciones y sonidos
            self.check_events()
            self.pressed_key()
            #if not self.ganaste or not self.game_over.perdiste: # Actualiza tiempo y colisiones si no perdi o no gane (estoy jugando)
            self.update_time()
            self.RELOJ.tick(self.FPS) # controlar la velocidad de actualización del juego
            self.colision_bala_jugador_con_alien()
            self.fin_de_tiempo()
            self.colision_alien_piso()
            self.colision_nave_y_alien()
            self.alien_fleet.update_bala_alien()
            self.colision_bala_alien_con_jugador()


    def check_events(self):
        '''Gestiona los eventos'''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running =  False

            elif event.type == self.BEGINING_TEXT:
                self.mostrar_texto_inicio = False # Da la orden para mostrar MISSION I al inicio de la partida

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    if not self.game_over.perdiste:
                        self.bala_jugador.disparar_bala()
                        self.bala_jugador.sonido_inicio.play()
                        
            # elif self.game_over.perdiste:
            #             self.portada.blit_portada() # Si perdi, SPACE se usa para ir a la portada e iniciar el juego
            #             nivel_uno = NivelUno()
            #             nivel_uno.run()
                        
                    


    def pressed_key(self):
        '''Maneja acciones con teclas mantenidas presionadas'''
        pressed_keys = pg.key.get_pressed()

        if True in pressed_keys:
            if pressed_keys[pg.K_LEFT]:
                flag = 'left'
                self.ship.move_ship(flag)
                self.ship.update_image(flag)

            if pressed_keys[pg.K_RIGHT]:
                flag = 'right'
                self.ship.move_ship(flag)
                self.ship.update_image(flag)

            if pressed_keys[pg.K_UP]:
                flag = 'up'
                self.ship.move_ship(flag)

            if pressed_keys[pg.K_DOWN]:
                flag = 'down'
                self.ship.move_ship(flag)
        else:
            self.ship.update_image()


    def update_screen(self):
        
        self.screen.blit(self.bg_image, self.ship.screen_rect) # Muestra imagen de fondo
        self.stars1.update() # Animaciones de fondo
        self.stars2.update()
        self.stars3.update()

        if self.explosion_alien:
            self.explosion_alien.update()
            self.explosion_alien.draw(self.screen)

        self.alien_fleet.draw()
        self.bala_jugador.blit_balas()
        self.bala_alien.blit_balas()
        self.tiempo.blit_tiempo()
        self.puntaje.blit_score()
        self.vida1.blit_vida()
        self.vida2.blit_vida()
        self.vida3.blit_vida()

        if self.explosion_nave:
            self.explosion_nave.update()
            self.explosion_nave.draw(self.screen)
        self.ship.blit_ship()

        if self.mostrar_texto_inicio:
                self.screen.blit(self.text, (self.ANCHO/2 - 57, self.ALTO/2)) # Muestra MISSION X al inicio de la partida

        if self.game_over.perdiste:
                self.game_over.blit_game_over() # Muestra pantalla de GAME OVER
                
                
        if self.ganaste:
            if self.resumen.resumen_flag:
                self.resumen.blit_resumen() # Muestra resumen de puntos
                
                    
        pg.display.flip()
