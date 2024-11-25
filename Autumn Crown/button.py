class Botón():
    def __init__(self, imagen, pos, entrada_texto, font, color_base, color_flotante):
        self.imagen = imagen
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.color_base, self.color_flotante = color_base, color_flotante
        self.entrada_texto = entrada_texto
        self.text = self.font.render(self.entrada_texto, True, self.color_base)
        if self.imagen is None:
            self.imagen = self.text
        self.rect = self.imagen.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def actualizar(self, pantalla):
        if self.imagen is not None:
            pantalla.blit(self.imagen, self.rect)
        pantalla.blit(self.text, self.text_rect)

    def revisarEntrada(self, posición):
        if posición[0] in range(self.rect.left, self.rect.right):
            return True
        return False
    
    def cambiarColor(self, posición):
        if posición[0] in range(self.rect.left, self.rect.right) and posición[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.entrada_texto, True, self.color_flotante)
        else:
            self.text = self.font.render(self.entrada_texto, True, self.color_base)