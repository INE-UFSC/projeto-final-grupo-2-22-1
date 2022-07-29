import pygame
from game.level import Level
from game.entity.player import Player  #Player sera instanciado aqui, assim
from game.entity.enemy import Enemy

class Control():
    def __init__(self):

        pygame.init()
        pygame.display.set_caption("Jogo do grupo 2")

        #tryexception OS
        self.__maps = ['versao_final/game/maps/map1.json']    #Aqui os caminhos para os arquivos csv
        self.__current_map = 0

        self.clock = pygame.time.Clock()
        self.FPS = 120
        self.display = pygame.display.set_mode([1024, 768])

        self.level = Level(self.__maps[self.__current_map])
    def start(self):
        gameLoop = True
        while gameLoop:
            self.clock.tick(self.FPS)  
            self.level.run()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameLoop = False

            pygame.display.update()


    def collision(self,block):
        pass

    
    @property
    def maps(self):
        return self.__maps

        
