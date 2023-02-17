import pygame

from jam_session.lib.pygame_utils.create_surface import initialize_game_surface


def start_game():
    game_surface = initialize_game_surface()
    while True:
        pygame.display.update()


if __name__ == "__main__":
    start_game()