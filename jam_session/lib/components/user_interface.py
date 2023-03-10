import pygame
import pygame.sprite


class DefaultUserInterface:
    DEFAULT_COLOR = (0,0,0)

    def __init__(self, ui_width: int = 800, ui_height: int = 800) -> None:
        self.ui_surface = pygame.Surface()
        self.layer_background = None # Sprite or Resource to Blitz
        self.layer_collision = None # Task: How to handle collision layer for rpg games
        self.layer_objects = pygame.sprite.Group()
        self.layer_characters = pygame.sprite.Group()

    def draw(self):
        self.ui_surface.fill(self.DEFAULT_COLOR)
        self.ui_surface.blit(self.layer_background)
        # How to collide
        self.layer_objects.draw(self.ui_surface)
        self.layer_characters.draw(self.ui_surface)