import pygame

class PhysicsManager:
    def __init__(self, collision_group, platform_group):
        self.entity_list = []
        self.collision_group = collision_group
        self.platform_group = platform_group

    def update(self):
        for entity in self.entity_list:
            entity.jump()
            self.horizontal_collision(entity)
            self.vertical_collision(entity)
            self.wall_check(entity)

    def add_entity(self, entity):
        try:
            print(f"Physics Manager: Attempting to add {entity.name}!")
            self.entity_list.append(entity)
            print(f"Physics Manager: Added {entity.name} successfully!")
        except AttributeError:
            print("Physics Manager: Invalid Entity Added (Entity has no name!)")
        
    def remove_entity(self, entity):
        try:
            self.entity_list.remove(entity)
            print(f"Physics Manager: {entity} removed successfully!")
        except:
            print(f"Physics Manager: {entity} could not be removed (Entity not found!)")

    def horizontal_collision(self, entity):
        entity.move()
        collidable_sprites = self.collision_group.sprites()
        
        for sprite in collidable_sprites:
            if sprite.rect.colliderect(entity.rect):
                if entity.direction.x < 0: # Moving Left
                    entity.rect.left = sprite.rect.right
                elif entity.direction.x > 0: # Moving Right
                    entity.rect.right = sprite.rect.left    

    def vertical_collision(self, entity):
        entity.apply_gravity()
        collidable_sprites = self.collision_group.sprites()
        
        for sprite in collidable_sprites:
            if sprite.rect.colliderect(entity.rect):
                if entity.direction.y > 0: # Falling Down
                    entity.rect.bottom = sprite.rect.top
                    entity.direction.y = 0
                    entity.jumps = 2 # Reset Jumps Logic
                elif entity.direction.y < 0: # Jumping Up
                    entity.rect.top = sprite.rect.bottom
                    entity.direction.y = 0 # Bonk head, stop moving up

            for sprite in self.platform_group:
                temp_entity_bottom = pygame.Rect(entity.rect.x, entity.rect.bottom+1, entity.width, 1)
                if sprite.rect.colliderect(temp_entity_bottom):
                    if entity.direction.y > 0: # Falling Down
                        entity.rect.bottom = sprite.rect.top
                        entity.direction.y = 0
                        entity.jumps = 2

    def wall_check(self, entity):
        if not hasattr(entity, 'on_wall'):
            return
        entity.wall_hold()
        temp_rect_left = pygame.Rect(entity.rect.x-1, entity.rect.y, 1,entity.height)
        temp_rect_right = pygame.Rect(entity.rect.x+1, entity.rect.y, 1,entity.height)

        for sprite in self.collision_group.sprites():
            if (sprite.rect.colliderect(temp_rect_left) or sprite.rect.colliderect(temp_rect_right)) and entity.direction.y != 0:
                if (not entity.on_wall):
                    entity.direction.y = 0
                entity.on_wall = True
                return
        entity.on_wall = False