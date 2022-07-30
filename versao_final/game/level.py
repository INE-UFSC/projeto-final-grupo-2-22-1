import pygame
import json
from game.map_objects.block import Block
from game.map_objects.door import Door
from game.entity.player import Player
from game.entity.enemy import Enemy
class Level:
    def __init__(self,

        #enemies: list[Enemy],
        player: Player, 
        path: str,
        pygame_groups: list,
       
    ):
        self.__path = path
        self.__player = Player
        self.__next_map = False
        self.__next_map = False      #Essas condicoes o system vai analisar e decidir oq fazer (Puxar algum menu, mudar o level... etc)
        self.__defeat = False
       

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
                if col == 'P':
                    self.__player.rect = pygame.Rect(x, y, 20, 50)
                if col == 'E':
                    Enemy((x,y), [self.__enemyGroup])
    def run(self):
        self.__blockGroup.draw(self.__display_surface)
        self.__doorGroup.draw(self.__display_surface)
        self.__object_group.draw(self.__display_surface)
        self.__enemyGroup.draw(self.__display_surface)
    
    @property
    def next_map(self):
        return  self.__next_map
    @next_map.setter
    def next_map(self, boolean):
        self.__next_map = boolean
    
    @property
    def defeat(self):
        return self.__defeat
    @defeat.setter
    def defeat(self, boolean):
        self.__defeat = boolean
    


    