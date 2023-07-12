from typing import List

import pygame
import pygame.sprite
from pygame import locals as pygame_constants

from jam_session.lib.components import assets_default, assets_player
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
        self.game_clock = pygame.time.Clock() 
        self.group_container: pygame.sprite.Group = pygame.sprite.Group()
        self.is_running = False
        self.frame_rate = 30

    def start(self) -> None:
        self.is_running = True
        while self.is_running:
            for item in self.game_interface.is_character_hit_wall():
                item.has_collision = True
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
        self.group_container.add(player_obj)
        player_actions = player_obj.get_event_actions()
        self.event_handler.add_event_actions(*player_actions)
        self.game_interface.layer_characters.add(player_obj)

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
    game_instance.game_interface.initialize()

    game_instance.event_handler.add_event_actions(
        KeyboardEventAction(
            key=(pygame_constants.QUIT, None),
            method_to_call=lambda: game_instance.stop() and pygame.quit()
        )
    )
    game_instance.event_handler.add_event_actions(
        KeyboardEventAction(
            key=(pygame_constants.KEYUP, pygame_constants.K_q),
            method_to_call=lambda: game_instance.stop() and pygame.quit()
        )
    )

    game_instance.game_interface.set_background('./jam_session/resources/places/main_office/bg_office.png')
    game_instance.game_interface.set_wall('./jam_session/resources/places/main_office/bg_wall.png')
    player_obj = assets_player.create_default_player(200, 200)
    if player_obj:
        game_instance.set_player(player_obj)
    
    # ... Carga de Nivel (Lo que signifique eso ...)

    return game_instance
