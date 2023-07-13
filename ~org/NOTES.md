#!/usr/bin/env python
import pygame
import pygame
from pygame.locals import *

import sys

default_game_title = "This is an example game"
default_width = 640
default_height = 250

def initialize_game_surface(title = default_game_title, width = default_width, height = default_height) -> pygame.Surface:
    pygame.init()
    pygame.display.set_caption(title)
    
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))

    return screen, clock

def render_scroll_background_list(game_display, bg_list, scroll_x, scroll_y, scroll_direction_right = False):
    for bg in bg_list:
        background_position_base = (scroll_x, scroll_y)
        background_position_overflow = (scroll_x - default_width, 0)
        game_display.blit(bg, background_position_base)
        game_display.blit(bg, background_position_overflow)



if __name__ == '__main__':
    position_x = 0
    position_y = 0

    speed_x = 1
    speed_y = 0

    game_display, game_clock = initialize_game_surface()
    background_resources = [pygame.image.load(f"./resources/grey_L{index}.png") for index in range(1, 5)]
    while True:
        game_clock.tick(60)
        position_x += speed_x

        # Restart the render
        if position_x >= default_width:
            position_x = 0
        elif position_x <= 0:
            position_x = default_width

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                
                if event.key == K_LEFT:
                    speed_x += 1
                if event.key == K_RIGHT:
                    speed_x -= 1

        render_scroll_background_list(
            game_display=game_display, 
            bg_list=background_resources, 
            scroll_x=position_x, 
            scroll_y=position_y
        )
        
        pygame.display.update()
        