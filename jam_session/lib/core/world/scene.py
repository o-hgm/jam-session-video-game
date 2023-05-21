import pygame


class Scene:
    """
    A Scene represents a delimited Area in the game world.
    A Scene is conformed by:
    + A background surface
    + A collide layer
    + A collection of Assets rendered
    + A collection of No Controlled Players
    """
    def __init__(self, ui_manager) -> None:
        self.ui_surface: pygame.Surface = None
        
        self.layer_background: pygame.Surface = None # Sprite or Resource to Blitz
        self.layer_collision: pygame.Surface = None # Task: How to handle collision layer for rpg games
        
        self.layer_objects = pygame.sprite.Group()
    

    def set_bg_from_path(self, bg_path: str) -> None:
        self.layer_background = pygame.image.load(bg_path).convert_alpha()
    
    def add_game_object(self, obj) -> None:
        self.layer_objects.add(obj)

    def set_bg_collision_from_path(self, wall_path: str) -> None:
        self.layer_collision = pygame.image.load(wall_path).convert_alpha()
        self.layer_collision_mask = pygame.mask.from_surface(self.layer_collision)
    