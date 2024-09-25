import pygame
import math

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
screen = pygame.display.set_mode((800, 600)) # Tamaño de la ventana
pygame.display.set_caption("Collision of Circles") # Título de la ventana

# Colores de fondo
black_color = (0, 0, 0)
white_color = (255, 255, 255)

# Colores de los círculos
blue_color = (0, 0, 255)
red_color = (255, 0, 0)

# Clase para crear el círculo y añadiendo sus atributos
class Círculo:
    def __init__(self, x, y, radio, color):
        self.x = x
        self.y = y
        self.radio = radio
        self.color = color
        self.velocidad = 5 # Velocidad de movimiento en pixeles
    def mover(self, dx, dy):
        self.x += dx * self.velocidad
        self.y += dy * self.velocidad

    def dibujar(self, superficie):
        pygame.draw.circle(superficie, self.color, (int(self.x), int(self.y)), self.radio)

    def colisión(self, otro):
        distancia = math.sqrt((self.x - otro.x) ** 2 + (self.y - otro.y) ** 2)
        return distancia < (self.radio + otro.radio)

# Creando los círculos
círculo_1 = Círculo(200, 300, 60, blue_color)
círculo_2 = Círculo(600, 300, 60, red_color)

# Bucle principal del juego
running = True
while running:
    # Evento para cerrar la ventana
    for event in pygame.event.get(): # Lista de Eventos
        if event.type == pygame.QUIT:
            running = False

    # Estado de las teclas
    teclas = pygame.key.get_pressed()
    dx1, dy1 = 0, 0
    dx2, dy2 = 0, 0

    # Movimiento del primer círculo según las teclas presionadas
    if teclas[pygame.K_LEFT]: dx1 = -1
    if teclas[pygame.K_RIGHT]: dx1 = 1
    if teclas[pygame.K_UP]: dy1 = -1
    if teclas[pygame.K_DOWN]: dy1 = 1

    # Movimiento del segundo círculo según las teclas presionadas
    if teclas[pygame.K_a]: dx2 = -1
    if teclas[pygame.K_d]: dx2 = 1
    if teclas[pygame.K_w]: dy2 = -1
    if teclas[pygame.K_s]: dy2 = 1

    # Mover los círculos
    círculo_1.mover(dx1, dy1)
    círculo_2.mover(dx2, dy2)

    if círculo_1.colisión(círculo_2):
       círculo_1.color = (255, 0, 0) # Cambia el color del círculo azul a rojo
       círculo_2.color = (0, 0, 255) # Cambia el color del círculo rojo a azul
    else:
       círculo_1.color = blue_color # Vuelve al color azul
       círculo_2.color = red_color # Vuelve al color rojo

    # Actualizar la pantalla
    pygame.display.update()

    # Dibujar
    screen.fill(black_color)
    #screen.fill(white_color)
    círculo_1.dibujar(screen)
    círculo_2.dibujar(screen)
    pygame.display.flip()

    # Limita los FPS a 60
    pygame.time.Clock().tick(60)

# Cerrar Pygame
pygame.quit()