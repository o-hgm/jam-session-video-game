import pygame
import pygame.draw
# Initialize pygame
pygame.init()


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

"""
0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 P 0 0 1 1 1 1 0 0 0 0 0
0 0 0 0 0 1 1 1 1 0 0 0 0 0 
0 0 0 0 0 1 1 1 1 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 
"""

# Generate a simple map with walkable (0) and non-walkable (1) cells
def generate_map():
    game_map = [[0 for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
    for i in range(5, 15):
        for j in range(10, 20):
            game_map[i][j] = 1
    return game_map

# Function to check if a position is walkable
def is_walkable(x, y, game_map):
    if 0 <= x < MAP_WIDTH and 0 <= y < MAP_HEIGHT:
        return game_map[y][x] == 0
    return False

game_map = generate_map()

# Function to render the visible portion of the map
# Function to render the visible portion of the map

def render_map(screen, game_map, player_position):
    
    # Calculate the range of visible cells based on the player's position
    min_x = max(0, player_position[0] - WINDOW_DISPLAY_WIDTH // (2 * GRID_SIZE))
    min_y = max(0, player_position[1] - WINDOW_DISPLAY_HEIGHT // (2 * GRID_SIZE))
    
    max_y = max(DRAWABLE_SURFACE_Y, player_position[1] + WINDOW_DISPLAY_HEIGHT // (2 * GRID_SIZE))
    max_x = max(DRAWABLE_SURFACE_X, player_position[0] + WINDOW_DISPLAY_WIDTH // (2 * GRID_SIZE))
    

    
    for y in range(min_y, max_y):
        for x in range(min_x, max_x):
            try:
                cell_color = (200, 200, 200) if game_map[y][x] == 0 else (100, 100, 100)
            except:
                cell_color = (100,0,0)
            pygame.draw.rect(
                screen, 
                cell_color, 
                (
                    x * GRID_SIZE - min_x * GRID_SIZE, 
                    y * GRID_SIZE - min_y * GRID_SIZE, 
                    GRID_SIZE, 
                    GRID_SIZE
                 )
            )

    return min_x, min_y


PLAYER_COLOR = (0, 255, 0)
# Dummy player_position, to be replaced with the actual player character
player_position = (1, 1)


# Create game window
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
screen.fill(BG_GAME_COLOR)
pygame.display.set_caption("RPG Game")
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    # Limit frame rate
    clock.tick(FPS)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                new_x = player_position[0] - 1
                if is_walkable(new_x, player_position[1], game_map):
                    player_position = (new_x, player_position[1])
            elif event.key == pygame.K_RIGHT:
                new_x = player_position[0] + 1
                if is_walkable(new_x, player_position[1], game_map):
                    player_position = (new_x, player_position[1])
            elif event.key == pygame.K_UP:
                new_y = player_position[1] - 1
                if is_walkable(player_position[0], new_y, game_map):
                    player_position = (player_position[0], new_y)
            elif event.key == pygame.K_DOWN:
                new_y = player_position[1] + 1
                if is_walkable(player_position[0], new_y, game_map):
                    player_position = (player_position[0], new_y)
            print("Player is in: (%s, %s)" % player_position)


    # Update game state

    # Render game screen
    screen.fill(BG_COLOR)
    min_x, min_y = render_map(screen, game_map, player_position)

    # Draw player at their current position relative to the viewport
    pygame.draw.rect(screen, (255, 0, 0), ((player_position[0] - min_x) * GRID_SIZE, (player_position[1] - min_y) * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    pygame.display.flip()

# Quit pygame
pygame.quit()
