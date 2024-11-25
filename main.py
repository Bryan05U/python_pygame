import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
screen = pygame.display.set_mode((800, 600)) # Tamaño de la ventana
pygame.display.set_caption("Autumn Crown") # Título de la ventana

# Definir fuente de letra
font = pygame.font.SysFont("Times New Roman", 70)
font_2 = pygame.font.SysFont("Georgia", 30)

# Definir colores
TEXT_COL = (255, 255, 255)

def dibujar_título(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def dibujar_texto(text, font, text_col, x, y):
    img = font_2.render(text, True, text_col)
    screen.blit(img, (x, y))

# Icono del juego
icon = pygame.image.load('Autumn Crown/icon/icon.ico')
pygame.display.set_icon(icon)
#pygame.display.iconfy():
#pygame.set_gamma():

# Imagen de fondo
image = pygame.image.load('Autumn Crown/image/background.jpg')

# Color de fondo
background_color = (255, 255, 255)

# Bucle principal del juego
running = True
while running:
    # Evento para cerrar la ventana
    for event in pygame.event.get(): # Lista de Eventos
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

    # Pintar el fondo
    screen.fill(background_color)

    # Dibujar la imagen de fondo
    screen.blit(image, (-50,-50))
    
    # Dibujar textos
    dibujar_título("Autumn Crown", font, TEXT_COL, 180, 80)
    dibujar_texto("• Iniciar juego", font, TEXT_COL, 210, 245)
    dibujar_texto("• Puntuaciones", font, TEXT_COL, 210, 300)
    dibujar_texto("• Opciones", font, TEXT_COL, 210, 350)
    dibujar_texto("• Salir del juego", font, TEXT_COL, 210, 400)

    # Limita los FPS a 60
    pygame.time.Clock().tick(60)

    # Actualizar la pantalla
    pygame.display.update()

# Cerrar Pygame
pygame.quit()