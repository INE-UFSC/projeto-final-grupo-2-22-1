# -*- coding: utf-8 -*-
import pygame
from equipamentos import *
from personagens import *
from action import Disparo
from map import *

BLACK = (46, 46, 46)
GREEN = (0, 128, 0)
GRAY = (207,207,196)
ultima_tecla = 'x'
mapa_atual = 1

def init():
    pass

# iniciar pygame
pygame.init()
# tamanho da janela
display = pygame.display.set_mode([1024, 768])
# nome do display
pygame.display.set_caption("Jogo do grupo 2")

# Grupos de sprites. (uma das funcionalidades dos grupos de sprite são de detectar colisões entre eles.)
objectGroup = pygame.sprite.Group()
actionGroup = pygame.sprite.Group()
enemyGroup = pygame.sprite.Group()
blockGroup = pygame.sprite.Group()
portaGroup = pygame.sprite.Group()

#para testes arma (em construção)
gun = Arma()
pocao = Item()
vida = 100
dano = 50

#instancioando objetos
jogador = Player(100,50,gun,pocao,objectGroup)
newEnemy0 = Enemy(vida, dano, gun ,  objectGroup,enemyGroup)
newEnemy0.rect.center = [812, 584] # posição
newEnemy1 = Enemy(vida, dano, gun , objectGroup,enemyGroup)
newEnemy1.rect.center = [112, 284]

#barra de vida e barra de armamentos
font = pygame.font.Font('freesansbold.ttf', 32)
barraVida = font.render("Aqui quantas vidas o personagem tem", True, (255, 255, 255), (0, 0, 0))
barraVidaRect = barraVida.get_rect()
barraVidaRect.center = (512, 20)

barraArmamento = font.render("Aqui os armamentos", True, (255, 255, 255), (0, 0, 0))
barraArmamentoRect = barraArmamento.get_rect()
barraArmamentoRect.center = (512, 748)

# Draw
def draw_window(current_map):  # lógica para criação do mapa
    for y in range(len(current_map)):
        for x in range(len(current_map[y])):
            if current_map[y][x] == "X":
                rect1 = Block(blockGroup)
                rect1.rect.x = x * 32
                rect1.rect.y = y * 32
            if current_map[y][x] == "P":
                rect1 = Porta(portaGroup)
                rect1.rect.x = x * 32
                rect1.rect.y = y * 32

draw_window(map1)                   

#FPS
clock = pygame.time.Clock()
FPS = 120

# Main
def loop_principal():
    gameLoop = True
    while gameLoop:
        clock.tick(FPS)  #método tick, força gameLoop a rodar em FPS atribuido

        for event in pygame.event.get(): #eventos de mouse ou teclado

            if event.type == pygame.QUIT:
                gameLoop = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    novoDisparo = Disparo(objectGroup, actionGroup)
                    novoDisparo.rect.center = jogador.rect.center
                if event.key == pygame.K_d:
                    jogador.mover_direita()
                    ultima_tecla = 'D'                   
                if event.key == pygame.K_a:
                    jogador.mover_esquerda()
                    ultima_tecla = 'A'                    
                if event.key == pygame.K_w:
                    jogador.mover_cima()
                    ultima_tecla = 'W'                   
                if event.key == pygame.K_s:
                    jogador.mover_baixo()
                    ultima_tecla = 'S'                 
                 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    jogador.velocidadeX = 0
                if event.key == pygame.K_a:
                    jogador.velocidadeX = 0
                if event.key == pygame.K_w:
                    jogador.velocidadeY = 0        
                if event.key == pygame.K_s:
                    jogador.velocidadeY = 0                                
            
        # colisões
        if jogador.teste_colisao(blockGroup):
            if ultima_tecla == 'D':
                jogador.velocidadeX = 0
                jogador.intencao_pos[0] -= 2
            if ultima_tecla == 'A':
                jogador.velocidadeX = 0
                jogador.intencao_pos[0] += 2
            if ultima_tecla == 'W':
                jogador.velocidadeY = 0
                jogador.intencao_pos[1] += 2
            if ultima_tecla == 'S':
                jogador.velocidadeY = 0
                jogador.intencao_pos[1] -= 2

        pygame.sprite.groupcollide(actionGroup, enemyGroup, True, True)  # colisão entre tiro e inimigo
        pygame.sprite.groupcollide(actionGroup, blockGroup, True, False)  # colisão entre tiro e mapa

        collisionPlayerEnemy = pygame.sprite.spritecollide(jogador, enemyGroup, False, pygame.sprite.collide_mask) # colisão entre jogador e inimigo
        if collisionPlayerEnemy:
            if  0 >= (jogador.vida - 50):    #Gambiarra pra n ficar indo num loop infinito
                gameLoop = False
            jogador.tomar_dano(50)

        # draw
        display.fill(BLACK)
        display.blit(barraVida, barraVidaRect), (barraArmamento, barraArmamentoRect)
        display.blit(barraArmamento, barraArmamentoRect)
        portaGroup.draw(display)
        objectGroup.draw(display)
        blockGroup.draw(display)  #desenha os sprites do mapa
     
        # update
        objectGroup.update()
        pygame.display.update()

def menu_defeat():
    defeat_loop = True
    while defeat_loop:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                defeat_loop = False

        display.fill(BLACK)
        font = pygame.font.Font('freesansbold.ttf', 72)
        defeat_text = font.render("GAME OVER", True, (255, 0, 0))
        display.blit(defeat_text, (275, 350))
        pygame.display.update()


def menu_win():
    win_loop = True
    while win_loop:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                win_loop = False

        display.fill(GRAY)
        font = pygame.font.Font('freesansbold.ttf', 72)
        win_text = font.render("Você ganhou!", True, (0, 170, 0))
        display.blit(win_text, (275,350))
        pygame.display.update()