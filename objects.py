import pygame

class Collidable(pygame.sprite.Sprite):
    def __init__(self, length, height, x, y, color='gray'):
        super().__init__()
        self.image = pygame.Surface((length, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
        # self.wall_holdable = False

    def horizontal_collision(self, entity):
        pass

    def vertical_collision(self, entity):
        pass

class SolidWall(Collidable):
    def __init__(self, length, height, x, y, color='gray'):
        super().__init__(length, height, x, y, color)
        # self.wall_holdable = True

    def horizontal_collision(self, entity):
        if self.rect.colliderect(entity.rect):
            if entity.direction.x < 0: # Moving Left
                entity.rect.left = self.rect.right
            elif entity.direction.x > 0: # Moving Right
                entity.rect.right = self.rect.left

        if hasattr(entity, 'on_wall'):
            temp_rect_left = pygame.Rect(entity.rect.x-1, entity.rect.y, 1,entity.height)
            temp_rect_right = pygame.Rect(entity.rect.x+1, entity.rect.y, 1,entity.height)
            if (self.rect.colliderect(temp_rect_left) or self.rect.colliderect(temp_rect_right)) and entity.direction.y != 0:
                entity.on_wall = True
                # print("ENTITY ON WALL")

    def vertical_collision(self, entity):
        if self.rect.colliderect(entity.rect):
            if entity.direction.y > 0: # Falling Down
                entity.rect.bottom = self.rect.top
                entity.direction.y = 0
                if hasattr(entity, 'jumps'):
                    entity.jumps = 2 # Reset Jumps Logic
            elif entity.direction.y < 0: # Jumping Up
                entity.rect.top = self.rect.bottom
                entity.direction.y = 0 # Bonk head, stop moving up
                # print("BONK HEAD")

class Platform(Collidable):
    def __init__(self, length, height, x, y, color='white'):
        super().__init__(length, height, x, y, color)
        # self.wall_holdable = False

    def vertical_collision(self, entity):
        temp_entity_bottom = pygame.Rect(entity.rect.x, entity.rect.bottom-1, entity.width, 1)
        if temp_entity_bottom.colliderect(self.rect):
            if entity.direction.y > 0: # Falling Down
                entity.rect.bottom = self.rect.top
                entity.direction.y = 0
                if hasattr(entity, 'jumps'):
                    entity.jumps = 2
                # print(f"PLATFORM COLLIDED WITH {entity.name}")

    def horizontal_collision(self, entity):
        pass

class Message(pygame.sprite.Sprite):
    def __init__(self, text, font, color=(255,255,255), pos=(0,0)):
        super().__init__()
        self.font = font
        self.text = text
        self.color = color
        self.rect = pygame.Rect(pos, (0,0))
        self.appear()

    def appear(self):
        self.image = self.font.render(self.text, True, self.color)
        self.rect.size = self.image.get_size()

