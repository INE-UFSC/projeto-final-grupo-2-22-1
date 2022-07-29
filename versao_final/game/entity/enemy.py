import pygame
import math
from game.entity.character import Character

class Enemy(Character):
    def __init__(self, vida, dano,  *groups):
        super().__init__(vida, dano, *groups)
        self.image = pygame.image.load("image/Enemy/enemy.png")
        self.rect = self.image.get_rect()
        self.timer = 0

    def update(self,*args):
        self.timer += 0.003
        self.rect.x = 512 + math.sin(self.timer) * 320