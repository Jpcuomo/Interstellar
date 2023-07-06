import pygame as pg
import sys
import re

pg.init()

#Dibujar la pantalla de ingreso de iniciales
def dibujar_ingreso_iniciales(pantalla:object, iniciales_jugador:str):
    fuente_superior = pg.font.SysFont('Stencil', 35)
    fuente_inferior = pg.font.SysFont('Stencil', 20)
    
    pantalla.fill((0, 0, 0))

    line = fuente_superior.render(f'-------------', True, 'White')
    texto = fuente_superior.render('Enter your initials', 1, 'White')
    texto2 = fuente_superior.render(iniciales_jugador, 1, 'Red')
    texto3 = fuente_inferior.render('Press ENTER to continue', 1, 'Yellow')
  
    pantalla.blit(texto, (500 - (texto.get_width()/2), 200))
    pantalla.blit(texto2, (500 - (texto2.get_width()/2) , 360))
    pantalla.blit(texto3, (500 - (texto3.get_width()/2), 610))
    pantalla.blit(line, (500 - (line.get_width()/2), 380))
    
    pg.display.update()


def validar_iniciales(letra:str):
    # Obtener iniciales del jugador
    if type(letra) == str:
        if re.match(r'^[a-zA-Z]{1}$', letra):
            resultado = True
        else:
            resultado = False
    else: 
        resultado = False
        
    return resultado
    

#Pantalla para ingreso de iniciales
def pantalla_ingreso_iniciales(pantalla:object, dicc_jugador:dict)->None: 
    iniciales_jugador = ''
    ingreso_nombre = True
    while ingreso_nombre == True:
        
        for event in pg.event.get():
            if event.type == pg.QUIT: #Permite cerrar el juego
                ingreso_nombre = False
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    iniciales_jugador = iniciales_jugador[:-2]
                    
                elif event.key == pg.K_RETURN and len(iniciales_jugador) > 0:
                    dicc_jugador['iniciales'] = iniciales_jugador.upper()
                    ingreso_nombre = False
                    return iniciales_jugador
                
                elif event.key == pg.K_SPACE:
                    iniciales_jugador += ''
                    
                else:
                    letra = event.unicode
                    if validar_iniciales(letra) and len(iniciales_jugador) < 6:
                        iniciales_jugador += f'{letra}.'
            
        dibujar_ingreso_iniciales(pantalla, iniciales_jugador)

