import pygame
from círculo_1 import Círculo_1
from círculo_2 import Círculo_2

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
screen = pygame.display.set_mode((800, 600)) # Tamaño de la ventana
pygame.display.set_caption("Figures Movement") # Título de la ventana

# Color de fondo
background_color = (0, 0 ,0)

círculo_1 = Círculo_1(600, 300)
círculo_2 = Círculo_2(200, 300)

# Bucle principal del juego
running = True
while running:
    # Evento para cerrar la ventana
    for event in pygame.event.get(): # Lista de Eventos
        if event.type == pygame.QUIT:
            running = False

    # Estado de las teclas
    teclas = pygame.key.get_pressed()
    teclas_2 = pygame.key.get_pressed()

    # Mover el círculo 1
    círculo_1.mover(teclas)

    # Pintar el fondo
    screen.fill(background_color)

    # Dibujar los círculos 1 y 2
    pygame.draw.circle(screen, (255, 0, 0), (círculo_1.x, círculo_1.y), 50)
    pygame.draw.circle(screen, (0, 0, 255), (círculo_2.x, círculo_2.y), 50)

    # Mover el círculo 2
    círculo_2.mover(teclas_2)

    # Actualizar la pantalla
    pygame.display.update()

# Cerrar Pygame
pygame.quit()