class GameController:
    """
    Game Controller implements all the game logic and rules for Late Again.
    It instantiates the game components and connect them together.

    Game Controller is the main entry point for the game.
    """

    def __init__(self) -> None:
        self.is_running = False
        self.clock_fps = 60


    def run_game(self) -> None:
        self.is_running = True

        while self.is_running:
            self.clock.tick(self.clock_fps)
            self.handle_events()
            self.update_game_state()
            self.draw_ui()

    def handle_events(self) -> None:
        pass

    def update_game_state(self) -> None:
        pass

    def draw_ui(self) -> None:
        pass
