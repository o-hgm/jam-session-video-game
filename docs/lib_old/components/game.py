from collections import defaultdict
from typing import Any, Callable, Tuple

import pygame
from pygame.locals import *

import sys

from .game_interface import GameInterface

class Game:
    """
    A Game instance the components of the game and controls the application flow.

    Game contains a UI. This UI is responsible of painting and check interaction with 
    Any graphical content.

    A game run on Levels. A Level encapsullates the requirements and the goals of a game.

    
    """
    GAME_TITLE = 'Late Again: The Game'
    DEFAULT_WIDTH = 640
    DEFAULT_HEIGHT = 250

    @staticmethod
    def get_default() -> "Game":
        game_obj = Game()

        how_to_quit = lambda kwargs: game_obj.end_game_loop()

        game_obj.game_ui = GameInterface()
        game_obj.register_keyboard_event(
            key=(pygame.QUIT, None),
            target_object=game_obj,
            event_context={},
            target_method=how_to_quit
        )
        game_obj.register_keyboard_event(
            key=(pygame.KEYDOWN, pygame.K_q),
            target_object=game_obj,
            event_context={},
            target_method=how_to_quit
        )
        return game_obj


    game_interface: GameInterface = None

    def __init__(self) -> None:
        self.run_loop = True
        self.game_ui = None
        self.game_clock = None
        self.game_surface = None

        self.keyboard_events = defaultdict(list)

    def __bootstrap_game(self):
        pygame.init()
        pygame.display.set_caption(Game.GAME_TITLE)

        self.game_clock   = pygame.time.Clock()

    def __initialize_game_interface(self):
        self.game_surface = pygame.display.set_mode((Game.DEFAULT_WIDTH, Game.DEFAULT_HEIGHT))
        self.game_ui.set_screen(self.game_surface)
        self.game_ui.configure()

    def __teardown_game(self):
        pygame.quit()
        sys.exit()

    def start(self):
        self.__bootstrap_game()
        while self.run_loop:
            self.handle_keyboard_events()
            self.draw_game_ui()
        
        self.__teardown_game()


    def draw_game_ui(self) -> None:
        pass

    def register_keyboard_event(self, key: Tuple, target_object: Any, target_method: Callable, event_context: dict) -> "KeyboardEventHandler":
        """
        Register a keyboard event in game loop
        """
        keyboard_event_handler = KeyboardEventHandler(
            key=key,
            target_object=target_object,
            target_method=target_method,
            event_context=event_context
        )
        self.keyboard_events[key].append(keyboard_event_handler)

        return keyboard_event_handler

    def handle_keyboard_events(self) -> None:
        """
        Game object controls keyboard event loop. Components will register events
        using register_keyboard_event.
        """
        for event in pygame.event.get():
            event_key = getattr(event, 'key', None)
            keyboard_event_generic = (event.type, None)
            keyboard_event_detail = (event.type, event_key)

            keyboard_event: KeyboardEventHandler
            # Handle Type Events
            for keyboard_event in self.keyboard_events.get(keyboard_event_generic, list()):
                keyboard_event.method_to_call(kwargs=keyboard_event.event_context)
            
            # Handle Type, Key Events. If to avoid double call
            if event_key:
                for keyboard_event in self.keyboard_events.get(keyboard_event_detail, list()):
                    keyboard_event.method_to_call(kwargs=keyboard_event.event_context)
            
            if event.type == pygame.QUIT:
                self.run_loop = False

    def end_game_loop(self):
        self.run_loop = False

class KeyboardEventHandler:
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