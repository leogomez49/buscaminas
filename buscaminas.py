import random
from seting import *
import pygame

pygame.init()
Pantalla = pygame.display.set_mode(RESOLUCION)
pygame.draw.rect(Pantalla,COLOR_BG,(00,00,ANCHO,ALTO))
pygame.draw.rect(Pantalla,COLOR_PANEL,(00,00,ANCHO,PANEL))
for ancho in range(0,ANCHO,ANCHO_CEL):
    pygame.draw.line(Pantalla,GRIS,(ancho,PANEL),(ancho,ALTO),1)
for alto in range(PANEL,(ALTO+1),ALTO_CEL):
    pygame.draw.line(Pantalla,GRIS,(0,alto),(ANCHO,alto),1)    


pygame.display.update()


def aleatoriedad():
    cord_x = random.randint(0,CANT_COL-1)
    cord_y = random.randint(0,CANT_FIL-1)
    return cord_x,cord_y
    
def colocacion_minas():
    numeros = []
    minas_colocadas = 0
    while CANT_MINAS != minas_colocadas:
        cordenadas = aleatoriedad()
        if cordenadas not in numeros:
            numeros.append(cordenadas)
            minas_colocadas += 1
            matriz[cordenadas] = 1
            
        
    
    print(matriz)
    
    
    
colocacion_minas()



while True : 
    for event in pygame.event.get():
       
        if event.type == pygame.QUIT: 
            pygame.quit() 
            quit(0)
