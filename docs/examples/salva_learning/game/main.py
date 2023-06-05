import sys
import pygame as pg
from settings import *
from entities import Player
from scenes import MainScene, MenuScene

class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption(CAPTION)
        self.display = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
            # Scene
        self.scene = MenuScene(self)

    def run(self):
        while 1:
            dt = self.clock.tick(FPS) / 1000
            ev = pg.event.get()                 # new
            for event in ev:                    # edited
                if event.type == pg.QUIT:
                    sys.exit()
            # Scene events
            self.scene.events(ev)
            self.scene.update(dt)
            self.scene.draw(self.display)
            pg.display.update()

    def change_scene(self, scene):
        self.scene = scene


if __name__ == '__main__':
    game = Game()
    game.run()