from typing import Any, Tuple

import pygame
from pygame.sprite import Sprite

from jam_session.settings import WINDOW_WIDTH, WINDOW_HEIGHT


class Asset(Sprite):
    """
    An Asset is a Entity which can be draw in a Surface.
    """

    @staticmethod
    def from_image_resource(img_path: str, x_origin: int = 0, y_origin: int = 0) -> "Asset":
        asset_obj = Asset()
        asset_obj.position_x = x_origin
        asset_obj.position_y = y_origin
        asset_obj.image = pygame.image.load(img_path)
        asset_obj.initialize()

        return asset_obj

    # Constructor. Pass in the color of the block, and its x and y position
    def __init__(self, *args, **kwargs):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.position_x = 0
        self.position_y = 0

    def initialize(self, *args, **kwargs) -> None:
        self.rect = self.image.get_rect()
        

    def get_coordinates(self) -> Tuple[int, int]:
        return self.position_x, self.position_y

    def update_rect_position(self) -> None:
        self.rect.center = self.get_coordinates()

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.update_rect_position()
        return super().update(*args, **kwargs)


class ScrollingAsset(Asset):
    """
    This asset scrolls
    """
    DEFAULT_SPEED_X = 10
    DEFAULT_SPEED_Y = 10

    @staticmethod
    def from_image_resource(
        img_path: str, 
        x_origin: int = 0, y_origin: int = 0, 
        x_speed: int = DEFAULT_SPEED_X, y_speed: int = DEFAULT_SPEED_Y,
        screen_width: int = WINDOW_WIDTH, screen_height: int = WINDOW_HEIGHT) -> "ScrollingAsset":
        asset_obj = ScrollingAsset()
        asset_obj.position_x = x_origin
        asset_obj.position_y = y_origin
        asset_obj.scroll_x = x_speed
        asset_obj.scroll_y = y_speed
        asset_obj.screen_limit_x = screen_width,

        asset_obj.image = pygame.image.load(img_path)
        asset_obj.initialize()

        return asset_obj

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scroll_x = 0
        self.scroll_y = 0
        self.screen_limit_x = 0
        self.screen_limit_y = 0

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.position_x += self.scroll_x
        self.position_y += self.scroll_y
    
        return super().update(*args, **kwargs)
    