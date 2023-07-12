import pygame_gui as pg_gui
import pygame as pg

class Ui:
    def __init__(self, display):
        self.display = display
        self.manager = pg_gui.UIManager(
            (self.display.get_width(), self.display.get_height())
        )

        self.ui_panel = pg_gui.elements.UIPanel(
            relative_rect=pg.Rect(
                (0, int(self.display.get_height() * 2 / 3)),
                (
                    self.display.get_width(),
                    int(self.display.get_height() * 1 / 3),
                ),
            ),
            #starting_layer_height=1,
            manager=self.manager,
            )
        self.ui_panel.hide()
        self.show_panel = False

    def draw(self):
        if self.show_panel:
            self.ui_panel.show()
        else:
            self.ui_panel.hide()