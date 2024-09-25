import pygame

class Círculo():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidad = 1 # Velocidad de movimiento en pixeles

    # Movimiento del círculo según las teclas presionadas
    def mover(self, teclas_2):
        if teclas_2[pygame.K_a]:
            self.x -= self.velocidad
        if teclas_2[pygame.K_d]:
            self.x += self.velocidad
        if teclas_2[pygame.K_w]:
            self.y -= self.velocidad
        if teclas_2[pygame.K_s]:
            self.y += self.velocidad