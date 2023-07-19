import pytest

import pygame
from late_again.components.maps.tmx import TMXMapController

MAP_PATH = "tests/resources/map_1.tmx"
MAP_PATH_2 = "tests/resources/map_2.tmx"

SURFACE_WIDTH, SURFACE_HEIGHT = (800, 600)
# Got from map file
MAP_TILE_WIDTH, MAP_TILE_HEIGHT = (64, 64)
# Got from map file
MAP_TILES_X, MAP_TILES_Y = (30, 20)

# 0 Index grid
WALKABLE_ON_X = 5 * MAP_TILE_WIDTH
WALKABLE_ON_Y = 5 * MAP_TILE_HEIGHT

@pytest.fixture
def tmx_map() -> TMXMapController:
    pygame.init()

    pygame_screen = pygame.display.set_mode((SURFACE_WIDTH, SURFACE_HEIGHT))
    tmx_map = TMXMapController(pygame_screen, MAP_PATH)

    tmx_map.load_resources()

    return tmx_map


@pytest.fixture
def tmx_map_scroll() -> TMXMapController:
    pygame.init()

    pygame_screen = pygame.display.set_mode((SURFACE_WIDTH, SURFACE_HEIGHT))
    tmx_map = TMXMapController(pygame_screen, MAP_PATH_2)

    return tmx_map

def test_tmx_map_loader(tmx_map):
    """
    Ensures that, given a map resource, after loading it, 
    the map controller contains all the data to perform render and 
    calculation.

    Map loading is included as fixture to avoid repeating the code in
    all the tests.
    """

    tmx_map.load_resources()


    assert tmx_map.tmx_map is not None
    assert tmx_map.size_w == 800
    assert tmx_map.size_h == 600
    assert tmx_map.tile_w == MAP_TILE_WIDTH
    assert tmx_map.tile_h == MAP_TILE_HEIGHT
    assert tmx_map.tiles_x == MAP_TILES_X
    assert tmx_map.tiles_y == MAP_TILES_Y

def test_tmx_walkable_check(tmx_map: TMXMapController):
    
    tmx_map.load_resources()

    MIN_X, MIN_Y = (0, 0)
    MAX_X, MAX_Y = (MAP_TILES_X * MAP_TILE_WIDTH, MAP_TILES_Y * MAP_TILE_HEIGHT)

    RANGE_X = range(MIN_X, MAX_X + MAP_TILE_WIDTH, MAP_TILE_WIDTH)
    RANGE_Y = range(MIN_Y, MAX_Y + MAP_TILE_HEIGHT, MAP_TILE_HEIGHT)

    print(f"RANGE_X: {RANGE_X} ({len(RANGE_X)} items)")
    print(f"RANGE_Y: {RANGE_Y} ({len(RANGE_Y)} items)")

    for x in RANGE_X:
        for y in RANGE_Y:
            print(f"Checking tile at position ({x}, {y}) [{x/MAP_TILE_WIDTH}, {y/MAP_TILE_HEIGHT}]")
            # Check internally
            cell_is_walkable = tmx_map.is_walkable((x , y))
            
            # The walkable area of the map is a square of 6x6 tiles
            must_be_walkable = x <= WALKABLE_ON_X and y <= WALKABLE_ON_Y

            assert cell_is_walkable == must_be_walkable, (
                f"Tile at position ({x}, {y}) [{x/MAP_TILE_WIDTH}, {y/MAP_TILE_HEIGHT}] is "
                f"{'walkable' if cell_is_walkable else 'empty'} "
                f"but should be {'walkable' if must_be_walkable else 'empty'}"
            )


def test_tmx_render(tmx_map: TMXMapController):
    """
    Ensures that the map is rendered on the screen.
    """
    tmx_map.render_map()
    pygame.display.flip()

    assert tmx_map.tmx_map is not None
    pygame.time.wait(5000)


def test_tmx_render_move_around(tmx_map_scroll: TMXMapController):
    """
    Ensures that the map is rendered on the screen and moves when the center 
    of the map is changed.
    """
    tmx_map_scroll.load_resources()

    # 5, 5 is the first point where the visible area changes
    for X in range(5, MAP_TILES_X, 1):
        for Y in range(5, MAP_TILES_Y, 1):
            print(f"Scroll is in ({X}, {Y})")
            tmx_map_scroll.game_surface.fill((255, 255, 255))
            tmx_map_scroll.set_center(X * MAP_TILE_WIDTH, Y * MAP_TILE_HEIGHT)
            tmx_map_scroll.render_map()
            pygame.display.flip()
            pygame.time.wait(1000)

    pygame.display.flip()

    assert tmx_map_scroll.tmx_map is not None
    pygame.time.wait(1000)

    assert False, ("Render is not working as expected. Check the relation between tiles and pixel position.")
