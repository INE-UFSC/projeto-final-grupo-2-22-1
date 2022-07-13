# -*- coding: utf-8 -*-
import pygame
from equipamentos import *
from personagens import *
from action import Disparo
from map import *
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

        # Grupos de sprites. (uma das funcionalidades dos grupos de sprite são de detectar colisões entre eles.)
        self.object_group = pygame.sprite.Group()
        self.actionGroup = pygame.sprite.Group()
        self.enemyGroup = pygame.sprite.Group()
        self.blockGroup = pygame.sprite.Group()


        self.gun = Arma()
        self.pocao = Item()

        self.vida = 100
        self.dano = 50


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

        font = pygame.font.Font('freesansbold.ttf', 18)
        self.porta = font.render("next map", True, (255, 255, 255), (0, 0, 0))
        self.portaRect = self.porta.get_rect()
        self.portaRect.center = (980, 400)


        self.draw_window(map1)

        # FPS
        self.clock = pygame.time.Clock()
        self.FPS = 120

    # Draw
    def draw_window(self,current_map):  # lógica para criação do map

        for y in range(len(current_map)):
            for x in range(len(current_map[y])):
                if current_map[y][x] == "X":
                    rect1 = Block(self.blockGroup)
                    rect1.rect.x = x * 32
                    rect1.rect.y = y * 32




    # Main
    def loop_menu(self):
        loopmenu=True
        display = pygame.display.set_mode([1024, 768])
        button1= button('#FCCAAE',393,445,225,66,'Novo jogo')
        self.display.fill((22,0,31)) 
        button2= button('#FCCAAE',393,570,222,63,'Opcoes')
        imagemfundo=pygame.image.load('imagem_fundo_menu.png')

        while loopmenu:
            display.blit(imagemfundo,(0,0))
            button1.draw(display)
            button2.draw(display)
            
            for ev in pygame.event.get(): 
                mouse = pygame.mouse.get_pos() 
                if ev.type == pygame.QUIT: 
                    pygame.quit() 
            
                if ev.type == pygame.MOUSEBUTTONDOWN: 
                    if button1.posicao(mouse):
                        return 1
                        loopmenu= False                        
                    if button2.posicao(mouse):
                        return 2
                        print('opcoes')
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

        button1= button('#008000',410,450,200,40,'On')
        button2 = button('#008000',410,600,200,40,'1')
        switch_som=1
        switch_dif=1
        display        
        while opcoes:

            for ev in pygame.event.get():
                pygame.display.update()

                mouse = pygame.mouse.get_pos() 
                button1.draw(display)
                button2.draw(display)
                if ev.type == pygame.QUIT: 
                    pygame.quit() 
                if ev.type==pygame.MOUSEBUTTONDOWN:
                    if button1.posicao(mouse):
                        switch_som+=1
                        if switch_som%2==0:
                            button1= button('#FF0000',410,450,200,40,'Off')
                        else:
                            button1= button('#008000',410,450,200,40,'On')

                    if button2.posicao(mouse):
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

                        
                        print('foi')



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
    
