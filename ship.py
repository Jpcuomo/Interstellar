import pygame as pg


class Ship:
    '''Clase para seteos de nave principal'''
    def __init__(self, screen, screen_rect, speed) -> None:
        self.screen = screen 
        self.screen_rect = screen_rect
        
        self.speed = speed
        
        self.ship_image_left = pg.image.load('imagenes/ship-3.png')
        self.ship_image_left = pg.transform.scale(self.ship_image_left, (57,50))
        self.ship_image_right = pg.image.load('imagenes/ship3.png')
        self.ship_image_right = pg.transform.scale(self.ship_image_right, (57,50))
        self.ship_image_upright = pg.image.load('imagenes/ship0.png') 
        self.ship_image_upright = pg.transform.scale(self.ship_image_upright, (57,50))
        
        self.ship_image = self.ship_image_upright
        
        # Crea el rectangulo que contiene a la nave
        self.rect_ship = self.ship_image.get_rect() 
        self.rect_ship.midbottom = self.screen_rect.midbottom
        self.rect_ship.y -= 30 # Posición inicial en y
        
        self.dict_ship = {}
        self.dict_ship['rect'] = self.rect_ship
        self.dict_ship['left_image'] = self.ship_image_left
        self.dict_ship['right_image'] = self.ship_image_right
        self.dict_ship['upright_image'] = self.ship_image_upright
        self.dict_ship['mostrar'] = True
        
        
    def move_ship(self, flag):
        if flag == 'left':
            if self.dict_ship['rect'].x > 0:
                self.dict_ship['rect'].x -= self.speed
            self.update_image()
        elif flag == 'right':
            if self.dict_ship['rect'].right < self.screen_rect.width:
                self.dict_ship['rect'].x += self.speed
            self.update_image()
        if flag == 'up':
            if self.dict_ship['rect'].top >= 0:
                self.dict_ship['rect'].y -= self.speed
        elif flag == 'down':
            if self.dict_ship['rect'].bottom <= self.screen_rect.height:
                self.dict_ship['rect'].y += self.speed
        

    
    def update_image(self, direction='upright'):
        if direction == 'left':
            self.ship_image = self.dict_ship['left_image']
        elif direction == 'right':
            self.ship_image = self.dict_ship['right_image']
        else:
            self.ship_image = self.dict_ship['upright_image']
            
    # @property
    # def x(self):
    #     return self.rect_ship.x

    # @x.setter
    # def x(self, value):
    #     self.rect_ship.x = value

    # @property
    # def y(self):
    #     return self.rect_ship.y

    # @y.setter
    # def y(self, value):
    #     self.rect_ship.y = value

        
    def blit_ship(self):
        if self.dict_ship['mostrar']:
            #pg.draw.rect(self.screen, 'Yellow', self.rect_ship, width=2)
            self.screen.blit(self.ship_image, self.rect_ship)
        