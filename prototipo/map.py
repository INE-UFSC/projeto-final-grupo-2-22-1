import pygame

#map1 32x24, onde '.' será um espaço vazio e 'X' será um obstaculo
#mapa do jogo dever ser divisivel pelo tamanho da janela.
#1024 / 32 = 32
#768 / 24 = 32

class Block(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("prototipo/arquivos/bloco.png")
        self.rect = self.image.get_rect()

class Porta(pygame.sprite.Sprite):
    def __init__(self, image, *groups):
        super().__init__(image, *groups)
        self.image = pygame.image.load("prototipo/arquivos/porta1.png")
        self.rect = self.image.get_rect()        

    

map1 = [
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'X..............................X',
    'X..............................X',
    'X..............................X',
    'X...XXXXXXXX........XXXXXXXX...X',
    'X...X......................X...X',
    'X...X......................X...X',
    'X...X......................X...X',
    'X...X......................X...X',
    'X...X......................X...X',
    'X...X.......XXXXX..........X...P',
    'X...............X..............P',
    'X...............X..............P',
    'X...............X..............P',
    'XXXXX...........XXXXXXXXXXXX...X',
    'X...X......................X...X',
    'X...X......................X...X',
    'X...X......................X...X',
    'X...X......................X...X',
    'X...X......................X...X',
    '....XXXXXXXXXX.......XXXXXXX...X',
    '...............................X',
    '...............................X',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

map2 = [
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'X..............................X',
    'X..............................X',
    'X....XXX.XXX.XXX.XXX.XXX.......X',
    'X.....X..X....X...X..X.........X',
    'X.....X..XXX.XXX..X..XXX.......X',
    'X..............................X',
    'X..............................X',
    'X..............................X',
    'X..............................X',
    'X...............................',
    'X...............................',
    'X...............................',
    'X...............................',
    'X..............................X',
    'X..............................X',
    'X..............................X',
    'X..............................X',
    'X..............................X',
    'X..............................X',
    'P..............................X',
    'P..............................X',
    'P..............................X',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']    















