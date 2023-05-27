import pygame
from pygame.locals import *

import sys

default_game_title = "This is an example game"
default_width = 640
default_height = 250

def initialize_game_surface(title = default_game_title, width = default_width, height = default_height) -> pygame.Surface:
    pygame.display.set_caption(title)
    
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))

    return screen, clock

