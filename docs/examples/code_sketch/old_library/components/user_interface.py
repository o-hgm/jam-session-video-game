from typing import List, Tuple
import pygame
import pygame.sprite

import pygame_gui

from jam_session.lib.components.assets_default import Asset


class DefaultUserInterface:
    DEFAULT_COLOR = (0,0,0)

    def __init__(self, ui_width: int = 800, ui_height: int = 800) -> None:
        self.ui_width = ui_width
        self.ui_height = ui_height

        self.ui_manager = None # pygame_gui.UIManager((self.ui_width, self.ui_height), "theme.json")

        self.text_action_panel = None # 

        self.ui_surface: pygame.Surface = None
        
        self.layer_background: pygame.Surface = None # Sprite or Resource to Blitz
        self.layer_collision: pygame.Surface = None # Task: How to handle collision layer for rpg games
        
        self.layer_objects = pygame.sprite.Group()
        self.layer_characters = pygame.sprite.Group()

    def get_size(self) -> Tuple[int, int]:
        return (self.ui_width, self.ui_height)

    def initialize(self) -> None:
        pygame.init()
        self.ui_surface = pygame.display.set_mode(self.get_size())
        self.ui_manager = pygame_gui.UIManager((self.ui_width, self.ui_height), "theme.json")

        self.text_action_panel = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(
                (0, 300),
                (100, 100),
            ),
            starting_layer_height=1,
            manager=self.ui_manager,
        )


    def set_background(self, bg_path: str) -> None:
        self.layer_background = pygame.image.load(bg_path).convert_alpha()
    
    def include_object(self, obj) -> None:
        self.layer_objects.add(obj)

    def set_wall(self, wall_path: str) -> None:
        self.layer_collision = pygame.image.load(wall_path).convert_alpha()
        self.layer_collision_mask = pygame.mask.from_surface(self.layer_collision)
    
    def is_character_hit_wall(self) -> List[Asset]:
        result_list = []
        for img in self.layer_characters.sprites():
            mask = pygame.mask.from_surface(img.image)
            offset = img.rect.x - self.layer_collision.get_rect().x, img.rect.y - self.layer_collision_mask.get_rect().y

            if self.layer_collision_mask.overlap(mask, offset=offset):
                result_list.append(img)
        
        return result_list

    
    def draw(self):
        self.ui_surface.fill(self.DEFAULT_COLOR)
        if self.layer_background:
            self.ui_surface.blit(self.layer_background, self.layer_background.get_rect())
        # How to collide
        self.layer_objects.draw(self.ui_surface)
        self.layer_characters.draw(self.ui_surface)
        pygame.display.update()
        
