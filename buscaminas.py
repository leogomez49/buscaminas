from seting import *
import random
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

def colocacion_minas():
    numeros = []
        cord_x = random.randint(0, CANT_COL)
        cord_y = random.randint(0, CANT_COL)
        for i in range(1,CANT_MINAS):
            if cord_x,cord_y == numeros[i]:
                
        numeros.append((cord_x,cord_y))
    
    print(numeros)
    
    
    
colocacion_minas()



while True : 
    for event in pygame.event.get():
       
        if event.type == pygame.QUIT: 
            pygame.quit() 
            quit(0)
