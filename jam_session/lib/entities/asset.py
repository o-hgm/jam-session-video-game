from typing import Any

import pygame
from pygame.sprite import Sprite

class Asset(Sprite):
    """
    An Asset is a Entity which can be draw in a Surface.
    """
    pass
    # Constructor. Pass in the color of the block, and its x and y position
    def __init__(self, *args, **kwargs):
        # Call the parent class (Sprite) constructor
        super(self, Asset).__init__()

        self.position_x = 0
        self.position_y = 0

        self.image = None
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def get_coordinates() -> Tuple[int, int]:
        return self.position_x, self.position_y

    def update(self, *args: Any, **kwargs: Any) -> None:
        return super().update(*args, **kwargs)
    
a = Asset()
