import pygame as pg
import sys
import base_de_datos_puntuacion



class HighScores:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.ventana = pg.display.set_mode((ancho, alto))
        self.lista_puntajes = base_de_datos_puntuacion.obtener_mejores_puntajes()
     
    def dibujar_puntajes(self):
        pg.init()
        mostrar_scores = True
        while mostrar_scores:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                    
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        mostrar_scores = False
        
            self.ventana.fill('Black')
            fuente = pg.font.SysFont('Stencil', 30)
            
            self.font_titulo = pg.font.SysFont('Stencil', 35)
            self.high_scores_txt = self.font_titulo.render('HIGH SCORES', True, 'White')
            
            self.font_press_enter = pg.font.SysFont('Stencil', 20)
            self.press_enter_txt = self.font_press_enter.render('Press ENTER to exit', True, 'Yellow')
            
            self.ventana.blit(self.high_scores_txt, (self.ancho // 2 - self.high_scores_txt.get_width() // 2,  85))
            self.ventana.blit(self.press_enter_txt, (self.ancho // 2 - self.press_enter_txt.get_width() // 2,  720))
            
            
            for i, (numero, iniciales, puntaje) in enumerate(self.lista_puntajes):
                texto = f"#{i + 1} -  {iniciales}  -  {puntaje:.0f}"
                render_texto = fuente.render(texto, True, 'White')
                posicion_y = 170 + i * 50
                self.ventana.blit(render_texto, (self.ancho // 2 - 105, posicion_y))
                
            pg.display.flip()  # Actualizar la ventana