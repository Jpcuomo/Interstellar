import pygame as pg

class Explosion:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.current_frame = 0
        self.frame_delay = 10  # Retraso entre frames de la animación
        self.frame_timer = 0
        self.active = False
        self.frames = self.cargar_cuadros()
        
        pg.mixer.music.set_volume(0.4)
        self.sonido_explosion_alien = pg.mixer.Sound("sonidos/explosiones/sfx_exp_shortest_soft9.wav")
        self.sonido_explosion_alien.play()
        self.sonido_explosion_alien.stop()
        
        self.sonido_explosion_nave = pg.mixer.Sound("sonidos/explosiones/sfx_exp_shortest_soft9.wav")
        self.sonido_explosion_nave.play()
        self.sonido_explosion_nave.stop()
        

    def cargar_cuadros(self):
        frames = []
        lista_archivos = []
        for i in range(6, 24):
            lista_archivos.append(f'imagenes/explosion/{i}.png')
        
        for file in lista_archivos:
            img = pg.image.load(file)
            img = pg.transform.scale(img, (70,70))
            frames.append(img)
        return frames


    def update(self):
        if self.active:
            self.frame_timer += 10
            if self.frame_timer >= self.frame_delay:
                self.current_frame += 1
                self.frame_timer = 0
                if self.current_frame >= len(self.frames):
                    self.active = False


    def draw(self, screen):
        if self.active:
            screen.blit(self.frames[self.current_frame], (self.x, self.y))
            
