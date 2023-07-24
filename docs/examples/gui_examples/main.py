import sys
from ui import NarratorPanel, UIManager, PlayerPanel
import pygame as pg
import pygame_gui as pg_gui
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
                    if event.key == pg.K_3:
                        self.player_panel.create_button(self.ui.manager, 'new button!!!', 580, 20)
                    if event.key == pg.K_ESCAPE:
                        sys.exit()

                self.ui.manager.process_events(event)

                if event.type == pg_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.player_panel.text_button:
                        text_input = self.player_panel.text_entry.get_text()
                        if (text_input != ""):
                            print(self.player_panel.text_entry.get_text())
                            self.player_panel.text_entry.set_text('')

                    if event.ui_element == self.player_panel.button:
                        self.player_panel.button.kill()

                if self.ui.manager.get_focus_set() and  self.player_panel.text_entry in self.ui.manager.get_focus_set():
                    if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                        text_input = self.player_panel.text_entry.get_text()
                        if (text_input != ""):
                            print(self.player_panel.text_entry.get_text())
                            self.player_panel.text_entry.set_text('')

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