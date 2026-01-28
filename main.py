import pygame
from settings import *
from level import Level
from level1 import tilesheet

# Setup
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformerer")
clock = pygame.time.Clock()

level = Level(tilesheet)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    level.run()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
