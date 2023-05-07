import pygame
import pygame.draw
import pygame_gui
import pygame.key

import pytmx

# Initialize pygame
pygame.init()


PLAYER_COLOR = (0, 255, 0)
# Dummy player_position, to be replaced with the actual player character
player_position = (1, 1)

# Define the total width and height
GAME_WIDTH, GAME_HEIGHT = 864, 600
# Define game settings
WINDOW_DISPLAY_WIDTH, WINDOW_DISPLAY_HEIGHT = GAME_WIDTH, int(GAME_HEIGHT * 2 / 3)

FPS = 60
BG_COLOR = (50, 50, 50)
BG_GAME_COLOR = (100, 100, 100)
# Define grid settings
GRID_SIZE = 64
MAP_WIDTH, MAP_HEIGHT = 10, 7

DRAWABLE_SURFACE_X = int(WINDOW_DISPLAY_WIDTH / GRID_SIZE)
DRAWABLE_SURFACE_Y = int(WINDOW_DISPLAY_HEIGHT / GRID_SIZE)


# Generate a simple map with walkable (0) and non-walkable (1) cells
def generate_map():
    game_map = [[0 for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
    for i in range(5, 15):
        for j in range(10, 20):
            game_map[i][j] = 1
    return game_map


class GameEngine:
    def __init__(self, width, height, fps):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("RPG Game")
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.running = True
        self.user_interface = None

    def handle_events(self):
        key_event = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                key_event = event.key

            if event.type == pygame.KEYDOWN and self.user_interface.text_input.is_enabled:
                self.user_interface.handle_text_input(event)
            # Pass events to pygame_gui manager
            self.user_interface.manager.process_events(event)

        return key_event

    def main_loop(self, scene: "Scene", player: "SpritePlayer", user_interface: "UserInterfaceInteractive"):
        while self.running:
            self.clock.tick(self.fps)
            key_event = self.handle_events()
            scene.update(player, key_event)
            player.update(scene, key_event)
            user_interface.draw(self.screen, scene, player)
            pygame.display.flip()

        pygame.quit()


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


class UserInterface:
    def __init__(self, bg_color):
        self.bg_color = bg_color

    def draw(self, screen, scene, player):
        screen.fill(self.bg_color)
        scene.render(screen, player.position)
        player.render(screen, scene)


class Player:
    def __init__(self, position, color):
        self.position = position
        self.color = color

    def update(self, scene, key_event):
        if key_event:
            new_x, new_y = self.position

            if key_event == pygame.K_LEFT:
                new_x -= 1
            elif key_event == pygame.K_RIGHT:
                new_x += 1
            elif key_event == pygame.K_UP:
                new_y -= 1
            elif key_event == pygame.K_DOWN:
                new_y += 1

            if scene.is_walkable(new_x, new_y):
                self.position = (new_x, new_y)

    def render(self, screen, scene):
        min_x, min_y = scene.visible_range(self.position)
        pygame.draw.rect(
            screen,
            self.color,
            (
                (self.position[0] - min_x) * scene.grid_size,
                (self.position[1] - min_y) * scene.grid_size,
                scene.grid_size,
                scene.grid_size,
            ),
        )


import pygame
from pytmx import load_pygame

class Scene:
    def __init__(
        self,
        grid_size,
        drawable_surface_x,
        drawable_surface_y,
        user_interface,
        map_file,
    ):
        self.map_data = load_pygame(map_file)
        self.user_interface = user_interface
        self.grid_size = grid_size
        self.drawable_surface_x = drawable_surface_x
        self.drawable_surface_y = drawable_surface_y

    def is_walkable(self, x, y):
        print(x, y)
        map_tile = self.map_data.get_tile_image(x, y, 1)
        print(map_tile)
        if map_tile is not None:
            return False
        return True
        if 0 <= x < len(self.map_data[0]) and 0 <= y < len(self.map_data):
            return self.map_data[y][x] == 0
        return False

    def is_colliding(self, x, y):
        if y >= 5 and y <= 15:
            if x >= 10 and x <= 20:
                return (True, "Asset")

        return (False, None)

    def visible_range(self, player_position):
        min_x = max(1, player_position[0] - self.drawable_surface_x // 2)
        min_y = max(1, player_position[1] - self.drawable_surface_y // 2)
        return min_x, min_y

    def render(self, screen: "pygame.Surface", player_position):
        min_x, min_y = self.visible_range(player_position)
        max_x, max_y = min_x + self.drawable_surface_x, min_y + self.drawable_surface_y

        """
        for layer in self.map_data.layers:
            pass
        """
        for y in range(min_y, max_y):
            for x in range(min_x, max_x):
                tile_obj = self.map_data.get_tile_image(x, y, 0)
                if tile_obj is None:
                    tile_obj = self.map_data.get_tile_image(x, y, 1)

                if tile_obj:
                    map_coordinates = (
                            (x - min_x) * self.grid_size,
                            (y - min_y) * self.grid_size
                    )
                    screen.blit(tile_obj, map_coordinates)

    def handle_interaction(self, player, asset):
        self.user_interface: UserInterfaceInteractive
        self.user_interface.ui_dialog_panel.show()
        self.user_interface.update_dialog(f"New interaction with {asset}")
        self.user_interface.enable_action_buttons({})
        
    def clear_interaction(self, player):
        self.user_interface: UserInterfaceInteractive
        self.user_interface.ui_dialog_panel.hide()

    def update(self, player, key_event):
        pass  # No update needed for the scene in this example, but you can add more logic here if needed.


import pygame


class SpritePlayer:
    def __init__(self, position, sprite_sheet_path, sprite_size):
        self.sprite_map = {
            "direction_down": [],
            "direction_left": [],
            "direction_right": [],
            "direction_up": [],
        }
        self.default_layout = [
            "direction_down",
            "direction_left",
            "direction_right",
            "direction_up",
        ]
        self.current_action = "direction_down"
        self.current_frame = 0
        self.position = position
        self.sprite_size = sprite_size
        self.sprites = self.load_sprites(sprite_sheet_path, sprite_size)
        self.current_sprite = self.sprite_map[self.current_action][self.current_frame]

    def load_sprites(self, sprite_sheet_path, sprite_size):
        sprite_sheet = pygame.image.load(sprite_sheet_path).convert_alpha()
        width, height = sprite_sheet.get_size()
        sprites = []

        for y in range(0, height, sprite_size):
            index = int(y / sprite_size)
            current_action = (
                self.default_layout[index] if index < len(self.default_layout) else None
            )
            if current_action is not None:
                for x in range(0, width, sprite_size):
                    sprite = pygame.Surface(
                        (sprite_size, sprite_size), pygame.SRCALPHA, 32
                    )
                    sprite.blit(sprite_sheet, (0, 0), (x, y, sprite_size, sprite_size))
                    self.sprite_map[current_action].append(sprite)


    def update(self, scene, key_event):
        if key_event:
            new_x, new_y = self.position

            if key_event == pygame.K_LEFT:
                new_x -= 1
                self.current_action = "direction_left"
                # Update the current sprite to face left
                # self.current_sprite = self.sprites[1]
            elif key_event == pygame.K_RIGHT:
                new_x += 1
                self.current_action = "direction_right"
                # Update the current sprite to face right
                # self.current_sprite = self.sprites[2]
            elif key_event == pygame.K_UP:
                new_y -= 1
                self.current_action = "direction_up"
                # Update the current sprite to face up
                # self.current_sprite = self.sprites[3]
            elif key_event == pygame.K_DOWN:
                new_y += 1
                self.current_action = "direction_down"
                # Update the current sprite to face down
                # self.current_sprite = self.sprites[0]

            total_frames_of_current_action = self.sprite_map[self.current_action] or 1
            self.current_frame = (self.current_frame + 1) % len(
                total_frames_of_current_action
            )
            self.current_sprite = self.sprite_map[self.current_action][
                self.current_frame
            ]

            if scene.is_walkable(new_x, new_y):
                self.position = (new_x, new_y)

            is_colliding, target_asset = scene.is_colliding(new_x, new_y)
            if is_colliding:
                scene.handle_interaction(self, target_asset)
            else:
                scene.clear_interaction(self)

    def render(self, screen, scene):
        min_x, min_y = scene.visible_range(self.position)
        screen.blit(
            self.current_sprite,
            (
                (self.position[0] - min_x) * scene.grid_size,
                (self.position[1] - min_y) * scene.grid_size,
            ),
        )


def main():
    # Create instances of game components
    game_engine = GameEngine(GAME_WIDTH, GAME_HEIGHT, FPS)
    user_interface = UserInterfaceInteractive(BG_COLOR, game_engine)
    # El tamaño de sprite afecta a la collision
    player = SpritePlayer((1, 1), "Sprite-Wei.png", 128)
    scene = Scene(
        GRID_SIZE,
        DRAWABLE_SURFACE_X,
        DRAWABLE_SURFACE_Y,
        user_interface,
        "map_1.tmx"
    )

    # Run the game
    game_engine.main_loop(scene, player, user_interface)


if __name__ == "__main__":
    main()
