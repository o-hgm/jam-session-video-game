import pygame

class Game(object):
    """
    Game encapsula la lógica de ejecución del juego. Define como se organizan los recursos y 
    de que formas interactuan entre ellos.
    """
    DEFAULT_WIDTH = 800
    DEFAULT_HEIGHT = 600
    DEFAULT_GAME_TITLE = "Game Engine"
    DEFAULT_FPS = 30

    def __init__(self) -> None:
        self.loop_enable = False
        
        # Full Display Settings
        self.ui_width = None
        self.ui_width = None
        self.ui_display_title = None
        # Component which handles User Interface operations
        self.ui_game_interface = None
        # Pygame Display Component
        self.pygame_display = None

        # Game Clock Settings
        self.game_loop_fps = None

    def configure_display(self, width = DEFAULT_WIDTH, height = DEFAULT_HEIGHT, title = DEFAULT_GAME_TITLE, fps = DEFAULT_FPS):
        pass

    def initialize_game_engine(self):
        pass

    def run_loop(self):
        # Initialize loop
        self.loop_enable = True

        while self.loop_enable:
            # Run Clock Tick 
            self.clock.tick(self.game_loop_fps)
            pygame.display.flip()


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

    def main_loop(self, scene, player, user_interface):
        while self.running:
            self.clock.tick(self.fps)
            key_event = self.handle_events()
            scene.update(player, key_event)
            player.update(scene, key_event)
            user_interface.draw(self.screen, scene, player)
            pygame.display.flip()

        pygame.quit()