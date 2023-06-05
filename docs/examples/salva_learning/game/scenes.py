import sys
import pygame as pg
import pygame_gui as pgg
from entities import Player
from settings import *


class Scene:
    def __init__(self, game):
        self.game = game

    def events(self, events):
        raise NotImplementedError("events must be defined")

    def update(self, dt):
        raise NotImplementedError("update must be defined")

    def draw(self, display):
        raise NotImplementedError("draw must be defined")


class MenuScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.manager = pgg.UIManager(
            (WIDTH, HEIGHT), theme_path='res/themes/custom.json')

        self.play_button = pgg.elements.UIButton(
            relative_rect=pg.Rect((400, 100), (200, 50)),
            text='JUGAR', manager=self.manager)

        self.credits_button = pgg.elements.UIButton(
            relative_rect=pg.Rect((400, 175), (200, 50)),
            text='CREDITOS', manager=self.manager)

        self.exit_button = pgg.elements.UIButton(
            relative_rect=pg.Rect((400, 250), (200, 50)),
            text='SALIR', manager=self.manager)

    def events(self, events):
        for event in events:
            self.manager.process_events(event)
            if event.type == pgg.UI_BUTTON_PRESSED:
                if event.ui_element == self.play_button:
                    self.game.change_scene(MainScene(self.game))
                if event.ui_element == self.credits_button:
                    print("ESCENA DE CRÉDITOS")
                if event.ui_element == self.exit_button:
                    sys.exit()

    def update(self, dt):
        self.manager.update(dt)

    def draw(self, display):
        display.fill((0, 0, 0))
        self.manager.draw_ui(display)


class MainScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.background = pg.image.load("res/images/grass.png").convert_alpha()
        self.common_group = pg.sprite.Group()
        self.common_group.add(Player(325, 150))

    def events(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.game.change_scene(MenuScene(self.game))

    def update(self, dt):
        self.common_group.update(dt)

    def draw(self, display):
        display.blit(self.background, (0, 0))
        self.common_group.draw(display)