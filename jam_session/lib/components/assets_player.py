"""
Tareas pendientes:
* [x] Mover gestión de movimiento desde código anterior
* [ ] Mover gestión de animación desde código anterior
...
"""

from typing import Tuple, Callable, Any

from pygame import locals as pygame_constants

import pygame.sprite

from jam_session.lib.components.event_handler import KeyboardEventAction
from jam_session.lib.components.assets_default import Asset

class Player(Asset):
    """
    """
    MOVE_SPEED = 5

    MOVE_UP = (0,-1)
    MOVE_DOWN = (0,1)
    MOVE_LEFT = (-1, 0)
    MOVE_RIGHT = (1, 0)

    STATUS_MOVE_IDLE = 0
    STATUS_MOVE_ACTIVE = 1

    def __init__(self, *groups: pygame.sprite.AbstractGroup) -> None:
        super().__init__(*groups)
        self.position_update_units = 5
        self.move_direction = Player.MOVE_UP
        self.move_status = Player.STATUS_MOVE_IDLE

    def update_asset_position(self) -> None:
        if self.move_status == Player.STATUS_MOVE_ACTIVE:
            x_update = self.move_direction[0] * self.position_update_units
            y_update = self.move_direction[1] * self.position_update_units 
            self.x += x_update
            self.y += y_update

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.update_asset_position()
        return super().update(*args, **kwargs)

    def get_event_actions(self) -> Tuple[KeyboardEventAction]:
        move_up = KeyboardEventAction(
            key=(pygame_constants.KEYDOWN, pygame_constants.K_UP),
            method_to_call=self.action_move_up,
            target_object=self,
        )
        move_up_halt = KeyboardEventAction(
            key=(pygame_constants.KEYUP, pygame_constants.K_UP),
            method_to_call=self.action_move_stop,
            target_object=self,
        )
        move_down = KeyboardEventAction(
            key=(pygame_constants.KEYDOWN, pygame_constants.K_DOWN),
            method_to_call=self.action_move_down,
            target_object=self,
        )
        move_down_halt = KeyboardEventAction(
            key=(pygame_constants.KEYUP, pygame_constants.K_DOWN),
            method_to_call=self.action_move_stop,
            target_object=self,
        )
        move_left = KeyboardEventAction(
            key=(pygame_constants.KEYDOWN, pygame_constants.K_LEFT),
            method_to_call=self.action_move_left,
            target_object=self,
        )
        move_left_halt = KeyboardEventAction(
            key=(pygame_constants.KEYUP, pygame_constants.K_LEFT),
            method_to_call=self.action_move_stop,
            target_object=self,
        )
        move_right = KeyboardEventAction(
            key=(pygame_constants.KEYDOWN, pygame_constants.K_RIGHT),
            method_to_call=self.action_move_right,
            target_object=self,
        )
        move_right_halt = KeyboardEventAction(
            key=(pygame_constants.KEYUP, pygame_constants.K_RIGHT),
            method_to_call=self.action_move_stop,
            target_object=self,
        )


        return [move_up, move_up_halt, move_down, move_down_halt, move_left, move_left_halt, move_right, move_right_halt]
    

    def set_move_direction(self, direction):
        self.move_direction = direction
        self.current_frame = self.move_status

    def set_move_status(self, status):
        self.move_status =  status
        if self.move_status:
            self.current_frame = self.STATUS_MOVE_IDLE


    def action_move_up(self, *args, **kwargs) -> None:
        """
        Codigo para definir dirección y estado
        """
        self.set_move_direction(self.MOVE_UP)
        self.set_move_status(self.STATUS_MOVE_ACTIVE)

    def action_move_down(self, *args, **kwargs) -> None:
        """
        Codigo para definir dirección y estado
        """
        self.set_move_direction(self.MOVE_DOWN)
        self.set_move_status(self.STATUS_MOVE_ACTIVE)

    def action_move_left(self, *args, **kwargs) -> None:
        """
        Codigo para definir dirección y estado
        """
        self.set_move_direction(self.MOVE_LEFT)
        self.set_move_status(self.STATUS_MOVE_ACTIVE)
    
    def action_move_right(self, *args, **kwargs) -> None:
        """
        Codigo para definir dirección y estado
        """
        self.set_move_direction(self.MOVE_RIGHT)
        self.set_move_status(self.STATUS_MOVE_ACTIVE)
    
    def action_move_stop(self, *args, **kwargs) -> None:
        """
        Codigo para definir dirección y estado
        """
        self.set_move_direction(self.MOVE_UP)
        self.set_move_status(self.STATUS_MOVE_IDLE)


def create_default_player(x: int = 0, y: int = 0) -> Asset:
    default_image = './jam_session/resources/characters/pj.png'
    asset_obj = Player()
    asset_obj.x = x
    asset_obj.y = y
    asset_obj.image = pygame.image.load(default_image)
    asset_obj.setup()

    return asset_obj