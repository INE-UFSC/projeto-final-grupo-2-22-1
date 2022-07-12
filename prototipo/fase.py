import pygame
from personagens.player import Player
from personagens.enemy import Enemy
from blocks import *
from action import *
from configs import *
from equipamentos import *

class Fase:
    def __init__(self):
        self.object_group = pygame.sprite.Group()
        self.actionGroup = pygame.sprite.Group()
        self.enemyGroup = pygame.sprite.Group()
        self.blockGroup = pygame.sprite.Group()
        self.portaGroup = pygame.sprite.Group()

        self.vida = 100
        self.dano = 50
        self.gun = Arma()
        self.pocao = Item()

   
    def run(self):

        self.jogador = Player(100,50,self.gun,self.pocao,self.object_group)

        self.imagem_inimigo = pygame.image.load("prototipo/arquivos/enemy.png")
 
        self.newEnemy0 = Enemy(self.vida, self.dano, self.gun , self.imagem_inimigo, self.object_group,self.enemyGroup)
        self.newEnemy0.rect.center = [812, 584] # posição
        self.newEnemy1 = Enemy(self.vida, self.dano, self.gun ,self.imagem_inimigo, self.object_group,self.enemyGroup)
        self.newEnemy1.rect.center = [112, 284]

        #Barra de vida e armamentos
        font = pygame.font.Font('freesansbold.ttf', 32)
        self.barraVida = font.render("Aqui quantas vidas o personagem tem", True, (255, 255, 255), (0, 0, 0))
        self.barraVidaRect = self.barraVida.get_rect()
        self.barraVidaRect.center = (512, 20)

        self.barraArmamento = font.render("Aqui os armamentos", True, (255, 255, 255), (0, 0, 0))
        self.barraArmamentoRect = self.barraArmamento.get_rect()
        self.barraArmamentoRect.center = (512, 748)

        self.draw_window(map1)
    def draw_window(self,current_map):  # lógica para criação do map

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

