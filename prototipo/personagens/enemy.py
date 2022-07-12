import pygame
import math
from equipamentos import *
from personagens.personagem import Personagem

class Enemy(Personagem):
    def __init__(self, vida, dano, arma, imagem, *groups):
        super().__init__(vida, dano, arma, *groups)

        self.image = imagem

        self.image = pygame.transform.scale(self.image, [20, 50])
        self.rect = self.image.get_rect()
        self.timer = 0


    def update(self,*args):
    # Comandos
        self.timer += 0.003
        self.rect.x = 512 + math.sin(self.timer) * 320