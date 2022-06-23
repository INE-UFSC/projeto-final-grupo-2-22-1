import pygame

class Player(pygame.sprite.Sprite): # classe Player herda de pygame.sprite.Sprite
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("arquivos/careca.png")  # carregando a imagem
        self.rect = pygame.Rect(0, 740, 20, 50)  # retangulo do player (posição x, y, altura, largura)

    def update(self, *args):
        # lógica
        keys = pygame.key.get_pressed() #keys recebe eventos teclas precionadas

        # movimentação
        if keys[pygame.K_d]:
            self.rect.x += 1
        elif keys[pygame.K_a]:
            self.rect.x -= 1
        elif keys[pygame.K_s]:
            self.rect.y += 1
        elif keys[pygame.K_w]:
            self.rect.y -= 1

        # lógica para personagem não sair do limite da tela
        if self.rect.top < 40:
            self.rect.top = 40
        elif self.rect.bottom > 728:
            self.rect.bottom = 728
        elif self.rect.left < 32:
            self.rect.left = 32
        elif self.rect.right > 992:
            self.rect.right = 992





