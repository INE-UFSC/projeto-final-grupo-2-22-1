import pygame
import json
from game.map_objects.block import Block
from game.map_objects.door import Door
from game.maps.map1 import *

class Level:
    def __init__(self,
        #blocks: list[Block],
        #doors: list[Door],
        #enemies: list[Enemy],
        #player: Player,
        path: str
    ):
        self.__path = path
        #self.__blocks= blocks
        #self.__doors: doors
        self.__win: False      #Essas condicoes o system vai analisar e decidir oq fazer (Puxar algum menu, mudar o level... etc)
        self.__defeat: False

    # Grupos de sprites. (uma das funcionalidades dos grupos de sprite são de detectar colisões entre eles.)
        self.display_surface = pygame.display.get_surface()
        self.object_group = pygame.sprite.Group()
        self.enemyGroup = pygame.sprite.Group()
        self.blockGroup = pygame.sprite.Group()
        self.doorGroup = pygame.sprite.Group()
        self.create_map()

    #carrega o codigo do mapa.json
    def get_map(self):
        file = open(self.__path, 'r')
        return json.load(file)["map"]


    #IMPLEMENTAR O DRAW_MAP
    def create_map(self):
        map_array = self.get_map()

        for row_index,row in enumerate(map_array):
            for col_index, col in enumerate(row):
                x = col_index * 32
                y = row_index * 32
                if col == 'X':
                    Block((x,y),[self.blockGroup])
                if col == 'D':
                    Door((x,y),[self.doorGroup])

    def run(self):
        self.blockGroup.draw(self.display_surface)
        self.doorGroup.draw(self.display_surface)
        

    