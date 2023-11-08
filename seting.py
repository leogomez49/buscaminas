import numpy as np
from pygame import *

ANCHO = 400
ALTO = 500
COLOR_BG = (80,80,80)
COLOR_PANEL = (50,60,50)
PANEL = ALTO//4
PANEL_RESTA =  ALTO - PANEL

GRIS = (40,40,40)
NEGRO = (50,12,12)
RESOLUCION = (ANCHO,ALTO)
ANCHO_CEL = 25
ALTO_CEL = 25
CANT_MINAS = 15
CANT_FIL = int(PANEL_RESTA/ALTO_CEL)
CANT_COL = int(ANCHO/ANCHO_CEL)
matriz = np.zeros((CANT_FIL+2,CANT_COL+2),dtype = int)

print(matriz)
print(PANEL)
