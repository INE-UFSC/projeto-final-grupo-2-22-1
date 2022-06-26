import pygame



class Player(pygame.sprite.Sprite): # classe Player herda de pygame.sprite.Sprite
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("arquivos/careca.png")  # carregando a imagem
        self.rect = pygame.Rect(40, 680, 20, 50)  # retangulo do player (posição x, y, altura, largura)
        self.velocidadeX = 0
        self.velocidadeY = 0
        self.intencao_pos = list(self.rect.center)

    def update(self, *args):
       self.intencao_pos[0] += self.velocidadeX
       self.intencao_pos[1] += self.velocidadeY

    def mover_direita(self):
        if self.rect.right < 992:
            self.velocidadeX += 3
            self.intencao_pos[0] += self.velocidadeX

    def mover_esquerda(self):
        if self.rect.left > 32:
            self.velocidadeX -= 3
            self.intencao_pos[0] += self.velocidadeX    

    def mover_cima(self):
        if self.rect.top > 40:
            self.velocidadeY -= 3
            self.intencao_pos[1] += self.velocidadeY

    def mover_baixo(self):
        if self.rect.bottom < 728:
            self.velocidadeY += 3
            self.intencao_pos[1] += self.velocidadeY

    def parar_horizontal(self):
        self.velocidadeX = 0
        if self.rect.left < 32:
            self.rect.left = 32

    def parar_vertical(self):
        self.velocidadeY = 0            

    def autorizar_movimento(self):
        self.rect.center = self.intencao_pos
    
    def recusar_movimento(self):
        self.intecao_pos = list(self.rect.center)

    def teste_colisao(self, grupo):
        temp = self.rect.center
        self.rect.center = self.intencao_pos
        if not pygame.sprite.spritecollide(self, grupo, False):
            self.autorizar_movimento()
            
        else:
            self.rect.center = temp
            self.velocidadeX = 0
            self.velocidadeY = 0
            self.recusar_movimento()
            
            
        
        






