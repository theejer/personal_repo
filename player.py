import pygame
from entity import Entity

class Player(Entity):
    def __init__(self, name, pos):
        super().__init__(name, pos)
        self.width = 32
        self.height = 64
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft=pos)
        self.jumps = 2
        self.on_wall = False

    # Override
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
            
        self.rect.x += self.direction.x * self.speed

    # Override
    def jump(self):
        keys = pygame.key.get_just_pressed()
        if keys[pygame.K_SPACE] and self.direction.y >= 0 and self.jumps > 0:
            self.direction.y = self.jump_speed
            self.jumps -= 1

    def wall_hold(self):
        keys = pygame.key.get_pressed()
        # Only cling if we are actually touching a wall AND falling
        if (self.on_wall) and keys[pygame.K_SPACE] and self.direction.y > 0:
            self.gravity = 0.05
            self.direction.x = 0
            # print("WALL HOLD GRAVITY")
        else:
            self.gravity = 0.8
            # print("NORMAL GRAVITY")