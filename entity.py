import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, name, pos):
        super().__init__()
        self.name = name
        # Movement logic
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -12

    def move(self):
        pass

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        pass