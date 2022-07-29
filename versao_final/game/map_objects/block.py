import pygame
class Block(pygame.sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)
<<<<<<< HEAD
        self.image = pygame.image.load('versao_final\game\image\Block\green_block.png').convert_alpha()  
=======
        self.image = pygame.image.load('versao_final\game\image\Block\green_block.png').convert_alpha()     
>>>>>>> becf2d8e06329a22a36180a8e6bfee29c30ef1c8
        self.rect = self.image.get_rect(topleft = pos)