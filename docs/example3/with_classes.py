from docs.example3.Player import SpritePlayer
from docs.example3.Scene import Scene
from docs.example3.UserInterfaceInteractive import UserInterfaceInteractive
import pygame
import pygame.draw
import pygame.key

# Initialize pygame
pygame.init()

"""
Información para generar el mapa y dibujar el grid. En la versión anterior se utilizaba 
para dibujar los 'rect' que representaban suelo, muralla y personaje.
"""
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

"""
Indica el número de celdas disponibles
"""
DRAWABLE_SURFACE_X = int(WINDOW_DISPLAY_WIDTH / GRID_SIZE)
DRAWABLE_SURFACE_Y = int(WINDOW_DISPLAY_HEIGHT / GRID_SIZE)


class GameEngine:
    """
    Representa el controlador principal del juego, conecta la interfaz con los distintos elementos del juego.
    
    """
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

class UserInterface:
    def __init__(self, bg_color):
        self.bg_color = bg_color

    def draw(self, screen, scene, player):
        screen.fill(self.bg_color)
        scene.render(screen, player.position)
        player.render(screen, scene)


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
        "tiled/testofi2.tmx"
    )

    # Run the game
    game_engine.main_loop(scene, player, user_interface)


if __name__ == "__main__":
    main()
