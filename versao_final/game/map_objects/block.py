import pygame
class Block(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("image/Block/green_block.png")     
        self.rect = self.image.get_rect()