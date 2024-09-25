import pygame
from triangle import Triángulo
from circle import Círculo
from rect import Rectángulo

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
screen = pygame.display.set_mode((800, 600)) # Tamaño de la ventana
pygame.display.set_caption("Movement of Figures") # Título de la ventana

#pygame.display.set_icon():
#pygame.display.iconfy():
#pygame.set_gamma():

# Color de fondo
background_color = (0, 0 ,0)

triángulo = Triángulo(400, 150)
círculo = Círculo(300, 100)
rectángulo = Rectángulo(200, 300, 100, 50)

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
    teclas_3 = pygame.key.get_pressed()

    # Mover el triángulo
    triángulo.mover(teclas)

    # Pintar el fondo
    screen.fill(background_color)

    # Dibujar un triángulo
    triángulo.dibujar(screen)

    # Dibujar otras figuras geométricas
    pygame.draw.circle(screen, (255, 0, 0), (círculo.x, círculo.y), 50)
    pygame.draw.rect(screen, (0, 255, 0), (rectángulo.x, rectángulo.y, rectángulo.ancho, rectángulo.alto))
    #pygame.draw.line(screen, (0, 0, 255), (100, 500), (700, 500), 5)

    # Mover el círculo
    círculo.mover(teclas_2)

    # Mover el rectángulo
    rectángulo.mover(teclas_3)

    # Actualizar la pantalla
    pygame.display.update()

# Cerrar Pygame
pygame.quit()