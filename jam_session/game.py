#!/usr/bin/env python
import pygame

from jam_session.lib.pygame_utils.create_surface import initialize_game_surface
from jam_session.lib.base.keyboard_event import keyboard_event_loop

from jam_session.settings import WINDOW_HEIGHT, WINDOW_WIDTH


def start_game():
    game_surface, game_clock = initialize_game_surface(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

    asset_scene_start_game_title = pygame.image.load('./jam_session/resources/sprites/scene_start_game_title.png')

    asset_position_x = (WINDOW_WIDTH - asset_scene_start_game_title.get_width())/2
    asset_position_y = (WINDOW_WIDTH - asset_scene_start_game_title.get_height())/2

    game_surface.blit(asset_scene_start_game_title, (asset_position_x, asset_position_y))



    while True:
        """ game_surface.fill(), rect=None, special_flags=0) """
        game_clock.tick(60)
        keyboard_event_loop()
        pygame.display.update()
        asset_position_x, asset_position_y = pj_move(game_surface, asset_position_x, asset_position_y)


if __name__ == "__main__":
    start_game()

def pj_move(game_surface, position_x, position_y):
    asset_pj = pygame.image.load('./jam_session/resources/characters/pj.png')
    color_fondo = (0, 0, 0)
    velocidad = 5

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        position_x -= velocidad

    if teclas[pygame.K_RIGHT]:
        position_x += velocidad

    if teclas[pygame.K_UP]:
        position_y -= velocidad

    if teclas[pygame.K_DOWN]:
        position_y += velocidad

    # Actualizar la pantalla con el color de fondo
    game_surface.fill(color_fondo)
    # Dibujar la imagen en la pantalla
    game_surface.blit(asset_pj, (position_x, position_y))
    # Actualizar la pantalla
    pygame.display.update()
    return position_x, position_y
