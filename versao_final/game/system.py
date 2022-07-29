import pygame
from game.level import Level
from game.entity.player import Player  #Player sera instanciado aqui, assim
from game.entity.enemy import Enemy

class Control():
    def __init__(self):

        pygame.init()
        pygame.display.set_caption("Jogo do grupo 2")

        try:
            self.__maps = ['versao_final/game/maps/map1.json']    #Aqui os caminhos para os arquivos csv
        except FileNotFoundError:
            self.__maps = ['versao_final\game\maps\map1.json']


        self.__current_map = 0

        self.__clock = pygame.time.Clock()
        self.__FPS = 120
        self.display = pygame.display.set_mode([1024, 768])

        self.__object_group = pygame.sprite.Group()
        self.__enemyGroup = pygame.sprite.Group()
        self.__blockGroup = pygame.sprite.Group()
        self.__doorGroup = pygame.sprite.Group()

        python_groups = [self.__object_group, self.__enemyGroup, self.__blockGroup, self.__doorGroup]


        self.__level = Level(self.__maps[self.__current_map], python_groups)
        self.__player = Player()



    def start(self):
        gameLoop = True
        while gameLoop:
            self.__clock.tick(self.__FPS)  
            self.__level.run()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameLoop = False

            pygame.display.update()
 
    @property
    def maps(self):
        return self.__maps

        
