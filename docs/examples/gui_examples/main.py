import sys
from ui import NarratorPanel, UIManager, PlayerPanel
import pygame as pg
from settings import *
from character import Character
from player import Player

class Game:
    def __init__(self):
        pg.init()
        self.display = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.current_player_frame = 0
        self.playergroup = pg.sprite.Group()
        self.npcgroup = pg.sprite.Group()
        self.player = Player('Sprite_tyler_front.png', self)
        self.npc = Character('Sprite_mary_front.png', 400, 400)
        self.ui = UIManager(self.display)
        self.narrator_panel = NarratorPanel(self.display, self.ui.manager)
        self.player_panel = PlayerPanel(self.display, self.ui.manager)

    def run(self):
        while 1:
            dt = self.clock.tick(FPS) / 1000

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_1:
                        self.narrator_panel.show_panel = not self.narrator_panel.show_panel
                        self.player_panel.show_panel = False
                    if event.key == pg.K_2:
                        self.player_panel.show_panel = not self.player_panel.show_panel
                        self.narrator_panel.show_panel = False
                    if event.key == pg.K_ESCAPE:
                        sys.exit()

                self.ui.manager.process_events(event)

            self.clock.tick(FPS)
            self.display.fill((128,128,128))

            self.npcgroup.add(self.npc)
            self.playergroup.add(self.player)

            self.player.update(dt)
            self.narrator_panel.update()
            self.player_panel.update()
            self.ui.update(dt)

            self.playergroup.draw(self.display)
            self.npcgroup.draw(self.display)

            pg.display.flip()

if __name__ == '__main__':
    game = Game()
    game.run()