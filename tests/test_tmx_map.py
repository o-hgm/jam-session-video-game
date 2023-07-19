import pygame
from late_again.components.maps.tmx import TMXMapController

def test_tmx_map_loader():
    """
    """
    pygame.init()
    MAP_PATH = "tests/resources/map_1.tmx"

    SURFACE_WIDTH, SURFACE_HEIGHT = (800, 600)
    MAP_TILE_WIDTH, MAP_TILE_HEIGHT = (64, 64)

    pygame_screen = pygame.display.set_mode((SURFACE_WIDTH, SURFACE_HEIGHT))
    pygame_surface = pygame.Surface((SURFACE_WIDTH, SURFACE_HEIGHT))
    tmx_map = TMXMapController(pygame_surface, MAP_PATH)

    tmx_map.load_resources()

    assert tmx_map.tmx_map is not None
    assert tmx_map.size_w == 800
    assert tmx_map.size_h == 600
    assert tmx_map.tile_w == MAP_TILE_WIDTH
    assert tmx_map.tile_h == MAP_TILE_HEIGHT