import sys
from ui import Ui
import pygame as pg
from settings import *
from character import Character
from player import Player

class Game:
    def __init__(self):
        pg.init()
        self.display = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.debug = True
        self.current_player_frame = 0
        self.playergroup = pg.sprite.Group()
        self.npcgroup = pg.sprite.Group()
        self.player = Player('Sprite_tyler_front.png', self)
        self.mary = Character('Sprite_mary_front.png', 400, 400)
        self.ui = Ui(self.display)

    def run(self):
        while 1:
            dt = self.clock.tick(FPS) / 1000

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_F1:
                        debug = not debug

            self.clock.tick(FPS)
            self.display.fill((128,128,128))

            self.npcgroup.add(self.npc)
            self.playergroup.add(self.player)

            self.player.update(dt)
            self.ui.manager.update(dt)

            self.playergroup.draw(self.display)
            self.npcgroup.draw(self.display)
            self.ui.draw()

            self.ui.manager.draw_ui(self.display)

            pg.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()