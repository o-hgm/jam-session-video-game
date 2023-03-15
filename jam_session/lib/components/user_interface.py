from typing import Tuple
import pygame
import pygame.sprite


class DefaultUserInterface:
    DEFAULT_COLOR = (0,0,0)

    def __init__(self, ui_width: int = 800, ui_height: int = 800) -> None:
        self.ui_width = ui_width
        self.ui_height = ui_height

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

    def set_background(self, bg_path: str) -> None:
        self.layer_background = pygame.image.load(bg_path)
    def include_object(self, obj) -> None:
        self.layer_objects.add(obj)

    def draw(self):
        self.ui_surface.fill(self.DEFAULT_COLOR)
        if self.layer_background:
            self.ui_surface.blit(self.layer_background, self.layer_background.get_rect())
        # How to collide
        self.layer_objects.draw(self.ui_surface)
        self.layer_characters.draw(self.ui_surface)
        pygame.display.update()
        
