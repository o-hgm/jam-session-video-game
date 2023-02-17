import pygame
from pygame.locals import *

import sys

from jam_session.lib.pygame_utils.game_state import quit_game


keyup_event_dict = {
    K_ESCAPE: quit_game
}


def keyboard_event_loop():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            trigger_function = keyup_event_dict.get(event.key) 
            if trigger_function:
                trigger_function()