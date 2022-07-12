# -*- coding: utf-8 -*-
from fase import Fase
import pygame
from equipamentos import *
from personagens.player import *
from personagens.enemy import *
from blocks import *
from configs import *
from fase import *
class Game():
    def __init__(self):

        self.BLACK = (46, 46, 46)
        self.GREEN = (0, 128, 0)
        self.GRAY = (207, 207, 196)


        # iniciar pygame
        pygame.init()
        # tamanho da janela
        self.display = pygame.display.set_mode([1024, 768])
        # nome do display
        pygame.display.set_caption("Jogo do grupo 2")
        self.fase = Fase()
        self.clock = pygame.time.Clock()
        self.FPS = 120
 # Main
    def loop_principal(self):

        gameLoop = True
        while gameLoop:
            self.clock.tick(self.FPS)  # método tick, força gameLoop a rodar em FPS atribuido
            # eventos de mouse ou teclado
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameLoop = False
            self.fase.run()
                # colisões
            collisionPlayerEnemy = pygame.sprite.spritecollide(self, self.enemyGroup, False, pygame.sprite.collide_mask) # colisão entre jogador e inimigo
            pygame.sprite.groupcollide(self.actionGroup, self.enemyGroup, True, True)  # colisão entre tiro e inimigo
            pygame.sprite.groupcollide(self.actionGroup, self.blockGroup, True, False)  # colisão entre tiro e mapa

           
           #Logica de dano e menu_defeat()
            
            if collisionPlayerEnemy:
                if  0 >= (self.jogador.vida - 50):    
                    gameLoop = False

                self.jogador.tomar_dano(50)

            if self.jogador.vida <=0:
                self.menu_defeat()


            # draw
            self.display.fill(self.BLACK)
            self.display.blit(self.barraVida, self.barraVidaRect), (self.barraArmamento, self.barraArmamentoRect)
            self.display.blit(self.barraArmamento, self.barraArmamentoRect)
            self.portaGroup.draw(self.display)
            self.object_group.draw(self.display)
            self.blockGroup.draw(self.display)  # desenha os sprites

            # updated
            self.object_group.update()
            pygame.display.update()

            if (959 < self.jogador.rect.centerx < 982) and  (400  < self.jogador.rect.bottom < 500):
                gameLoop = False
                self.menu_win()

            


    def menu_defeat(self):
        defeat_loop = True
        while defeat_loop:
            self.clock.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    defeat_loop = False


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