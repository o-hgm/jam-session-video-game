import pygame

from jam_session.lib.pygame_utils.create_surface import initialize_game_surface
from jam_session.lib.base.keyboard_event import keyboard_event_loop


def start_game():
    game_surface, game_clock = initialize_game_surface()
    while True:
        game_clock.tick(60)
        keyboard_event_loop()
        pygame.display.update()


if __name__ == "__main__":
    start_game()