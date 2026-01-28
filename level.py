from settings import SCREEN_WIDTH
from settings import SCREEN_HEIGHT
import pygame 
from settings import *
from player import Player
from camera import CameraGroup
from objects import CollisionObject, Message
from physics import PhysicsManager



class Level:
    def __init__(self, tilesheet):
        # Get the display surface
        self.display_surface = pygame.display.get_surface()
        
        # Sprite groups - CHAANGE: Use our new CameraGroup
        self.camera_group = CameraGroup()
        self.collision_group = pygame.sprite.Group()
        self.platform_group = pygame.sprite.Group()

        self.tilesheet = tilesheet
        self.setup_level()
        self.physics_manager = PhysicsManager(self.player, self.collision_group, self.platform_group)
        self.message = Message("", pygame.font.SysFont(None, 128), (255, 0, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        
    def setup_level(self):
        
        
        # Collision Sprites Group

        # Reading Tilesheet
        x_axis = 0
        y_axis = 0

        player_pos = ()
        player_falling = True

        for row in self.tilesheet:
            x_axis = 0
            for tile in row:
                if tile == "X": # Adding Collidable Walls
                    object = CollisionObject(OBJECT_LENGTH, OBJECT_HEIGHT, x_axis, y_axis)
                    self.camera_group.add(object)
                    self.collision_group.add(object)
                    if player_pos:
                        if player_pos[0] == x_axis:
                            player_falling = False
                elif tile == "S": # Adding the Player Spawn
                    self.player = Player((x_axis, y_axis))
                    self.camera_group.add(self.player)
                    player_pos = (x_axis, y_axis)
                elif tile == "P": # Adding Platforms
                    object = CollisionObject(OBJECT_LENGTH, OBJECT_HEIGHT, x_axis, y_axis, "white")
                    self.camera_group.add(object)
                    self.platform_group.add(object)
                
                x_axis += OBJECT_LENGTH
            y_axis += OBJECT_HEIGHT

        if not player_pos:
            player_pos = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        elif player_falling:
            self.message = Message("PLAYER NOT SET PROPERLY", pygame.font.SysFont(None, 128), (255, 0, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))



    def run(self):
        self.physics_manager.update()
        
        self.display_surface.fill('black')
        self.camera_group.custom_draw(self.player)
        self.display_surface.blit(self.message.image, self.message.rect.topleft)
