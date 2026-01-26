import pygame

class CollisionObject(pygame.sprite.Sprite):
    def __init__(self, length, height, x, y, color='gray'):
        super().__init__()
        self.image = pygame.Surface((length, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
