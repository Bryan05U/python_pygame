import pygame
import math
from triangle import Triángulo

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
screen = pygame.display.set_mode((800, 600)) # Tamaño de la ventana
pygame.display.set_caption("Normalized Diagonal Movement of the Triangle") # Título de la ventana

# Color de fondo
background_color = (0, 0 ,0)

# Posición inicial del triángulo
triángulo = Triángulo(400, 300)

# Definir la velocidad constante
v_constante = 1

# Vector de dirección diagonal
dirección = (1, 1)

# Calcular la magnitud del vector de dirección
magnitud = math.sqrt(dirección[0]**2 + dirección[1]**2)

# Normalizar el vector de dirección
dirección_normalizada = (dirección[0] / magnitud, dirección[1] / magnitud)

# Calcular el vector de movimiento
velocidad = (dirección_normalizada[0] * v_constante, dirección_normalizada[1] * v_constante)

# Bucle principal del juego
running = True
while running:
    # Evento para cerrar la ventana
    for event in pygame.event.get(): # Lista de Eventos
        if event.type == pygame.QUIT:
            running = False

    # Estado de las teclas
    teclas = pygame.key.get_pressed()

    # Mover el triángulo
    triángulo.mover(teclas)

    # Pintar el fondo
    screen.fill(background_color)

    # Dibujar un triángulo
    triángulo.dibujar(screen)

    # Actualizar la pantalla
    pygame.display.update()

    # Limitar los FPS a 60
    pygame.time.Clock().tick(60)

# Cerrar Pygame
pygame.quit()