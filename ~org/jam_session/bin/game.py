from jam_session.lib.components.game import create_game

def start_game():
    game_obj = create_game()
    game_obj.start()

if __name__ == "__main__":
    start_game()