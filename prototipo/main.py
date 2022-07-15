# -*- coding: utf-8 -*-

import pygame
from fase import Fase
from equipamentos import *
from personagens.player import *
from personagens.enemy import *
from blocks import *
from configs import *
from fase import *
from botao import button

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
    def loop_menu(self):
        loopmenu=True
        button1= button('#FCCAAE',393,445,225,66,'Novo jogo')
        self.display.fill((22,0,31)) 
        button2= button('#FCCAAE',393,570,222,63,'Opcoes')
        imagemfundo=pygame.image.load('imagem_fundo_menu.png')

        while loopmenu:
            self.display.blit(imagemfundo,(0,0))
            button1.draw(self.display)
            button2.draw(self.display)
            
            for ev in pygame.event.get(): 
                mouse = pygame.mouse.get_pos() 
                if ev.type == pygame.QUIT: 
                    pygame.quit() 
            
                if ev.type == pygame.MOUSEBUTTONDOWN: 
                    if button1.posicao(mouse):
                        self.loop_principal()
                        loopmenu= False                        
                    if button2.posicao(mouse):
                        self.loop_opcoes()
                        loopmenu= False 
                if ev.type ==pygame.MOUSEMOTION:
                    if button1.posicao(mouse):
                        button1.color = '#FF8845'
                    else:
                        button1.color= '#FCCAAE'   
                    if button2.posicao(mouse):
                        button2.color = '#FF8845'
                    else:
                        button2.color= '#FCCAAE'   
                pygame.display.update()
    def loop_opcoes(self):
        opcoes=True
        display = pygame.display.set_mode([1024, 768])
        self.display.fill((22,0,31)) 

        button1= button('#008000',410,350,200,40,'On')
        button2 = button('#008000',410,450,200,40,'1')
        button3 = button('#008000',410,550,200,40,'voltar')
        switch_som=1
        switch_dif=1        
        while opcoes:

            for ev in pygame.event.get():
                pygame.display.update()

                mouse = pygame.mouse.get_pos() 
                button1.draw(display)
                button2.draw(display)
                button3.draw(display)
                if ev.type == pygame.QUIT: 
                    pygame.quit() 
                if ev.type==pygame.MOUSEBUTTONDOWN:
                    #implementar logica para som
                    if button1.posicao(mouse):
                        switch_som+=1
                        if switch_som%2==0:
                            button1= button('#FF0000',410,450,200,40,'Off')
                        else:
                            button1= button('#008000',410,450,200,40,'On')

                    if button2.posicao(mouse):
                        #implementar logica para dificuldade
                        switch_dif+=1
                        if switch_dif==1:
                            button2 = button('#008000',410,600,200,40,'1')
                        elif switch_dif==2:
                            button2 = button('#008000',410,600,200,40,'2')
   
                        elif switch_dif==3:
                            button2 = button('#008000',410,600,200,40,'3')

                        elif switch_dif==4:
                            switch_dif=1
                            button2 = button('#008000',410,600,200,40,'1')
                    if button3.posicao(mouse):
                        opcoes = False
                        self.loop_menu()



    def loop_principal(self):
        

        gameLoop = True
        while gameLoop:
            self.clock.tick(self.FPS)  # método tick, força gameLoop a rodar em FPS atribuido
            # eventos de mouse ou teclado
            for event in pygame.event.get():


                if event.type == pygame.QUIT:
                    gameLoop = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        novoDisparo = Disparo(self.object_group, self.actionGroup)
                        novoDisparo.rect.center = self.jogador.rect.center

                    if event.key == pygame.K_d:
                        self.jogador.mover_direita()

                    if event.key == pygame.K_a:
                        self.jogador.mover_esquerda()

                    if event.key == pygame.K_w:
                        self.jogador.mover_cima()

                    if event.key == pygame.K_s:
                        self.jogador.mover_baixo()
                    if event.key == pygame.K_ESCAPE:
                        gameLoop= False
                        self.game_pause()


                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d or event.key == pygame.K_a:
                        self.jogador.parar_horizontal()
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        self.jogador.parar_vertical()

            # colliding
            pygame.sprite.groupcollide(self.actionGroup, self.enemyGroup, True, True)  # colisão entre tiro e inimigo
            collisionPlayerEnemy = pygame.sprite.spritecollide(self.jogador, self.enemyGroup, False, pygame.sprite.collide_mask) # colisão entre jogador e inimigo

            if collisionPlayerEnemy:
                if  0 >= (self.jogador.vida - 50):    #Gambiarra pra n ficar indo num loop infinito
                    gameLoop = False

                self.jogador.tomar_dano(50)

            if self.jogador.vida <=0:
                self.menu_defeat()


            self.jogador.teste_colisao(self.blockGroup)



            # draw
            self.display.fill(self.BLACK)
            self.display.blit(self.barraVida, self.barraVidaRect), (self.barraArmamento, self.barraArmamentoRect)
            self.display.blit(self.barraArmamento, self.barraArmamentoRect)
            self.display.blit(self.porta, self.portaRect)
            self.object_group.draw(self.display)
            self.blockGroup.draw(self.display)  # desenha os sprites

            # updated
            self.object_group.update()
            pygame.display.update()

            if (959 < self.jogador.rect.centerx < 982) and  (400  < self.jogador.rect.bottom < 500):
                gameLoop = False
                self.menu_win()

            print(self.jogador.rect.centerx, self.jogador.rect.bottom)

    def game_pause(self):
        self.display.fill(self.BLACK)
        pausa=True
        while pausa:
            for ev in pygame.event.get():
                if ev.type==pygame.KEYDOWN:
                    if ev.key ==pygame.K_ESCAPE:
                        pausa = False
                        self.loop_principal()
            pygame.display.update()


    def menu_defeat(self):
        defeat_loop = True
        botao= button('#FCCAAE',393,445,225,66,'voltar ao lobby')
        while defeat_loop:
            self.clock.tick(self.FPS)

            for event in pygame.event.get():
                botao.draw(self.display)

                if event.type == pygame.QUIT:
                    defeat_loop = False


            self.display.fill(self.BLACK)
            font = pygame.font.Font('freesansbold.ttf', 72)
            defeat_text = font.render("GAME OVER", True, (255, 0, 0))
            self.display.blit(defeat_text, (260, 150))

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

    
