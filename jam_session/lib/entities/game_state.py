import pygame

from jam_session.lib.base.keyboard_event import keyboard_event_loop


class GameState:
    def __init__(self) -> None:
        self.current_stage = None
        self.game_surface = None
        self.game_clock = None
    
    def play(self):
        self.current_stage.initialize()
        while True:
            keyboard_event_loop()
            self.game_surface.fill((0,0,0))
            if self.current_stage:
                self.current_stage.run_iteration()
            pygame.display.update()
            self.game_clock.tick(4)