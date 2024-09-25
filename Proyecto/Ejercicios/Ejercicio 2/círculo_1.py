import pygame

class Círculo_1():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidad = 1 # Velocidad de movimiento en pixeles

    # Movimiento del círculo según las teclas presionadas
    def mover(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.x -= self.velocidad
        if teclas[pygame.K_RIGHT]:
            self.x += self.velocidad
        if teclas[pygame.K_UP]:
            self.y -= self.velocidad
        if teclas[pygame.K_DOWN]:
            self.y += self.velocidad