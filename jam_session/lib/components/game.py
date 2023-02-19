class Game:
    """
    A Game instance the components of the game and controls the application flow.
    """

    def __init__(self) -> None:
        self.run_loop = True

    def loop_iteration(self):
        pass

    def run(self):
        while self.run_loop:
            self.loop_iteration()
