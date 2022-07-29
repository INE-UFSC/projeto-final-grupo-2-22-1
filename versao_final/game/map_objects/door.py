import pygame
class Door(pygame.sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("versao_finaldwgame\image\Object\door.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)