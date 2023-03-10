"""
* [-] Copiar código de gestión de eventos del módulo antiguo
* [ ] Añadir add_event_action y gestionarlo
"""
from typing import Tuple, Callable

import pygame.event

class EventAction:
    event_type: Tuple
    event_action: Callable

    def __init__(self, event_type, event_action) -> None:
        pass


class DefaultEventHandler:
    def __init__(self, *args, **kwargs):
        self.event_actions = []
    
    def add_event_action(self, event_action: EventAction) -> None:
        """
        Que ocurre si el evento existe?
        Se puede eliminar un evento cargado?
        """
        self.event_actions.append(event_action)


    def check_events(self):
        for event in pygame.event.get():
            if event.type in self.event_actions:
                if event.key in self.event_actions:
                    # ...
                    pass        