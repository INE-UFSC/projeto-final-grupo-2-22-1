import pygame
from game.entity.character import Character

class Player(Character):
    def __init__(self, vida, dano, *groups):
        super().__init__(vida, dano ,*groups)
        try:
            self.image = pygame.image.load("versao_final/game/image/Player/player.png")  # carregando a imagem
        except FileNotFoundError:
            self.image = pygame.image.load("versao_final\game\image\Player\player.png") 

        self.rect = pygame.Rect(40, 680, 20, 50)  # retangulo do player (posição x, y, altura, largura)
        self.__velocidadeX = 0
        self.__velocidadeY = 0
        self.__intencao_pos = list(self.rect.center)
        


    def update(self, *args): 
        self.intencao_pos[0] += self.velocidadeX
        self.intencao_pos[1] += self.velocidadeY
        self.rect.center = self.intencao_pos

    def mover_direita(self):
        self.velocidadeX = 3
        self.velocidadeY = 0
                   
    def mover_esquerda(self):
        self.velocidadeX = -3
        self.velocidadeY = 0           

    def mover_cima(self):
        self.velocidadeY = -3
        self.velocidadeX = 0
            
    def mover_baixo(self):
        self.velocidadeY = 3
        self.velocidadeX = 0

    def teste_colisao(self, grupo):
        if pygame.sprite.spritecollide(self, grupo, False):
            return True
        else:
            return False 




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
    