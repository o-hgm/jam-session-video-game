from typing import Any

import pygame.sprite

class Asset(pygame.sprite.Sprite):
    """
    It encapsullates a object painted in a reference position
    """
    def __init__(self, *groups: pygame.sprite.AbstractGroup) -> None:
        super().__init__(*groups)
        self.position_x = 0
        self.position_y = 0

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.rect.x = self.position_x
        self.rect.y = self.position_y
        return super().update(*args, **kwargs)