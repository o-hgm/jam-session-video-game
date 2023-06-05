from docs.example3.Player import Player
from docs.example3.Scene import Scene
import pygame
import pygame_gui

class UserInterfaceInteractive:
    def __init__(self, bg_color, game_engine):
        self.actions = {}
        self.bg_color = bg_color
        self.manager = pygame_gui.UIManager(
            (game_engine.screen.get_width(), game_engine.screen.get_height())
        )

        self.game_engine = game_engine
        game_engine.user_interface = self

        self.build_user_interface()

    def build_user_interface(self):
        self.ui_dialog_panel = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(
                (0, int(self.game_engine.screen.get_height() * 2 / 3)),
                (
                    self.game_engine.screen.get_width(),
                    int(self.game_engine.screen.get_height() * 1 / 3),
                ),
            ),
            #starting_layer_height=1,
            manager=self.manager,
        )
        self.ui_dialog_panel.hide()

        # Create a text box for the dialog
        self.ui_dialog_text_box = pygame_gui.elements.UITextBox(
            html_text="",
            relative_rect=pygame.Rect(
                (30, 10),
                (
                    500, 100
                ),
            ),
            manager=self.manager,
            container=self.ui_dialog_panel,
            anchors={
                "left": "left",
                "right": "right",
                "top": "top",
                "bottom": "bottom",
            },
        )

                # Create input box for user text input
        self.text_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((30, self.ui_dialog_panel.rect.height - 85), (500, 70)),
            manager=self.manager,
            container=self.ui_dialog_panel
        )
        self.text_input.disable()

    def handle_text_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                user_text = self.text_input.get_text()
                self.text_input.set_text('')
                self.update_dialog(f"El jugador dijo: {user_text}")

    def enable_action_buttons(self, actions):
        # Create buttons for actions
        self.actions = {
            "dialogue": pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(
                    (self.ui_dialog_panel.rect.width - 320, 30), (160, 30)
                ),
                text="Dialogar",
                manager=self.manager,
                container=self.ui_dialog_panel,
            ),
            "harass": pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(
                    (self.ui_dialog_panel.rect.width - 320, 70), (160, 30)
                ),
                text="Hostigar",
                manager=self.manager,
                container=self.ui_dialog_panel,
            ),
            "shout": pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(
                    (self.ui_dialog_panel.rect.width - 320, 110), (160, 30)
                ),
                text="Gritar",
                manager=self.manager,
                container=self.ui_dialog_panel,
            ),
            "kill": pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(
                    (self.ui_dialog_panel.rect.width - 320, 150), (160, 30)
                ),
                text="Violencia",
                manager=self.manager,
                container=self.ui_dialog_panel,
            ),
        }

    def update_dialog(self, text):
        self.ui_dialog_text_box.set_text(" " + text)

    def draw(self, screen, scene: "Scene", player: "Player"):
        screen.fill(self.bg_color)
        scene.render(screen, player.position)
        player.render(screen, scene)

        self.manager.update(1 / self.game_engine.fps)
        self.manager.draw_ui(screen)