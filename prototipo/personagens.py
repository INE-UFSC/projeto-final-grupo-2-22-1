import pygame
import math
from abc import ABC, abstractmethod

#classes armas e itens, colocar em outro lugar.
class Arma:
    pass

class Item:
    pass


class Personagem(ABC, pygame.sprite.Sprite):
    def __init__(self, vida, dano, arma: Arma, *groups):
        super().__init__(*groups)
        self.__vida = vida
        self.__dano = dano
        self.__arma = arma


    @abstractmethod
    def update(self):
        pass




class Player(Personagem):
    def __init__(self,vida ,dano ,arma, item: Item,  *groups):
        super().__init__(vida,dano,arma, *groups)
        self.__item = Item

        #Deixar o seguinte como atributo de persdongaens
        self.image = pygame.image.load("arquivos/careca.png")  # carregando a imagem
        self.rect = pygame.Rect(0, 740, 20, 50)  # retangulo do player (posição x, y, altura, largura)

    def update(self, *args):
        # lógica
        keys = pygame.key.get_pressed() #keys recebe eventos teclas precionadas

        # movimentação
        if keys[pygame.K_d]:
            self.rect.x += 3
        elif keys[pygame.K_a]:
            self.rect.x -= 3
        elif keys[pygame.K_s]:
            self.rect.y += 3
        elif keys[pygame.K_w]:
            self.rect.y -= 3

        # lógica para jogador não sair do limite da tela
        if self.rect.top < 40:
            self.rect.top = 40
        elif self.rect.bottom > 728:
            self.rect.bottom = 728
        elif self.rect.left < 32:
            self.rect.left = 32
        elif self.rect.right > 992:
            self.rect.right = 992



class Enemy(Personagem):
    def __init__(self, vida, dano, arma, *groups):
        super().__init__(vida, dano, arma, *groups)

        self.image = pygame.image.load("arquivos/enemy.png")
        self.image = pygame.transform.scale(self.image, [20, 50])
        self.rect = self.image.get_rect()
        self.timer = 0

    def update(self,*args):
    # Comandos
        self.timer += 0.003
        self.rect.x = 512 + math.sin(self.timer) * 320

