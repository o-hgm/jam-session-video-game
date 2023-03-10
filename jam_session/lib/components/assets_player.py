from typing import Tuple, Callable

from pygame import locals as pygame_constants


from jam_session.lib.components.assets_default import Asset

class EventAction:
    event_type: Tuple
    event_action: Callable

    def __init__(self, event_type, event_action) -> None:
        pass

class Player(Asset):
    def get_event_actions(self) -> Tuple[EventAction]:
        move_up = EventAction(
            event_type=(pygame_constants.KEYDOWN, pygame_constants.K_UP),
            event_action=self.set_move_up
        )
        move_halt=EventAction(
            event_type=(pygame_constants.KEYUP, pygame_constants.K_UP),
            event_action=self.set_move_stop
        )

        return [move_up, move_halt]
    
    def set_move_up(self):
        """
        Codigo para definir dirección y estado
        """
        pass


    def set_move_stop(self):
        """
        Codigo para definir dirección y estado
        """
        pass