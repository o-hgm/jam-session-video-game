import pygame

from jam_session.lib.core import game_engine

game_obj = None

def initialize_game_resources():
    global game_obj

    pygame.init()

    # Setup Game Engine
    game_obj = game_engine.Game()

def run_game():
    global game_obj
    initialize_game_resources()

    game_obj.run_loop()

if __name__ == "__main__":
    run_game()