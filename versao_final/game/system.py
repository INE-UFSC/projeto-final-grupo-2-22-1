import pygame
from game.level import Level
from game.entity.player import Player  #Player sera instanciado aqui, assim
from game.entity.enemy import Enemy

class Control():
    def __init__(self):

        pygame.init()
        pygame.display.set_caption("Jogo do grupo 2")

        self.__maps = ['maps/map1.csv']    #Aqui os caminhos para os arquivos csv

        self.clock = pygame.time.Clock()
        self.FPS = 120
        self.display = pygame.display.set_mode([1024, 768])

        # Grupos de sprites. (uma das funcionalidades dos grupos de sprite são de detectar colisões entre eles.)
        self.object_group = pygame.sprite.Group()
        self.enemyGroup = pygame.sprite.Group()
        self.blockGroup = pygame.sprite.Group()
        self.portaGroup = pygame.sprite.Group()
        
    def start(self):
        gameLoop = True
        while gameLoop:
            self.clock.tick(self.FPS)  

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameLoop = False

            pygame.display.update()
    
    
    @property
    def maps(self):
        return self.__maps

    def collision(self,block):
        pass
        
