import pygame
import math
from equipamentos import *
from personagens.personagem import Personagem

class Player(Personagem):
    def __init__(self,vida ,dano ,arma, item: Item, *groups):
        super().__init__(vida,dano,arma, *groups)
        self.__item = Item
        self.image = pygame.image.load("prototipo/arquivos/careca.png")  # carregando a imagem
        self.rect = pygame.Rect(40, 680, 20, 50)  # retangulo do player (posição x, y, altura, largura)
        self.velocidadeX = 0
        self.velocidadeY = 0
        self.intencao_pos = list(self.rect.center)

    def update(self, *args):
        self.rect.center = self.intencao_pos
        self.intencao_pos[0] += self.velocidadeX
        self.intencao_pos[1] += self.velocidadeY

    def mover_direita(self):
        self.velocidadeX = 2
        self.velocidadeY = 0
                   
    def mover_esquerda(self):
        self.velocidadeX = -2
        self.velocidadeY = 0           

    def mover_cima(self):
        self.velocidadeY = -2
        self.velocidadeX = 0
            
    def mover_baixo(self):
        self.velocidadeY = 2
        self.velocidadeX = 0

    def teste_colisao(self, grupo):
        if pygame.sprite.spritecollide(self, grupo, False):
            return True
        else:
            return  False 
