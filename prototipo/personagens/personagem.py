import pygame
from equipamentos import *
from abc import ABC, abstractmethod



class Personagem(ABC, pygame.sprite.Sprite):
    def __init__(self, vida, dano, arma: Arma, *groups):
        super().__init__(*groups)
        self.__vida = vida
        self.__dano = dano
        self.__arma = arma


    @abstractmethod
    def update(self):
        pass

    @property
    def vida(self):
        return self.__vida
    @vida.setter
    def vida(self,vida):
        self.__vida = vida

    @property
    def dano(self):
        return self.__dano
    @dano.setter
    def dano(self,dano):
        self.__dano = dano

    @property
    def arma(self):
        return self.__arma
    @arma.setter
    def arma(self, arma):
        return self.__arma


    def tomar_dano(self, qtdade_dano):
        self.__vida = self.__vida - qtdade_dano

