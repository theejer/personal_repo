from settings import SCREEN_HEIGHT
import pygame 
from settings import *
from player import Player
from camera import CameraGroup

class Wall(pygame.sprite.Sprite):
    def __init__(self, length, height, color='gray'):
        super().__init__()
        self.image = pygame.Surface((length, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(0, SCREEN_HEIGHT - height))


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
        
        # Collision Sprites Group
        self.collision_sprites = pygame.sprite.Group()

        # Floor
        self.floor = Wall(2000, 64)
        self.camera_group.add(self.floor)
        self.collision_sprites.add(self.floor)

        # Tall Wall
        self.wall = Wall(64, 1000)
        self.camera_group.add(self.wall)
        self.collision_sprites.add(self.wall)
        
        # Floating Platform
        platform = Wall(300, 32, 'green')
        platform.rect.topleft = (500, 500)
        self.camera_group.add(platform)
        self.collision_sprites.add(platform)

    def horizontal_collision(self):
        self.player.move()
        collidable_sprites = self.collision_sprites.sprites()
        
        for sprite in collidable_sprites:
            if sprite.rect.colliderect(self.player.rect):
                if self.player.direction.x < 0: # Moving Left
                    self.player.rect.left = sprite.rect.right
                elif self.player.direction.x > 0: # Moving Right
                    self.player.rect.right = sprite.rect.left
                

    def vertical_collision(self):
        self.player.apply_gravity()
        collidable_sprites = self.collision_sprites.sprites()
        
        for sprite in collidable_sprites:
            if sprite.rect.colliderect(self.player.rect):
                if self.player.direction.y > 0: # Falling Down
                    self.player.rect.bottom = sprite.rect.top
                    self.player.direction.y = 0
                    self.player.jumps = 2 # Reset Jumps Logic
                elif self.player.direction.y < 0: # Jumping Up
                    self.player.rect.top = sprite.rect.bottom
                    self.player.direction.y = 0 # Bonk head, stop moving up

    def wall_check(self):
        self.player.wall_hold()
        temp_rect_left = pygame.Rect(self.player.rect.x-1, self.player.rect.y, 1,64)


        temp_rect_right = pygame.Rect(self.player.rect.x+1, self.player.rect.y, 1,64)

        for sprite in self.collision_sprites.sprites():
            if (sprite.rect.colliderect(temp_rect_left) or sprite.rect.colliderect(temp_rect_right)) and self.player.direction.y != 0:
                if (not self.player.on_wall):
                    self.player.direction.y = 0
                self.player.on_wall = True
                return
        self.player.on_wall = False


    def run(self):
        # 1. Update Player (handles input, x movement)
        self.player.jump()
        
        # 2. Physics & Collisions
        # We separate axes to prevent getting stuck in corners
        self.horizontal_collision()
        self.vertical_collision()
        self.wall_check()
        
        # 3. Draw
        self.display_surface.fill('black')
        self.camera_group.custom_draw(self.player)
