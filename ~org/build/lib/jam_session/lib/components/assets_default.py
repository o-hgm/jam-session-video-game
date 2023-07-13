from typing import Any, Tuple

import pygame.sprite

class Asset(pygame.sprite.Sprite):
    """
    It encapsullates a object painted in a reference position
    """
    def __init__(self, x: int = 0, y: int = 0, *groups: pygame.sprite.AbstractGroup) -> None:
        super().__init__(*groups)
        self.x = x
        self.y = y
        self.has_collision = False

    def setup(self, *args, **kwargs) -> None:
        self.rect = self.image.get_rect()
        self.update_rect_position()

    def get_coordinates(self) -> Tuple[int, int]:
        return self.x, self.y

    def update_rect_position(self) -> None:
        self.rect.center = self.get_coordinates()

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.update_rect_position()
        return super().update(*args, **kwargs)


def from_image_resource(img_path: str, x: int = 0, y: int = 0) -> Asset:
    asset_obj = Asset()
    asset_obj.x = x
    asset_obj.y = y
    asset_obj.image = pygame.image.load(img_path)
    asset_obj.setup()

    return asset_obj