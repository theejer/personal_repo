import pygame

class CollisionObject(pygame.sprite.Sprite):
    def __init__(self, length, height, x, y, color='gray'):
        super().__init__()
        self.image = pygame.Surface((length, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

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

