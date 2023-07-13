class GameController:
    """
    Game Controller implements all the game logic and rules for Late Again.
    It instantiates the game components and connect them together.

    Game Controller is the main entry point for the game.
    """

    def __init__(self) -> None:
        self.is_running = False

    def run_game(self) -> None:
        self.is_running = True
        
        while self.is_running:
            pass