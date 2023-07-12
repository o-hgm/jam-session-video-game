import pygame
import pygame_gui

from pygame_gui.elements.ui_selection_list import UISelectionList

class StyledUISelectionList(UISelectionList):
    def __init__(self, *args, **kwargs):
        self.selected_option = dict()
        super().__init__(*args, **kwargs)

    def rebuild(self):
        super().rebuild()
        self.apply_hover_on_selected()

    def apply_hover_on_selected(self):
        if self.selected_option is not None:
            index = self.selected_option.get('index', 0)
            item = self.item_list_container.elements[index]
            item.hovered = True
            item.on_hovered()

class Scene:
    def __init__(self, background, collision_layer, objects, npcs):
        self.background = background
        self.collision_layer = collision_layer
        self.objects = objects
        self.npcs = npcs


class UserInterfaceManager:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width, self.screen_height = self.screen.get_size()

        self.manager = pygame_gui.UIManager((self.screen_width, self.screen_height), "theme.json")

        self.scene_viewport_width = self.screen_width
        self.scene_viewport_height = int(2 * self.screen_height / 3)
        self.text_action_width = self.screen_width
        self.text_action_height = self.screen_height - self.scene_viewport_height

        self.scene_viewport = pygame.Surface(
            (self.scene_viewport_width, self.scene_viewport_height)
        )
        self.text_action_panel = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(
                (0, self.scene_viewport_height),
                (self.text_action_width, self.text_action_height),
            ),
            starting_layer_height=1,
            manager=self.manager,
        )

    def show_actions(self, actions):
        self.actions = actions
        self.selected_action = 0

        action_texts = [action['text'] for action in actions]
        self.action_list = StyledUISelectionList(relative_rect=pygame.Rect((10, self.text_action_height - 200),
                                                                                         (self.text_action_width - 20, 200)),
                                                                item_list=action_texts,
                                                                manager=self.manager,
                                                                container=self.text_action_panel,
                                                                allow_multi_select=False)
        self.action_list.selected_option = {'index': self.selected_action, 'text': self.actions[self.selected_action]['text']}
        self.action_list.rebuild()

    def process_action_event(self):
        action_id = self.actions[self.selected_action]["id"]
        print(f"Selected action: {action_id}")

    def enable_text_box(self, text):
        text_box_height = self.text_action_height
        self.text_box = pygame_gui.elements.UITextBox(
            text,
            relative_rect=pygame.Rect(
                (0, 0), (self.text_action_width, text_box_height)
            ),
            manager=self.manager,
            container=self.text_action_panel,
        )
        self.text_box.rebuild()

    def write_text(self, text):
        self.text_box.html_text = text
        self.text_box.rebuild()

    def load_scene(self, scene):
        self.current_scene = scene
        self.scene_viewport.blit(scene.background, (0, 0))


import pygame
import pygame_gui

# ... UserInterfaceManager and Scene classes ...


def main():
    pygame.init()

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pokemon Style UI Example")

    clock = pygame.time.Clock()
    ui_manager = UserInterfaceManager(screen)
    ui_manager.manager.ui_theme.load_theme("theme.json")

    yellow_background = pygame.Surface(
        (ui_manager.scene_viewport_width, ui_manager.scene_viewport_height)
    )
    yellow_background.fill((255, 255, 0))
    example_scene = Scene(yellow_background, None, [], [])
    ui_manager.load_scene(example_scene)

    # ui_manager.enable_text_box("")
    actions = [
        {"index": 0, "id": "action1", "text": "Action 1"},
        {"index": 1, "id": "action2", "text": "Action 2"},
        {"index": 2, "id": "action3", "text": "Action 3"},
    ]
    ui_manager.show_actions(actions)

    running = True
    while running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    ui_manager.selected_action = max(0, ui_manager.selected_action - 1)
                    ui_manager.action_list.selected_option = {'index': ui_manager.selected_action, 'text': ui_manager.actions[ui_manager.selected_action]['text']}
                    ui_manager.action_list.rebuild()
                elif event.key == pygame.K_DOWN:
                    ui_manager.selected_action = min(len(ui_manager.actions) - 1, ui_manager.selected_action + 1)
                    ui_manager.action_list.selected_option = {'index': ui_manager.selected_action, 'text': ui_manager.actions[ui_manager.selected_action]['text']}
                    ui_manager.action_list.rebuild()
                elif event.key == pygame.K_RETURN:
                    ui_manager.process_action_event()


            ui_manager.manager.process_events(event)

        ui_manager.manager.update(time_delta)
        ui_manager.action_list.apply_hover_on_selected()  # Add this line

        screen.blit(ui_manager.scene_viewport, (0, 0))
        ui_manager.manager.draw_ui(screen)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
