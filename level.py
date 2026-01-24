import pygame 
from settings import *
from player import Player
from camera import CameraGroup

class Level:
    def __init__(self):
        # Get the display surface
        self.display_surface = pygame.display.get_surface()
        
        # Sprite groups - CHAANGE: Use our new CameraGroup
        self.camera_group = CameraGroup()
        self.setup_level()
        
    def setup_level(self):
        self.player = Player((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.camera_group.add(self.player)
        
        # Create a Floor Sprite so the camera can draw it!
        # Before we just drew a rect, now we need a sprite for the group logic to work easily
        self.floor = pygame.sprite.Sprite()
        self.floor.image = pygame.Surface((2000, 64)) # Make it LONG (2000px)
        self.floor.image.fill('gray')
        self.floor.rect = self.floor.image.get_rect(topleft=(0, SCREEN_HEIGHT - 64))
        self.camera_group.add(self.floor)

    def vertical_collision(self):
        self.player.apply_gravity()
        
        # Check collision with the floor sprite
        if self.player.rect.colliderect(self.floor.rect):
            if self.player.direction.y > 0: # Falling down
                self.player.rect.bottom = self.floor.rect.top
                self.player.direction.y = 0
                self.player.jumps = 2
                
    def run(self):
        # 1. Update Player (handles input, x movement)
        self.player.move()
        self.player.jump()
        
        # 2. Handle Vertical Physics (Gravity + Floor Check)
        self.vertical_collision()
        
        # 3. Draw - CHANGE: Use custom_draw
        self.display_surface.fill('black')
        self.camera_group.custom_draw(self.player)
