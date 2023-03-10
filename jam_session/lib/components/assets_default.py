from typing import Any

import pygame.sprite

class Asset(pygame.sprite.Sprite):
    """
    It encapsullates a object painted in a reference position
    """
    def __init__(self, *groups: pygame.sprite.AbstractGroup) -> None:
        super().__init__(*groups)
        self.x = 0
        self.y = 0

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.rect.x = self.x
        self.rect.y = self.y
        return super().update(*args, **kwargs)