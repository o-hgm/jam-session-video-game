import pygame


class GameState:
    def __init__(self) -> None:
        self.current_stage = None
        self.game_surface = None
        self.game_clock = None
    
    def play(self):
        self.current_stage.initialize()
        while True:
            self.game_surface.fill((0,0,0))
            if self.current_stage:
                self.current_stage.run_iteration()
            pygame.display.update()
            self.game_clock.tick(4)