import pygame
import math
from equipamentos import *
from personagens.personagem import Personagem
from action import *
class Player(Personagem):
    def __init__(self,vida ,dano ,arma, item: Item, *groups):
        super().__init__(vida,dano,arma, *groups)
        self.__item = Item
        self.image = pygame.image.load("prototipo/arquivos/careca.png")  # carregando a imagem
        self.rect = pygame.Rect(40, 680, 20, 50)  # retangulo do player (posição x, y, altura, largura)
        self.velocidadeX = 0
        self.velocidadeY = 0
        self.intencao_pos = list(self.rect.center)
        self.ultima_tecla = 'x'

        #print(self.__vida)   #Erro aqui "AttributeError: 'Player' object has no attribute 'vida'"


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
    
    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    novoDisparo = Disparo(self.object_group, self.actionGroup)
                    novoDisparo.rect.center = self.jogador.rect.center

                if event.key == pygame.K_d:
                    self.mover_direita()
                    self.ultima_tecla = 'D'                   
                if event.key == pygame.K_a:
                    self.mover_esquerda()
                    self.ultima_tecla = 'A'                    
                if event.key == pygame.K_w:
                    self.mover_cima()
                    self.ultima_tecla = 'W'                   
                if event.key == pygame.K_s:
                    self.mover_baixo()
                    self.ultima_tecla = 'S'  

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.velocidadeX = 0
                if event.key == pygame.K_a:
                    self.velocidadeX = 0
                if event.key == pygame.K_w:
                    self.velocidadeY = 0        
                if event.key == pygame.K_s:
                    self.velocidadeY = 0    

    def teste_colisao(self, grupo):
        if pygame.sprite.spritecollide(self, grupo, False):
            if self.teste_colisao(Fase.blockGroup):
                if self.ultima_tecla == 'D':
                    self.velocidadeX = 0
                    self.intencao_pos[0] -= 2
                if self.ultima_tecla == 'A':
                    self.velocidadeX = 0
                    self.intencao_pos[0] += 2
                if self.ultima_tecla == 'W':
                    self.velocidadeY = 0
                    self.intencao_pos[1] += 2
                if self.ultima_tecla == 'S':
                    self.velocidadeY = 0
                    self.intencao_pos[1] -= 2

        else:
            return  False 
            