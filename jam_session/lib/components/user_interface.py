import pygame
import pygame.sprite


class DefaultUserInterface:
    DEFAULT_COLOR = (0,0,0)

    def __init__(self, ui_width: int = 800, ui_height: int = 800) -> None:
        self.ui_surface = pygame.Surface()
        self.ui_group = pygame.sprite.Group()

    def draw(self):
        self.ui_surface.fill(self.DEFAULT_COLOR)
        self.ui_group.draw(self.ui_surface)