from typing import List

import pygame
import pygame.sprite
from pygame import locals as pygame_constants

from jam_session.lib.components import assets_default
from jam_session.lib.components.assets_default import Asset
from jam_session.lib.components.assets_player import Player
from jam_session.lib.components.assets_npc import NoPlayerCharacter

from jam_session.lib.components.event_handler import DefaultEventHandler, KeyboardEventAction
from jam_session.lib.components.user_interface import DefaultUserInterface


class Game:
    """
    Class Game:
    It maintains the game loop running and updates all elements of the display.
    It relies on Event Handler to check all the possible events and uses UserInterface 
    abstraction to perform the draw loop. It includes all the graphic elements into a 
    Graphic Group to ensure are properly updated.

    """
    def __init__(self) -> None:
        self.event_handler: DefaultEventHandler = None
        self.game_interface: DefaultUserInterface = None
        self.object_list: List[Asset] = []
        self.game_clock = pygame.time.Clock() 
        self.group_container: pygame.sprite.Group = pygame.sprite.Group()
        self.is_running = False
        self.frame_rate = 30

    def start(self) -> None:
        self.is_running = True
        self.game_interface.initialize()
        while self.is_running:
            self.event_handler.check_events()
            self.group_container.update()
            self.game_interface.draw()
            self.game_clock.tick(self.frame_rate)

    def stop(self)-> None:
        self.is_running = False

    def include_asset(self, asset_obj: Asset) -> None:
        self.object_list.append(asset_obj)
        self.game_interface.include_object(asset_obj)


    def set_player(self, player_obj: Player) -> None:
        self.object_list.append(player_obj)
        self.event_handler.add_event_actions(*player_obj.get_event_actions())
        self.game_interface.add_asset(player_obj)

        # ... All the logic required to set-up a Player instance as an Active Player.

    def add_player_npc(self, npc_obj: NoPlayerCharacter) -> None:
        pass



def create_game() -> Game:
    """
    This factory create and wire all the required items.
    """
    game_instance = Game()
    # Choose elements to handle game loop
    game_instance.event_handler = DefaultEventHandler()
    game_instance.game_interface = DefaultUserInterface()
    # ... Carga de Jugador (Lo que signifique eso ...)
    # player_obj = create_player_from_sprite("./resources/.../...")

    game_instance.event_handler.add_event_actions(
        KeyboardEventAction(
            key=(pygame_constants.QUIT, None),
            target_method=lambda: game_instance.stop() and pygame.quit()
        )
    )
    game_instance.event_handler.add_event_actions(
        KeyboardEventAction(
            key=(pygame_constants.KEYUP, pygame_constants.K_q),
            target_method=lambda: game_instance.stop() and pygame.quit()
        )
    )

    game_instance.game_interface.set_background('./jam_session/resources/backgrounds/bg_office.png')
    asset_obj = assets_default.from_image_resource('./jam_session/resources/characters/pj.png', x=400, y=400)
    if asset_obj:
        game_instance.include_asset(asset_obj=asset_obj)

    player_obj = None
    if player_obj:
        game_instance.set_player(player_obj)
    
    # ... Carga de Nivel (Lo que signifique eso ...)

    return game_instance
