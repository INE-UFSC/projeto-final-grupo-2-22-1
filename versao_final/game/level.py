import pygame
import json
from game.map_objects.block import Block
from game.map_objects.door import Door
from game.entity.player import Player

class Level:
    def __init__(self,

        #enemies: list[Enemy],
        player: Player, 
        path: str,
        pygame_groups: list
    ):
        self.__path = path
        self.__player = Player
        self.__win: False      #Essas condicoes o system vai analisar e decidir oq fazer (Puxar algum menu, mudar o level... etc)
        self.__defeat: False

    # Grupos de sprites. (uma das funcionalidades dos grupos de sprite são de detectar colisões entre eles.)
        self.__display_surface = pygame.display.get_surface()
        self.__object_group = pygame_groups[0]
        self.__enemyGroup = pygame_groups[1]
        self.__blockGroup = pygame_groups[2]
        self.__doorGroup = pygame_groups[3]
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
                    Block((x,y),[self.__blockGroup])
                if col == 'D':
                    Door((x,y),[self.__doorGroup])

    def run(self):
        self.__blockGroup.draw(self.__display_surface)
        self.__doorGroup.draw(self.__display_surface)
    

    def collision_detector(self):
        pass

    