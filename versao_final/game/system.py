import pygame
from level import Level
from entity.player import Player  #Player sera instanciado aqui, assim

class Control():

    pygame.init()
    pygame.display.set_caption("Jogo do grupo 2")

    def __init__(self):
        self.__maps = ['maps/map1.csv']    #Aqui os caminhos para os arquivos csv

        self.clock = pygame.time.Clock()
        self.FPS = 120
        self.display = pygame.display.set_mode([1024, 768])
        
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