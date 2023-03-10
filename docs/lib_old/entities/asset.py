from typing import Any, Tuple

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
        super().__init__()

        self.position_x = 0
        self.position_y = 0

    def setup(self, *args, **kwargs) -> None:
        self.rect = self.image.get_rect()
        

    def get_coordinates(self) -> Tuple[int, int]:
        return self.position_x, self.position_y

    def update_rect_position(self) -> None:
        self.rect.center = self.get_coordinates()

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.update_rect_position()
        return super().update(*args, **kwargs)
    

def from_image_resource(img_path: str, x_origin: int = 0, y_origin: int = 0) -> Asset:
    asset_obj = Asset()
    asset_obj.position_x = x_origin
    asset_obj.position_y = y_origin
    asset_obj.image = pygame.image.load(img_path)
    asset_obj.setup()

    return asset_obj