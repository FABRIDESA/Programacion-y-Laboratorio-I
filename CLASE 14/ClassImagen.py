import pygame

class Imagen:
    #primero el init, el constructor
    def __init__(self,origen,tamaño,colores):
        self.superficie = pygame.Surface(tamaño)
        self.color = colores[0]
        self.color_colision = colores[1]
        self.superficie.fill(self.color)
        self.rectangulo = self.superficie.get_rect()
        self.rectangulo.center = origen

    def mover(self,sentido:str, desplazamiento:int, pantalla:pygame.Surface):
        if sentido == "Vertical":
            self.rectangulo.y += desplazamiento
            if self.rectangulo.top > pantalla.get_rect().height:
                self.rectangulo.bottom = 0
        else:
            self.rectangulo.x += desplazamiento
            if self.rectangulo.left > pantalla.get_rect().width:
                self.rectangulo.right = 0

    def detectar_colision(self,otra_imagen: "Imagen"):
        if self.rectangulo.colliderect(otra_imagen.rectangulo):
            self.superficie.fill(self.color_colision)
            otra_imagen.superficie.fill(otra_imagen.color_colision)
        else:
            self.superficie.fill(self.color)
            otra_imagen.superficie.fill(otra_imagen.color)
