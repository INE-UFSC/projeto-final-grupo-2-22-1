import pygame
class Block(pygame.sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('versao_final\game\image\Block\green_block.png').convert_alpha()  
        self.rect = self.image.get_rect(topleft = pos)