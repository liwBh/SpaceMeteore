import pygame
import sys
from pygame.locals import *

pygame.init()

#Definir dimensiones de la ventana
ventana = pygame.display.set_mode((400, 300))

#Titulo de la ventana
pygame.display.set_caption("Titulo de la ventana")

#Color de fondo
colorFondo = (1, 150, 70)

# Iniciar juego
while True:
    # Agregar el color de fondo
    ventana.fill(colorFondo)
    
    # Lectura de eventos
    for evento in pygame.event.get():
      
        # evento para cerrar la ventana
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
            
    # actualiza la ventan luego de que ocurren los eventos o cambios
    pygame.display.update()