import random
from seting import *
import pygame
import math

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
    cord_x = random.randint(0+1,CANT_COL-2)
    print(CANT_COL)
    cord_y = random.randint(0+1,CANT_FIL-2)
    return cord_x,cord_y
    
def colocacion_minas():
    numeros = []
    minas_colocadas = 0
    while CANT_MINAS != minas_colocadas:
        cordenadas = aleatoriedad()
        if cordenadas not in numeros:
            numeros.append(cordenadas)
            minas_colocadas += 1
            matriz[cordenadas] = 9
        
    print(matriz)
    
def xontador_vexinos(X,Y):
  vecinos = 0      
  for b in range(X-1,X+2):
    jup = b
    for v in range(Y-1, Y+2):
      up = v
      if not(X == jup and Y == up) and matriz[jup][up] == 9:
        vecinos += 1
        #print(X,Y)
        #print(vecinos)
  return vecinos

def nace ():
    global matriz
    matriz_2 = np.copy(matriz)

    for p in range(1,CANT_FIL+1):
      matrizX3 = p
      for o in range(1,CANT_COL+1):
        matrizY3 = o
        if matriz[matrizX3,matrizY3] == 9:
            continue
        else:
            vecinos = xontador_vexinos(matrizX3,matrizY3)
            matriz_2[matrizX3,matrizY3] = vecinos 
    matriz = matriz_2

def dibujar_cel(FILA,COLUMNA):
    #Codigo uno
    if matriz[FILA+1-(PANEL//ALTO_CEL)][COLUMNA+1] == 1:
        pygame.draw.rect(Pantalla,NEGRO,(ANCHO_CEL*COLUMNA+1,ALTO_CEL*FILA+1,ANCHO_CEL-1,ALTO_CEL-1))
    else: pygame.draw.rect(Pantalla,NEGRO,(ANCHO_CEL*COLUMNA+1,ALTO_CEL*FILA+1,ANCHO_CEL-1,ALTO_CEL-1))
    print(matriz)



colocacion_minas()
nace()
print("")
print(matriz)


while True : 
    for event in pygame.event.get():
       
        if event.type == pygame.QUIT: 
            pygame.quit() 
            quit(0)
            
        if event.type == pygame.MOUSEBUTTONDOWN:
          coord_col = int(math.floor(event.pos[0]/ANCHO_CEL))
          print(event.pos[1])
          coord_fil = int(math.floor((event.pos[1])/ALTO_CEL)) 
          
          
          dibujar_cel(coord_fil,coord_col)
          
          pygame.display.update()
          #print(MATRIZ)
                      
