import pygame
import random

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Clase para los desechos
class Desecho(pygame.sprite.Sprite):
    def __init__(self, tipo, contenedor_correcto, puntos, penalizacion):
        super().__init__()
        self.tipo = tipo
        self.contenedor_correcto = contenedor_correcto
        self.puntos = puntos
        self.penalicacion = penalizacion
        self.image = pygame.Surface([50, 50])  # Tamaño del desecho
        self.image.fill(VERDE)  # Color del desecho (puedes cambiarlo)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = 0
        self.velocidad = random.randint(1, 3)

    def update(self):
        self.rect.y += self.velocidad
        if self.rect.y > ALTO:
            self.rect.y = 0
            self.rect.x = random.randrange(ANCHO - self.rect.width)

# Función principal del juego
def main():
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    pygame.display.set_caption("Juego de Ecología")

    reloj = pygame.time.Clock()

    # Crear superficies para las dos secciones
    seccion_superior = pygame.Surface((ANCHO, ALTO // 2))
    seccion_inferior = pygame.Surface((ANCHO, ALTO // 2))
    seccion_superior.fill(BLANCO)
    seccion_inferior.fill(AZUL)

    todos_los_sprites = pygame.sprite.Group()

    # Crear desechos
    tipos_de_desechos = [("Plástico", "Reciclaje", 10, 5),
                         ("Vidrio", "Reciclaje", 15, 5),
                         ("Papel", "Reciclaje", 8, 3),
                         ("Orgánico", "Compostaje", 12, 6)]

    for i in range(3):  # Inicialmente solo 3 tipos de desechos
        tipo, contenedor_correcto, puntos, penalizacion = random.choice(tipos_de_desechos)
        desecho = Desecho(tipo, contenedor_correcto, puntos, penalizacion)
        todos_los_sprites.add(desecho)

    puntuacion = 0

    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

        # Actualizar
        todos_los_sprites.update()
        }
}