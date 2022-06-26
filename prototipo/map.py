import pygame
#from main import GREEN

#map1 32x24, onde '.' será um espaço vazio e 'X' será um obstaculo
#mapa do jogo dever ser divisivel pelo tamanho da janela.
#1024 / 32 = 32
#768 / 24 = 32

class Block(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("prototipo/arquivos/bloco.png")
        self.rect = self.image.get_rect()  


map1 = [
    'XXXX........................XXXX',
    'X..............................X',
    'X..............................X',
    'X..............................X',
    'X...XXXXXXXX........XXXXXXXX...X',
    'X...X......................X...X',
    'X...X......................X...X',
    'X...X......................X...X',
    'X...X......................X...X',
    'X...X......................X...X',
    'X...X.......XXXXX..........X...X',
    'X...............X..............X',
    'X...............X..............X',
    'X...............X..............X',
    'XXXXX...........XXXXXXXXXXXX...X',
    'X...X......................X...X',
    'X...X......................X...X',
    'X...X......................X...X',
    'X...X......................X...X',
    'X...X......................X...X',
    'X...XXXXXXXXXX.......XXXXXXX...X',
    'X....................X.........X',
    'X..............................X',
    'XXXX........................XXXX']
















