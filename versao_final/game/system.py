import pygame
from game.UI.interface import Interface
from game.level import Level
from game.entity.player import Player  #Player sera instanciado aqui, assim
from game.entity.enemy import Enemy

class Control():
    def __init__(self):

        pygame.init()
        pygame.display.set_caption("Jogo do grupo 2")

        try:
            self.__maps = ['versao_final/game/maps/map1.json', 'versao_final/game/maps/map1.json'] 

        except FileNotFoundError:  
            self.__maps = ['versao_final\game\maps\map1.json', 'versao_final\game\maps\map2.json']

        self.__last_key = ''
        self.__current_map = 0

        self.__change_map = False


        self.__clock = pygame.time.Clock()
        self.__FPS = 120
        self.display = pygame.display.set_mode([1024, 768])

        self.__object_group = pygame.sprite.Group()
        self.__enemyGroup = pygame.sprite.Group()
        self.__blockGroup = pygame.sprite.Group()
        self.__doorGroup = pygame.sprite.Group()

        self.__python_groups = [self.__object_group, self.__enemyGroup, self.__blockGroup, self.__doorGroup]

        self.__player = Player(200,50,self.__object_group)
        self.__level = Level(self.__player, self.__maps[self.__current_map], self.__python_groups)
        



    def start(self):
        gameLoop = True
        while gameLoop:
            self.__clock.tick(self.__FPS)  
            self.display.fill((0,0,0))
            self.__level.run()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameLoop = False

                if self.__level.next_map and self.__change_map:
                    self.__change_map = False
                    

                    print(self.__current_map)
                    print(self.__maps[self.__current_map])

                    #erro aqui talvez
                    self.__level = Level(self.__player, self.__maps[1], self.__python_groups)

            
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        if not pygame.sprite.spritecollide(self.__player, self.__blockGroup, False):
                            self.__player.mover_direita()
                            self.__last_key  = 'D'         
        
                    if event.key == pygame.K_a:
                        if not pygame.sprite.spritecollide(self.__player, self.__blockGroup, False):
                            self.__player.mover_esquerda()
                            self.__last_key  = 'A'  


                                        
                    if event.key == pygame.K_w:
                        if not pygame.sprite.spritecollide(self.__player, self.__blockGroup, False):
                            self.__player.mover_cima()
                            self.__last_key  = 'W'     

                                    
                    if event.key == pygame.K_s:
                        if not pygame.sprite.spritecollide(self.__player, self.__blockGroup, False):
                            self.__player.mover_baixo()
                            self.__last_key  = 'S' 
    

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        self.__player.velocidadeX = 0
                    if event.key == pygame.K_a:
                        self.__player.velocidadeX = 0
                    if event.key == pygame.K_w:
                        self.__player.velocidadeY = 0        
                    if event.key == pygame.K_s:
                        self.__player.velocidadeY = 0

                '''
                #colisao
                if pygame.sprite.spritecollide(self.__player, self.__blockGroup, False):
            
                    if  self.__last_key == 'D':
                        self.__player.velocidadeX = 0
                        self.__player.intencao_pos[0] -= 2

                  
                    elif self.__last_key == 'A':
                        self.__player.velocidadeX = 0
                        self.__player.intencao_pos[0] += 2

                         
                    elif self.__last_key == 'W':
                        self.__player.velocidadeY = 0
                        self.__player.intencao_pos[1] += 2

                          
                    elif self.__last_key == 'S':
                        self.__player.velocidadeY = 0
                        self.__player.intencao_pos[1] -= 2      
                '''   
                        


               
                if pygame.sprite.spritecollide(self.__player, self.__doorGroup, True) and not self.__change_map:
                    self.__level.next_map = True
                    self.__current_map += 1
                    self.__change_map = True




            self.__player.update()
            pygame.display.update()
 
    @property
    def maps(self):
        return self.__maps

        
