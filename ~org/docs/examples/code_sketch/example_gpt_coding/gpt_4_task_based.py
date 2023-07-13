import pygame
import pygame_gui
import pygame_gui.elements

# Constants
WIDTH = 800
HEIGHT = 600
TEXT_BOX_WIDTH = 400
TEXT_BOX_HEIGHT = 150

# Initialize pygame
pygame.init()

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game UI Example")

ui_manager = pygame_gui.UIManager(
    window_resolution=(800, 600),
    theme_path="./theme.json"
)


# Create a panel for text message
text_panel = pygame_gui.elements.UIPanel(
    relative_rect=pygame.Rect(
        200,200, 300,300
    ),
    starting_layer_height=4,
    manager=ui_manager,
    anchors={'center': 'center'},
    object_id=pygame_gui.core.ObjectID(object_id='#ui_panel_actions')
)

# Create a text box to display messages
text_box = pygame_gui.elements.UITextBox(
    html_text="Hello, welcome to our game!",
    relative_rect=pygame.Rect(0, 0, TEXT_BOX_WIDTH, TEXT_BOX_HEIGHT),
    manager=ui_manager,
    container=text_panel,
    anchors={"left": "left", "right": "right", "top": "top", "bottom": "bottom"},
)


def show_message(message):
    text_box.html_text = message
    text_box.rebuild()


# Main game loop
running = True
clock = pygame.time.Clock()

show_message("Hello my friend")

button_layout_rect = pygame.Rect(30, 20, 100, 20)


while running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        ui_manager.process_events(event)

    ui_manager.update(time_delta)

    # Draw everything
    screen.fill((255, 255, 255))
    ui_manager.draw_ui(screen)

    pygame.display.update()

pygame.quit()
