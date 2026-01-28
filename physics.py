import pygame

class PhysicsManager:
    def __init__(self, player, collision_group, platform_group):
        self.player = player
        self.collision_group = collision_group
        self.platform_group = platform_group

    def update(self):
        self.player.jump()
        self.horizontal_collision()
        self.vertical_collision()
        self.wall_check()

    def horizontal_collision(self):
        self.player.move()
        collidable_sprites = self.collision_group.sprites()
        
        for sprite in collidable_sprites:
            if sprite.rect.colliderect(self.player.rect):
                if self.player.direction.x < 0: # Moving Left
                    self.player.rect.left = sprite.rect.right
                elif self.player.direction.x > 0: # Moving Right
                    self.player.rect.right = sprite.rect.left    

    def vertical_collision(self):
        self.player.apply_gravity()
        collidable_sprites = self.collision_group.sprites()
        
        for sprite in collidable_sprites:
            if sprite.rect.colliderect(self.player.rect):
                if self.player.direction.y > 0: # Falling Down
                    self.player.rect.bottom = sprite.rect.top
                    self.player.direction.y = 0
                    self.player.jumps = 2 # Reset Jumps Logic
                elif self.player.direction.y < 0: # Jumping Up
                    self.player.rect.top = sprite.rect.bottom
                    self.player.direction.y = 0 # Bonk head, stop moving up

        for sprite in self.platform_group:
            temp_player_bottom = pygame.Rect(self.player.rect.x, self.player.rect.bottom-1, self.player.width, 1)
            if sprite.rect.colliderect(temp_player_bottom):
                if self.player.direction.y > 0: # Falling Down
                    self.player.rect.bottom = sprite.rect.top
                    self.player.direction.y = 0
                    self.player.jumps = 2

    def wall_check(self):
        self.player.wall_hold()
        temp_rect_left = pygame.Rect(self.player.rect.x-1, self.player.rect.y, 1,self.player.height)
        temp_rect_right = pygame.Rect(self.player.rect.x+1, self.player.rect.y, 1,self.player.height)

        for sprite in self.collision_group.sprites():
            if (sprite.rect.colliderect(temp_rect_left) or sprite.rect.colliderect(temp_rect_right)) and self.player.direction.y != 0:
                if (not self.player.on_wall):
                    self.player.direction.y = 0
                self.player.on_wall = True
                return
        self.player.on_wall = False