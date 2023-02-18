import pygame

from .game_state import GameState


class Stage:
    def __init__(self, game_state: GameState) -> None:
        self.game_state = game_state
        self.asset_group = None
        self.asset_objects = []

    def run_iteration(self):
        self.asset_group.update()
        self.asset_group.draw(self.game_state.game_surface)

    def load_assets(self):
        raise NotImplementedError()
    
    def initialize(self):
        self.asset_group = pygame.sprite.Group()

        for asset_object in self.load_assets():
             self.asset_group.add(asset_object)
            