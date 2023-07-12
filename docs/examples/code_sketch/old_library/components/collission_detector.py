from typing import List

import pygame

from jam_session.lib.components.user_interface import DefaultUserInterface
from jam_session.lib.components.assets_npc import NoPlayerCharacter
from jam_session.lib.components.assets_default import Asset


class CollisionDetector():
    ui: DefaultUserInterface

    def __init__(self, *args, **kwargs) -> None:
        self.ui = args[0] if args else kwargs.get('ui', None)

    def is_character_hit_wall(self) -> List[Asset]:
        result_list = []
        for img in self.layer_characters.sprites():
            mask = pygame.mask.from_surface(img.image)
            offset = img.rect.x - self.layer_collision.get_rect().x, img.rect.y - self.layer_collision_mask.get_rect().y

            if self.layer_collision_mask.overlap(mask, offset=offset):
                result_list.append(img)
        
        return result_list

    def is_character_hit_npc(self) -> List[NoPlayerCharacter]:
        result_list = []
        for img in self.ui.layer_characters.sprites():
            collide_sprite = pygame.sprite.spritecollideany(img, self.ui.layer_characters)
            mask = pygame.mask.from_surface(img.image)
            offset = img.rect.x - self.layer_collision.get_rect().x, img.rect.y - self.layer_collision_mask.get_rect().y

            if self.layer_collision_mask.overlap(mask, offset=offset):
                result_list.append(img)
        
        return result_list
    
    def is_character_hit_object(self) -> List[Asset]:
        return []
    