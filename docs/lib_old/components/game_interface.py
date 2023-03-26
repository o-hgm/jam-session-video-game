from typing import List

from pygame import Surface
from pygame.sprite import Sprite


class GameInterface:
    """
    A Game Interface is responsible for draw all the elements into a surface.
    Its refactored by game state
    """
    game_window: Surface
    objects: List[Sprite]

    def __init__(self) -> None:
        self.screen_surface: Surface = None
        self.objects: List[Sprite] = []

    def set_screen(self, screen_surface: Surface) -> None:
        self.screen_surface = screen_surface
    
    def configure(self) -> None:
        """
        It creates the User Interface
        """
        pass