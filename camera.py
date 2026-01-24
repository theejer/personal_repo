from settings import SCREEN_WIDTH
import player
import pygame
from settings import *

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

        self.display_surface = pygame.display.get_surface()

        self.offset = pygame.math.Vector2()

        self.half_w = SCREEN_WIDTH // 2
        self.half_h = 3 * SCREEN_HEIGHT // 4

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_w
        self.offset.y = player.rect.centery - self.half_h

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset

            self.display_surface.blit(sprite.image, offset_pos)
