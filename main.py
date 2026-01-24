import pygame
from settings import *
from level import Level

# Setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Side Scroller")
clock = pygame.time.Clock()

level = Level()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    level.run()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
