import pygame

class Disparo(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("arquivos/tiro.png")
        self.rect = self.image.get_rect()
        self.speed = 10

    def update(self,*args):
         self.rect.x += self.speed
         if self.rect.left > 1100:
            self.kill()
