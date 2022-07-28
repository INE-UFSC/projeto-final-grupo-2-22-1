import pygame
import csv
from game.map_objects.block import Block
from game.map_objects.door import Door

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
        self.__win: False               #Essas condicoes o system vai analisar e decidir oq fazer (Puxar algum menu, mudar o level... etc)
        self.__defeat: False
        self.create_map()
    #carrega o codigo do mapa.csv
    def get_map(self):
        with open(self.__path,'r') as current_map:
            csv.reader(current_map)
            map_array = list(current_map)

            for i in range(0, len(map_array)):
                map_array[i] = map_array[i].split(',')
            
        return map_array

    #IMPLEMENTAR O DRAW_MAP
    def create_map(self):
        map_array = self.get_map()
        for row_index,row in enumerate(map_array):
            for col_index, col in enumerate(row):
                x = col_index * 32
                y = row_index * 32
                if col == 'X':
                    Block((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'P':
                    Door((x,y),[self.visible_sprites])
''' 
    def draw_map(self):
        map_array=self.get_map()
        for line in range(len(map_array)):
            for x in line:
                if x == "X":
                    block = Block(self.blockGroup) #--nao sei  #mudar nome rect1
                    block.rect.x = x * 32 #-- nao sei
                    block.rect.y = y * 32 #-- nao sei
                if x == "P":
                    door = Door(self.portaGroup)
                    door.rect.x = x * 32
                    door.rect.y = y * 32
    
'''

'''
    def 


        """Uma fase do jogo"""

    @classmethod
    def from_file(cls, file: str) -> "Level":
        """Carregar uma fase de um arquivo"""

    @classmethod
    def from_list(cls, level: list[str]) -> "Level":
        """Carregar uma fase de uma lista"""

    def __init__(
        self,
        blocks: list[Block],
        doors: list[Door],
        enemies: list[Enemy],
        player: Player,
    ):
        self.__blocks = Group(*blocks)
        self.__doors = Group(*doors)
        self.__enemies = Group(*enemies)
        self.__player = player

        self.finished = False
        self.win
        self.lose

    def update(self):
        """Atualiza as entidades"""
        for enemy in spritecollide(self.__player, self.__enemies):
            enemy.damage(self.__player)

    def draw(self, screen: ...):
        """Renderiza a fase na tela"""

'''
    