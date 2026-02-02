import pygame

class PhysicsManager:
    def __init__(self, collision_group):
        self.entity_list = []
        self.collision_group = collision_group

    def update(self):
        for entity in self.entity_list:
            entity.jump()
            self.vertical_collision(entity)
            self.horizontal_collision(entity)
            

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
        
        # Reset on_wall status before checking collisions
        if hasattr(entity, 'on_wall'):
            entity.on_wall = False

        for collidable in collidable_sprites:
            collidable.horizontal_collision(entity)
            
        # Apply wall hold logic once after all collisions are checked
        if hasattr(entity, 'on_wall'):
            entity.wall_hold() 

    def vertical_collision(self, entity):
        entity.apply_gravity()
        collidable_sprites = self.collision_group.sprites()
        for collidable in collidable_sprites:
            collidable.vertical_collision(entity)

    # def wall_check(self, entity):
    #     if not hasattr(entity, 'on_wall'):
    #         return
    #     entity.wall_hold()
    #     temp_rect_left = pygame.Rect(entity.rect.x-1, entity.rect.y, 1,entity.height)
    #     temp_rect_right = pygame.Rect(entity.rect.x+1, entity.rect.y, 1,entity.height)

    #     for sprite in self.collision_group.sprites():
    #         if sprite.wall_holdable:
    #             if (sprite.rect.colliderect(temp_rect_left) or sprite.rect.colliderect(temp_rect_right)) and entity.direction.y != 0:
    #                 if (not entity.on_wall):
    #                     entity.direction.y = 0
    #                 entity.on_wall = True
    #                 return
    #     entity.on_wall = False