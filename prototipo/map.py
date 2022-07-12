import pygame
from configs import *
#from main import GREEN

#map1 32x24, onde '.' será um espaço vazio e 'X' será um obstaculo
#mapa do jogo dever ser divisivel pelo tamanho da janela.
#1024 / 32 = 32
#768 / 24 = 32

class Block(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load("prototipo/arquivos/bloco.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)















