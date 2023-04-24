import pygame
import pygame_gui
from pygame.locals import *
from pygame_gui.elements import UIPanel, UILabel, UIButton


class UIManager:
    def __init__(self, screen, manager):
        self.screen = screen
        self.manager = manager
        self.scene = Scene(manager)

    def draw(self):
        self.manager.draw_ui(self.screen)

    def process_events(self, event):
        self.manager.process_events(event)

    def show_text(self, text):
        self.scene.set_message(text)

    def update(self, time_delta):
        self.manager.update(time_delta)




class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, color, width=20, height=20):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


class UCP(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, (0, 0, 255))


class NPC(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, (255, 0, 0))


class StaticAsset(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, (0, 255, 0))

class Interaction:
    def __init__(self, manager):
        self.manager = manager

    def check_interaction(self, ucp, npc):
        if pygame.sprite.collide_rect(ucp, npc):
            self.trigger_interaction()

    def trigger_interaction(self):
        self.manager.show_text("Good Morning")


class Action:
    def __init__(self, manager):
        self.manager = manager

    def check_action(self, ucp, asset):
        if pygame.sprite.collide_rect(ucp, asset):
            self.trigger_action()

    def trigger_action(self):
        self.manager.show_action("Switch on")

class CustomUIPanel(UIPanel):
    def __init__(self, *args, border_color=(255, 255, 255), border_width=1, **kwargs):
        super().__init__(*args, **kwargs)
        self.border_color = border_color
        self.border_width = border_width
        self.set_image(None)

    def draw(self, surface):
        super().draw(surface)
        pygame.draw.rect(surface, self.border_color, self.relative_rect, self.border_width)


class Scene:
    def __init__(self, manager):
        self.manager = manager
        self.create_interface()

    def create_interface(self):
        self.panel = CustomUIPanel(
            pygame.Rect(0, 400, 800, 200),
            starting_layer_height=1,
            manager=self.manager,
            anchors={
                "left": "left",
                "right": "right",
                "top": "bottom",
                "bottom": "bottom",
            },
            object_id="pixel_panel",
            border_color=(255, 255, 255),
            border_width=4
        )

        self.message_label = UILabel(
            pygame.Rect(10, 10, 780, 180),
            "",
            manager=self.manager,
            container=self.panel,
            anchors={
                "left": "left",
                "right": "right",
                "top": "top",
                "bottom": "bottom",
            },
        )
    def set_message(self, message):
        self.message_label.set_text(message)
        self.message_label.rebuild()



def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("My RPG Game")
    clock = pygame.time.Clock()
    # Load with theme
    manager = pygame_gui.UIManager(
        window_resolution=(800, 600),
        theme_path="./theme.json"
    )
    import os
    print(os.path.exists('./theme.json'))
    ui_manager = UIManager(screen, manager)
    ui_manager.show_text("Hello")
    ucp = UCP(100, 100)
    npc = NPC(200, 100)
    asset = StaticAsset(300, 100)

    interaction = Interaction(ui_manager)
    action = Action(ui_manager)

    running = True

    while running:
        time_delta = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            ui_manager.process_events(event)

        ui_manager.update(time_delta)  # Add this line to update the UI manager
        ui_manager.draw()
    
        manager.update(time_delta)

        screen.blit(ucp.image, ucp.rect)
        screen.blit(npc.image, npc.rect)
        screen.blit(asset.image, asset.rect)

        interaction.check_interaction(ucp, npc)
        action.check_action(ucp, asset)

        pygame.display.flip()
        manager.update(time_delta)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
