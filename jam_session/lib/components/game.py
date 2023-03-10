from typing import List

import pygame
import pygame.sprite
from jam_session.lib.components.assets_player import Player

from jam_session.lib.components.event_handler import DefaultEventHandler
from jam_session.lib.components.user_interface import DefaultUserInterface
from jam_session.lib.components.assets_default import Asset


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

    def run_game(self) -> None:
        self.is_running = True
        while self.is_running:
            self.event_handler.check_events()
            self.object_list.update()
            self.game_interface.draw()
            self.game_clock.tick(self.frame_rate)

    def set_player(self, player_obj: Player) -> None:
        self.object_list.append(player_obj)
        self.event_handler.add_event_actions(*player_obj.get_event_actions())
        self.game_interface.add_asset(player_obj)
        
        # ... All the logic required to set-up a Player instance as an Active Player.

    def add_player_npc(self, npc_obj: Npc) -> None:
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
    player_obj = None
    game_instance.set_player(player_obj)
    # ... Carga de Nivel (Lo que signifique eso ...)

    return game_instance
