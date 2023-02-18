#!/usr/bin/env python
import pygame

from jam_session.lib.pygame_utils.create_surface import initialize_game_surface
from jam_session.lib.base.keyboard_event import keyboard_event_loop

from jam_session.settings import WINDOW_HEIGHT, WINDOW_WIDTH

class Asset:
    pass

class AnimatedAsset(Asset):
    pass

"""
 asset_scene_start_game_title = pygame.image.load('./jam_session/resources/sprites/scene_start_game_title.png')
    asset_scene_start_game_new_game = pygame.image.load('./jam_session/resources/sprites/scene_start_game_new_game.png')

    asset_position_title_x = (WINDOW_WIDTH - asset_scene_start_game_title.get_width())/2
    asset_position_title_y = (WINDOW_WIDTH - asset_scene_start_game_title.get_height())/2

    game_surface.blit(asset_scene_start_game_title, (asset_position_title_x, asset_position_title_y))

    asset_offset_y = 100
    asset_position_x = (WINDOW_WIDTH - asset_scene_start_game_new_game.get_width())/2
    asset_position_y = asset_offset_y + (WINDOW_WIDTH - asset_scene_start_game_new_game.get_height())/2

    game_surface.blit(asset_scene_start_game_new_game, (asset_position_x, asset_position_y))

    game_surface.blit(asset_scene_start_game_title, (asset_position_x, asset_position_y))

    from jam_session.lib.entities import asset
    asset_example = asset.from_image_resource('./jam_session/resources/sprites/scene_start_game_title.png', y_origin=200)
    asset_groups = pygame.sprite.Group()
    
    asset_groups.add(asset_example)

    while True:
        keyboard_event_loop()
        game_surface.fill((0,0,0))
        
        asset_groups.update()
        asset_groups.draw(game_surface)

        game_clock.tick(4)
        pygame.display.update()


    while True:
         game_surface.fill(), rect=None, special_flags=0)
        game_clock.tick(60)
        keyboard_event_loop()
        pygame.display.update()
        asset_position_x, asset_position_y = pj_move(game_surface, asset_position_x, asset_position_y)
    from itertools import cycle

    asset_animation = [asset_scene_start_game_new_game, None]
    asset_animation_iterator = cycle(asset_animation)
"""

class GameState:
    def __init__(self) -> None:
        self.current_stage = None
        self.game_surface = None
        self.game_clock = None
    
    def play(self):
        while True:
            self.game_surface.fill((0,0,0))
            if self.current_stage:
                self.current_stage.run_iteration()
            pygame.display.update()
            self.game_clock.tick(4)


class Stage:
    def __init__(self, game_state: GameState) -> None:
        from jam_session.lib.entities import asset
        self.game_state = game_state
        self.asset_example = asset.from_image_resource('./jam_session/resources/sprites/scene_start_game_title.png', y_origin=200)
        self.asset_groups = pygame.sprite.Group()
        self.asset_groups.add(self.asset_example)


    def run_iteration(self):
        self.asset_groups.update()
        self.asset_groups.draw(self.game_state.game_surface)


class MainMenuStage(Stage):
    pass

def start_game():
    game_state = GameState()
    game_state.game_surface, game_state.game_clock = initialize_game_surface(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    game_state.current_stage = MainMenuStage(game_state=game_state)

    game_state.play()




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
