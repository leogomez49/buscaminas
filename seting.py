import numpy as np
from pygame import *

ANCHO = 400
ALTO = 500
COLOR_BG = (80,80,80)
COLOR_PANEL = (50,60,50)
PANEL = ALTO//4
GRIS = (40,40,40)
RESOLUCION = (ANCHO,ALTO)
ANCHO_CEL = 25
ALTO_CEL = 25
CANT_FIL = int(ALTO/ALTO_CEL)
CANT_COL = int(ANCHO/ANCHO_CEL)
matriz = np.zeros((CANT_FIL,CANT_COL),dtype = int)

