import pygame
class Door(pygame.sprite.Sprite):
    def __init__(self, image, *groups):
        super().__init__(image, *groups)
        self.image = pygame.image.load("image/Object/door.png")
        self.rect = self.image.get_rect()        