"""
Tareas pendientes:
* [x] Mover gestión de movimiento desde código anterior
* [ ] Mover gestión de animación desde código anterior
...
"""

from typing import Tuple, Callable

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
        self.velocity = 5
        self.move_direction = Player.MOVE_UP
        self.move_status = Player.STATUS_MOVE_IDLE

    def get_event_actions(self) -> Tuple[KeyboardEventAction]:
        move_up = KeyboardEventAction(
            key=(pygame_constants.KEYDOWN, pygame_constants.K_UP),
            method_to_call=self.action_move_up,
            target_object=self,
        )
        move_halt=KeyboardEventAction(
            key=(pygame_constants.KEYUP, pygame_constants.K_UP),
            method_to_call=self.action_move_stop,
            target_object=self,
        )

        return [move_up, move_halt]
    

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


    def action_move_stop(self, *args, **kwargs) -> None:
        """
        Codigo para definir dirección y estado
        """
        pass