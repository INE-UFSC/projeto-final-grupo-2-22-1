import pygame
import math



class Enemy(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("arquivos/enemy.png")
        self.image = pygame.transform.scale(self.image, [20, 50])
        self.rect = self.image.get_rect()

        self.timer = 0



    def update(self,*args):
    # Comandos
        self.timer += 0.0003
        self.rect.x = 512 + math.sin(self.timer) * 350
