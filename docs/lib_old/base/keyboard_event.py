from jam_session.lib.entities.player import Player
import pygame
from pygame.locals import *

import sys

from jam_session.lib.pygame_utils.game_state import quit_game


keyup_event_dict = {
    K_ESCAPE: quit_game
}


def keyboard_event_loop(player : Player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.key == pygame.KEYDOWN:
            player.set_move_direction(Player.MOVE_DOWN)
        elif event.key == pygame.KEYUP:
            player.set_move_direction(Player.MOVE_UP)
        elif event.key == pygame.KEYRIGHT:
            player.set_move_direction(Player.MOVE_RIGHT)
        elif event.key == pygame.KEYLEFT:
            player.set_move_direction(Player.MOVE_LEFT)
        