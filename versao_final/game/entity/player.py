import pygame
from game.entity.character import Character

class Player(Character):
    def __init__(self, vida, dano, *groups):
        super().__init__(vida, dano ,*groups)
        self.image = pygame.image.load("versao_final/game/image/Player/player.png")  # carregando a imagem
        self.rect = pygame.Rect(40, 680, 20, 50)  # retangulo do player (posição x, y, altura, largura)
        self.__velocidadeX = 0
        self.__velocidadeY = 0
        self.__intencao_pos = list(self.rect.center)
        


    def update(self, *args):
 
        self.__intencao_pos[0] += self.__velocidadeX
        self.__intencao_pos[1] += self.__velocidadeY
        self.rect.center = self.__intencao_pos

    def mover_direita(self):
        self.__velocidadeX = 2
        self.__velocidadeY = 0
                   
    def mover_esquerda(self):
        self.__velocidadeX = -2
        self.__velocidadeY = 0           

    def mover_cima(self):
        self.__velocidadeY = -2
        self.__velocidadeX = 0
            
    def mover_baixo(self):
        self.__velocidadeY = 2
        self.__velocidadeX = 0




    @property
    def velocidadeX(self):
        return self.__velocidadeX
    @velocidadeX.setter
    def velocidadeX(self,velX):
        self.__velocidadeX = velX

    @property
    def velocidadeY(self):
        return self.__velocidadeY
    @velocidadeY.setter
    def velocidadeY(self, velY):
        self.__velocidadeY = velY

    @property
    def intencao_pos(self):
        return self.__intencao_pos
    @intencao_pos.setter
    def intencao_pos(self, intencao_pos):
        self.__intencao_pos = intencao_pos
    