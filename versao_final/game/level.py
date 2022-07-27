import pygame
import csv

class Level:
    def __init__(self,
        blocks: list[Block],
        doors: list[Door],
        enemies: list[Enemy],
        player: Player,
        path: str
    ):
        self.__path = path
        self.__blocks= blocks
        self.__doors: doors
        self.__win: False               #Essas condicoes o system vai analisar e decidir oq fazer (Puxar algum menu, mudar o level... etc)
        self.__defeat: False

    #carrega o codigo do mapa.csv
    def get_map(self):
        with open(self.__path,'r') as current_map:
            csv.reader(current_map)
            map_array = list(current_map)

            for i in range(0, len(map_array)):
                map_array[i] = map_array[i].split(',')
            
        return map_array

    #IMPLEMENTAR O DRAW_MAP
    '''
    def draw_map(self):
        map_array=self.get_map()
        for line in map_array:
            for x in line:
                if x == 'X':
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
    