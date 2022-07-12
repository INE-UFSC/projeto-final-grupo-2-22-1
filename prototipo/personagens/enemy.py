import pygame
from personagens.personagem import Personagem
from equipamentos import *
import math

class Enemy(Personagem):
    def __init__(self, vida, dano, pos, groups):
        super().__init__(vida, dano, pos, groups)

        self.image = pygame.image.load("prototipo/arquivos/enemy.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.timer = 0


    def update(self,*args):
    # Comandos
        self.timer += 0.003
        self.rect.x = 512 + math.sin(self.timer) * 320

