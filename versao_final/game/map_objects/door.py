import pygame
class Door(pygame.sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("/home/hpereira1/Documents/projeto-final-grupo-2-22-1/versao_final/game/image/Block/green_block.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)