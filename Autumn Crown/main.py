import pygame
import sys
from button import Botón

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
PANTALLA = pygame.display.set_mode((800, 600)) # Tamaño de la ventana
pygame.display.set_caption("Autumn Crown") # Título de la ventana

# Imagen de fondo
IMAGEN_FONDO = pygame.image.load('Autumn Crown/image/background.jpg')

###########################################

# Fuente de letra
def obtener_fuente(tamaño):
    return pygame.font.Font('Autumn Crown/assets/OldLondon.ttf', tamaño)

# Limita los FPS a 60
def limitar_fps():
    pygame.time.Clock().tick(60)

def iniciar_juego():
    while True:
        INICIAR_MOUSE_POS = pygame.mouse.get_pos()

        PANTALLA.fill("Black")

        INICIAR_TEXT = obtener_fuente(45).render("Selecciona un personaje", True, "White")
        INICIAR_RECT = INICIAR_TEXT.get_rect(center=(400, 100))
        PANTALLA.blit(INICIAR_TEXT, INICIAR_RECT)

        INICIAR_BACK = Botón(imagen=None,pos=(400, 460),
                          entrada_texto="Atrás", font=obtener_fuente(75), color_base="White", color_flotante="Green")
        
        INICIAR_BACK.cambiarColor(INICIAR_MOUSE_POS)
        INICIAR_BACK.actualizar(PANTALLA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INICIAR_BACK.revisarEntrada(INICIAR_MOUSE_POS):
                    menú_principal()

            # Actualizar pantalla
            pygame.display.update()

def puntuaciones():
    while True:
        PUNTUACIONES_MOUSE_POS = pygame.mouse.get_pos()

        PANTALLA.fill("Black")
        
        PUNTUACIONES_TEXT = obtener_fuente(45).render("Puntuaciones", True, "Black")
        PUNTUACIONES_RECT = PUNTUACIONES_TEXT.get_rect(center=(400, 260))
        PANTALLA.blit(PUNTUACIONES_TEXT, PUNTUACIONES_RECT)
        
        PUNTUACIONES_BACK = Botón(imagen=None, pos=(400, 460),
                              entrada_texto="Atrás", font=obtener_fuente(75), color_base="Black", color_flotante="Green")
        
        PUNTUACIONES_BACK.cambiarColor(PUNTUACIONES_MOUSE_POS) 
        PUNTUACIONES_BACK.actualizar(PANTALLA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PUNTUACIONES_TEXT.revisarEntrada(PUNTUACIONES_MOUSE_POS):
                    menú_principal()

        # Actualizar pantalla
        pygame.display.update()

def opciones():
    while True:
        OPCIONES_MOUSE_POS = pygame.mouse.get_pos()

        PANTALLA.fill("Black")
        
        OPCIONES_TEXT = obtener_fuente(45).render("Opciones", True, "Black")
        OPCIONES_RECT = OPCIONES_TEXT.get_rect(center=(640, 260))
        PANTALLA.blit(OPCIONES_TEXT, OPCIONES_RECT)
        
        OPCIONES_BACK = Botón(imagen=None, pos=(400, 460),
                              entrada_texto="Atrás", font=obtener_fuente(75), color_base="Black", color_flotante="Green")
        
        OPCIONES_BACK.cambiarColor(OPCIONES_MOUSE_POS) 
        OPCIONES_BACK.actualizar(PANTALLA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPCIONES_TEXT.revisarEntrada(OPCIONES_MOUSE_POS):
                    menú_principal()

        # Actualizar pantalla
        pygame.display.update()

def menú_principal():
    while True:
        PANTALLA.blit(IMAGEN_FONDO, (0, 0))

        MENÚ_MOUSE_POS = pygame.mouse.get_pos()

        MENÚ_TEXT = obtener_fuente(80).render("Autumn Crown", True, "#b68f40")
        MENÚ_RECT = MENÚ_TEXT.get_rect(center=(400, 100))

        INICIAR_BUTTON = Botón(imagen=pygame.image.load('Autumn Crown/assets/Iniciar Juego Rect.png'), pos=(400, 250),
                               entrada_texto="Iniciar Juego", font=obtener_fuente(40), color_base="White", color_flotante="Green")

        PUNTUACIONES_BUTTON = Botón(imagen=pygame.image.load('Autumn Crown/assets/Puntuaciones Rect.png'), pos=(400, 320),
                               entrada_texto="Puntuaciones", font=obtener_fuente(40), color_base="White", color_flotante="Green")

        OPCIONES_BUTTON = Botón(imagen=pygame.image.load('Autumn Crown/assets/Opciones Rect.png'), pos=(400, 390),
                               entrada_texto="Opciones", font=obtener_fuente(40), color_base="White", color_flotante="Green")

        SALIR_BUTTON = Botón(imagen=pygame.image.load('Autumn Crown/assets/Salir del Juego Rect.png'), pos=(400, 460),
                               entrada_texto="Salir del Juego", font=obtener_fuente(40), color_base="White", color_flotante="Green")


        PANTALLA.blit(MENÚ_TEXT, MENÚ_RECT)
        
        for button in [INICIAR_BUTTON, PUNTUACIONES_BUTTON, OPCIONES_BUTTON, SALIR_BUTTON]:
            button.cambiarColor(MENÚ_MOUSE_POS)
            button.actualizar(PANTALLA)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INICIAR_BUTTON.revisarEntrada(MENÚ_MOUSE_POS):
                    iniciar_juego()
                if PUNTUACIONES_BUTTON.revisarEntrada(MENÚ_MOUSE_POS):
                    puntuaciones()
                if OPCIONES_BUTTON.revisarEntrada(MENÚ_MOUSE_POS):
                    opciones()
                if SALIR_BUTTON.revisarEntrada(MENÚ_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        # Actualizar pantalla
        pygame.display.update()

menú_principal()