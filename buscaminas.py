from seting import *
import pygame

pygame.init()
pantalla = pygame.display.set_mode(RESOLUCION)
pygame.draw.rect(pantalla,COLOR_BG,(00,00,ANCHO,ALTO))
    


pygame.display.update()



while True : 
    for event in pygame.event.get():
       
        if event.type == pygame.QUIT: 
            pygame.quit() 
            quit(0)
