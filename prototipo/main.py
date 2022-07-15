# -*- coding: utf-8 -*-
import pygame
from equipamentos import *
from personagens.player import *
from personagens.enemy import *
from action import Disparo
from map import *

class Game():

    def __init__(self):
        self.BLACK = (46, 46, 46)
        self.GREEN = (0, 128, 0)
        self.GRAY = (207, 207, 196)
        self.ultima_tecla = 'x'
        self.clock = pygame.time.Clock()
        self.FPS = 120
        self.mapa_atual = '1'
        
        # iniciar pygame
        pygame.init()
        # tamanho da janela
        self.display = pygame.display.set_mode([1024, 768])
        # nome do display
        pygame.display.set_caption("Jogo do grupo 2")

        # Grupos de sprites. (uma das funcionalidades dos grupos de sprite são de detectar colisões entre eles.)
        self.object_group = pygame.sprite.Group()
        self.actionGroup = pygame.sprite.Group()
        self.enemyGroup = pygame.sprite.Group()
        self.blockGroup = pygame.sprite.Group()
        self.portaGroup = pygame.sprite.Group()

        self.gun = Arma()
        self.pocao = Item()
        self.jogador = Player(100,50,self.gun,self.pocao,self.object_group)
        self.draw_map(map1)
        #self.newEnemy0 = Enemy(100, 10, self.gun, self.object_group,self.enemyGroup)
        #self.newEnemy1 = Enemy(100, 10, self.gun, self.object_group,self.enemyGroup)
        #self.newEnemy0.rect.center = [812, 584] # posição
        #self.newEnemy1.rect.center = [112, 284]

    def loop_principal(self):
        gameLoop = True
        while gameLoop:
            self.clock.tick(self.FPS)  # método tick, força gameLoop a rodar em FPS atribuido

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    gameLoop = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        novoDisparo = Disparo(self.object_group, self.actionGroup)
                        novoDisparo.rect.center = self.jogador.rect.center

                    if event.key == pygame.K_d:
                        self.jogador.mover_direita()
                        self.ultima_tecla = 'D'                   
                    if event.key == pygame.K_a:
                        self.jogador.mover_esquerda()
                        self.ultima_tecla = 'A'                    
                    if event.key == pygame.K_w:
                        self.jogador.mover_cima()
                        self.ultima_tecla = 'W'                   
                    if event.key == pygame.K_s:
                        self.jogador.mover_baixo()
                        self.ultima_tecla = 'S'  

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        self.jogador.velocidadeX = 0
                    if event.key == pygame.K_a:
                        self.jogador.velocidadeX = 0
                    if event.key == pygame.K_w:
                        self.jogador.velocidadeY = 0        
                    if event.key == pygame.K_s:
                        self.jogador.velocidadeY = 0    

            # draw
            self.display.fill(self.BLACK)
            self.portaGroup.draw(self.display)
            self.object_group.draw(self.display)
            self.blockGroup.draw(self.display) 

            # updated
            self.colision()
            self.object_group.update()
            self.next_map()
            if self.jogador.teste_colisao(self.enemyGroup):
                self.menu_defeat()
                gameLoop = False
            pygame.display.update()

    def next_map(self):
        if self.jogador.teste_colisao(self.portaGroup):
            pygame.time.wait(1000)
            self.jogador.intencao_pos[0] -= 935
            pygame.sprite.Group.empty(self.blockGroup)
            pygame.sprite.Group.empty(self.portaGroup)
            if self.mapa_atual == '1':
                self.mapa_atual = '2'
                self.draw_map(map2)
            elif self.mapa_atual == '2':
                self.mapa_atual = '3'
                self.draw_map(map3)
            else:
                self.menu_win()
                self.gameLoop = False
                              
    def draw_map(self,current_map):  # lógica para criação do map
        for y in range(len(current_map)):
            for x in range(len(current_map[y])):
                if current_map[y][x] == "X":
                    rect1 = Block(self.blockGroup)
                    rect1.rect.x = x * 32
                    rect1.rect.y = y * 32
                if current_map[y][x] == "P":
                    rect1 = Porta(self.portaGroup)
                    rect1.rect.x = x * 32
                    rect1.rect.y = y * 32

    def colision(self):
        pygame.sprite.groupcollide(self.actionGroup, self.enemyGroup, True, True)  # colisão entre tiro e inimigo
        pygame.sprite.groupcollide(self.actionGroup, self.blockGroup, True, False)  # colisão entre tiro e mapa 
        if self.jogador.teste_colisao(self.blockGroup):
                if self.ultima_tecla == 'D':
                    self.jogador.velocidadeX = 0
                    self.jogador.intencao_pos[0] -= 2
                if self.ultima_tecla == 'A':
                    self.jogador.velocidadeX = 0
                    self.jogador.intencao_pos[0] += 2
                if self.ultima_tecla == 'W':
                    self.jogador.velocidadeY = 0
                    self.jogador.intencao_pos[1] += 2
                if self.ultima_tecla == 'S':
                    self.jogador.velocidadeY = 0
                    self.jogador.intencao_pos[1] -= 2                               
        
    def menu_defeat(self):
        defeat_loop = True
        while defeat_loop:
            self.clock.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    defeat_loop = False
                    gameLoop = False

            self.display.fill(self.BLACK)
            font = pygame.font.Font('freesansbold.ttf', 72)
            defeat_text = font.render("GAME OVER", True, (255, 0, 0))
            self.display.blit(defeat_text, (275, 350))
            pygame.display.update()

    def menu_win(self):
        win_loop = True
        while win_loop:
            self.clock.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    win_loop = False

            self.display.fill(self.GRAY)
            font = pygame.font.Font('freesansbold.ttf', 72)
            win_text = font.render("Você ganhou!", True, (0, 170, 0))
            self.display.blit(win_text, (275,350))
            pygame.display.update()

    
       





#LÓGICA DE COMBATE RETIRADA TEMPORARIAMENTE - 13/07 - 00:40
        #Logica de dano e menu_defeat()
        #if collisionPlayerEnemy:
        #    if  0 >= (self.jogador.vida - 50):    
        #        gameLoop = False
        #    self.jogador.tomar_dano(50)

        #if self.jogador.vida <=0:
        #    self.menu_defeat()        
