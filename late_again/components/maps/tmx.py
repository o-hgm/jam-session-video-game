from typing import Tuple

import pygame
from pytmx import load_pygame

from .base import MapController

class TMXMapController(MapController):
    """
    TmxTileMap class

    TileMap class is a wrapper for the pytmx.TiledMap class. It is used to load
    the Tiled map file and render the map on the screen. It also provides
    methods to access different layers of the map using the collide method.

    It also ensures the map is rendered in the center of the screen and 
    the player is always in the center of the map.
    """

    def __init__(
            self, 
            game_surface: pygame.Surface,
            tmx_file: str,
        ) -> None:
        """
        Initialize the TileMap class.
        """
        super().__init__(game_surface)
        self.tmx_file = tmx_file
        self.tmx_map = None
    
    def load_resources(self):
        """
        Load the resources for the map.
        """
        try:
            self.tmx_map = load_pygame(self.tmx_file)
            self.size_w = self.game_surface.get_width()
            self.size_h = self.game_surface.get_height()
            self.tile_w = self.tmx_map.tilewidth
            self.tile_h = self.tmx_map.tileheight
        except Exception as error:
            raise AttributeError(
                "Error loading the map file %s: %s" % 
                (self.tmx_file, error)
            )

    def is_floor(self, position: Tuple[int, int]) -> bool:
        """
        Check if the position is a floor.
        """
        raise NotImplementedError("is_floor method must be implemented in the subclass")
    
    def is_obstacle(self, position: Tuple[int, int]) -> bool:
        """
        Check if the position is a obstacle.
        """
        raise NotImplementedError("is_obstacle method must be implemented in the subclass")
    
    def is_asset(self, position: Tuple[int, int]) -> bool:
        """
        Check if the position is a asset.
        """
        raise NotImplementedError("is_asset method must be implemented in the subclass")
    
    def get_coordinates(self, position: Tuple[int, int]) -> Tuple[int, int]:
        """
        Get the coordinates of the position.
        """
        raise NotImplementedError("get_coordinates method must be implemented in the subclass")
    
    def update_state(self):
        """
        Update the state of the map.
        """
        raise NotImplementedError("update_state method must be implemented in the subclass")
    
    def render_map(self):
        """
        Render the map on the screen.


        """
        raise NotImplementedError("render_map method must be implemented in the subclass")
    
    def get_visible_area(self):
        """
        Get the visible area of the map.
        """
        raise NotImplementedError("get_visible_area method must be implemented in the subclass")
    
    def get_center(self):
        """
        Get the center of the map.
        """
        raise NotImplementedError("get_center method must be implemented in the subclass")
    
    def set_center(self, x, y):
        """
        Set the center of the map.

        This method is used to set the center of the map to the given coordinates.
        """
        raise NotImplementedError("set_center method must be implemented in the subclass")
    
    def distance_to_border(self, position):
        """
        Get the distance of the position to the anchor.

        This method is used to get the distance of the position to the anchor.
        """
        raise NotImplementedError("distance_to_anchor method must be implemented in the subclass")