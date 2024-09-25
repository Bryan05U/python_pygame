import pygame

class Rectángulo():
    def __init__(self, x, y, ancho, alto):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.velocidad = 1 # Velocidad de movimiento en pixeles

    # Movimiento del rectángulo según las teclas presionadas
    def mover(self, teclas_3):
        if teclas_3[pygame.K_j]:
            self.x -= self.velocidad
        if teclas_3[pygame.K_l]:
            self.x += self.velocidad
        if teclas_3[pygame.K_i]:
            self.y -= self.velocidad
        if teclas_3[pygame.K_k]:
            self.y += self.velocidad