import pygame
import pygame.draw
# Initialize pygame
pygame.init()


PLAYER_COLOR = (0, 255, 0)
# Dummy player_position, to be replaced with the actual player character
player_position = (1, 1)

# Define the total width and height
GAME_WIDTH, GAME_HEIGHT = 800, 600
# Define game settings
WINDOW_DISPLAY_WIDTH, WINDOW_DISPLAY_HEIGHT = GAME_WIDTH, int(GAME_HEIGHT * 2/3)

FPS = 60
BG_COLOR = (50, 50, 50)
BG_GAME_COLOR = (100, 100, 100)
# Define grid settings
GRID_SIZE = 16
MAP_WIDTH, MAP_HEIGHT = 50, 50

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

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                return event.key

    def main_loop(self, scene, player, user_interface):
        while self.running:
            self.clock.tick(self.fps)
            key_event = self.handle_events()
            scene.update(player, key_event)
            player.update(scene, key_event)
            user_interface.draw(self.screen, scene, player)
            pygame.display.flip()

        pygame.quit()


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
        pygame.draw.rect(screen, self.color, ((self.position[0] - min_x) * scene.grid_size, (self.position[1] - min_y) * scene.grid_size, scene.grid_size, scene.grid_size))


import pygame

class Scene:
    def __init__(self, map_data, grid_size, drawable_surface_x, drawable_surface_y):
        self.map_data = map_data
        self.grid_size = grid_size
        self.drawable_surface_x = drawable_surface_x
        self.drawable_surface_y = drawable_surface_y

    def is_walkable(self, x, y):
        if 0 <= x < len(self.map_data[0]) and 0 <= y < len(self.map_data):
            return self.map_data[y][x] == 0
        return False

    def visible_range(self, player_position):
        min_x = max(0, player_position[0] - self.drawable_surface_x // 2)
        min_y = max(0, player_position[1] - self.drawable_surface_y // 2)
        return min_x, min_y

    def render(self, screen, player_position):
        min_x, min_y = self.visible_range(player_position)
        max_x, max_y = min_x + self.drawable_surface_x, min_y + self.drawable_surface_y

        for y in range(min_y, max_y):
            for x in range(min_x, max_x):
                try:
                    cell_color = (200, 200, 200) if self.map_data[y][x] == 0 else (100, 100, 100)
                except:
                    cell_color = (100,0,0)
                
                pygame.draw.rect(
                screen,
                cell_color,
                (
                (x - min_x) * self.grid_size,
                (y - min_y) * self.grid_size,
                self.grid_size,
                self.grid_size,
                ),
                )

    def update(self, player, key_event):
        pass  # No update needed for the scene in this example, but you can add more logic here if needed.


import pygame

class SpritePlayer:
    def __init__(self, position, sprite_sheet_path, sprite_size):
        self.sprite_map = {
            'direction_down': [],
            'direction_left': [],
            'direction_right': [],
            'direction_up': []
        }
        self.default_layout = ['direction_down', 'direction_left', 'direction_right', 'direction_up']
        self.current_action = 'direction_down'
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
            current_action = self.default_layout[index] if index < len(self.default_layout) else None
            print("processing (y=%s) %s" % (y, current_action))
            if current_action is not None:
                for x in range(0, width, sprite_size):
                    sprite = pygame.Surface((sprite_size, sprite_size), pygame.SRCALPHA, 32)
                    sprite.blit(sprite_sheet, (0, 0), (x, y, sprite_size, sprite_size))
                    self.sprite_map[current_action].append(sprite)

        print(self.sprite_map)

    def update(self, scene, key_event):
        if key_event:
            new_x, new_y = self.position

            if key_event == pygame.K_LEFT:
                new_x -= 1
                self.current_action = 'direction_left'
                # Update the current sprite to face left
                # self.current_sprite = self.sprites[1]
            elif key_event == pygame.K_RIGHT:
                new_x += 1
                self.current_action = 'direction_right'
                # Update the current sprite to face right
                #self.current_sprite = self.sprites[2]
            elif key_event == pygame.K_UP:
                new_y -= 1
                self.current_action = 'direction_up'
                # Update the current sprite to face up
                # self.current_sprite = self.sprites[3]
            elif key_event == pygame.K_DOWN:
                new_y += 1
                self.current_action = 'direction_down'
                # Update the current sprite to face down
                #self.current_sprite = self.sprites[0]

            total_frames_of_current_action = self.sprite_map[self.current_action] or 1
            self.current_frame = (self.current_frame + 1) % len(total_frames_of_current_action)

            if scene.is_walkable(new_x, new_y):
                self.position = (new_x, new_y)
                self.current_sprite = self.sprite_map[self.current_action][self.current_frame]

    def render(self, screen, scene):
        min_x, min_y = scene.visible_range(self.position)
        screen.blit(self.current_sprite, ((self.position[0] - min_x) * scene.grid_size, (self.position[1] - min_y) * scene.grid_size))



def main():
    # Create instances of game components
    game_engine = GameEngine(GAME_WIDTH, GAME_HEIGHT, FPS)
    user_interface = UserInterface(BG_COLOR)
    player = SpritePlayer((1, 1), "sprite_sheet_2.png", 64)
    scene = Scene(generate_map(), GRID_SIZE, DRAWABLE_SURFACE_X, DRAWABLE_SURFACE_Y)

    # Run the game
    game_engine.main_loop(scene, player, user_interface)

if __name__ == "__main__":
    main()