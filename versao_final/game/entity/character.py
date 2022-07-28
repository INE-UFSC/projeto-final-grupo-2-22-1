import pygame
from abc import ABC, abstractmethod


class Character(ABC, pygame.sprite.Sprite):
    def __init__(self, vida, dano, *groups):
        super().__init__(*groups)
        self.__vida = vida
        self.__dano = dano
        

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

   








