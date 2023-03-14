"""
* [-] Copiar código de gestión de eventos del módulo antiguo
* [ ] Añadir add_event_action y gestionarlo
"""
from collections import defaultdict
from typing import Any, Iterable, Tuple, Callable

import pygame.event

class EventAction:
    pass

class KeyboardEventAction(EventAction):
    """
    Represents something to do when system detects that a key combination has been pressed
    """
    KEY_EMPTY = (None, None)
    
    key: Tuple
    target_object: Any
    method_to_call: Callable
    event_context: dict

    def __init__(self, *args, **kwargs) -> None:
        try:
            self.key = kwargs['key']
            self.method_to_call = kwargs['target_method']
            self.target_object = kwargs.get('target_object')
            self.event_context = kwargs.get('event_context', dict())
        except KeyError as e:
            raise AttributeError('KeyboardEventHandler must include attribute %s' % e)

    def __repr__(self) -> str:
        f"KeyboardEventHandler[Key={self.key}] => {self.method_to_call}"
    
    def __str__(self) -> str:
        return f"Event {self.key} calls to {self.method_to_call}"
    

class DefaultEventHandler:
    def __init__(self, *args, **kwargs):
        self.event_actions = defaultdict(defaultdict)
    
    def add_event_actions(self, *event_actions: Iterable[EventAction]) -> None:
        """
        Que ocurre si el evento existe?
        Se puede eliminar un evento cargado?
        """
        for event_action in event_actions:
            event_type = event_action.key[0]
            event_key = event_action.key[1]
            if event_type in self.event_actions and event_key in self.event_actions[event_type]:
                    self.event_actions[event_type][event_key].append(event_action)
            else:
                self.event_actions[event_type][event_key] = [event_action]


    def check_events(self):
        event: pygame.event.Event

        for event in pygame.event.get():
            if event.type in self.event_actions:
                key_value = getattr(event, 'key', None)
                if key_value in self.event_actions[event.type]:
                    event_list = self.event_actions[event.type][key_value]
                    for event_obj in event_list:
                        event_obj.method_to_call()