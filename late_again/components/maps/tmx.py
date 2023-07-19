from typing import Tuple

import logging
import pygame
import pytmx

from .base import MapController


log = logging.getLogger(__name__)

class TMXMapController(MapController):
    """
    TmxTileMap class

    TileMap class is a wrapper for the pytmx.TiledMap class. It is used to load
    the Tiled map file and render the map on the screen. It also provides
    methods to access different layers of the map using the collide method.

    It also ensures the map is rendered in the center of the screen and 
    the player is always in the center of the map.
    """
    LAYER_WALKABLE = "walkable"
    LAYER_OBSTACLE = "obstacle"
    LAYER_ASSET = "asset"

    GID_EMPTY = 0

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
        self.tmx_summary = {}

    def __load_map_file(self):
        self.tmx_map = pytmx.load_pygame(self.tmx_file)

        # Total size of the map
        self.size_w = self.game_surface.get_width()
        self.size_h = self.game_surface.get_height()
        
        # Center of the map
        self.center_x = self.size_w // 2
        self.center_y = self.size_h // 2

        # Tile size
        self.tile_w = self.tmx_map.tilewidth
        self.tile_h = self.tmx_map.tileheight

        self.tile_x = self.center_x // self.tile_w
        self.tile_y = self.center_y // self.tile_h

        # Number of tiles
        self.tiles_x = self.tmx_map.width
        self.tiles_y = self.tmx_map.height

    def __initialize_tmx_summary(self):
        self.tmx_summary = {
            self.LAYER_WALKABLE: None,
            self.LAYER_OBSTACLE: None,
            self.LAYER_ASSET: [],
        }

    def __process_tile_layer(self, tmx_layer: pytmx.TiledTileLayer):
        """
        Here we are assuming that the map has only one walkable layer, 
        one obstacle layer and multiple asset layers.

        This is a limitation of the current implementation.
        """
        if tmx_layer.properties.get("isWalkable", None):
            self.tmx_summary["walkable"] = tmx_layer
        elif tmx_layer.properties.get("isObstacle", None):
            self.tmx_summary["obstacle"] = tmx_layer
        elif tmx_layer.properties.get("isAsset", None):
            self.tmx_summary["asset"].append(tmx_layer)

    def __process_object_layer(self, tmx_layer):
        pass

    def __process_map_layers(self):
        for tmx_layer in self.tmx_map.visible_layers:
            if isinstance(tmx_layer, pytmx.TiledTileLayer):
                self.__process_tile_layer(tmx_layer)
            elif isinstance(tmx_layer, pytmx.TiledObjectGroup):
                self.__process_object_layer(tmx_layer)
            else:
                raise TypeError("Invalid layer type: %s" % type(tmx_layer))

    def load_resources(self):
        """
        Load the resources for the map.
        """
        try:
            # Clean the mapping dictionary
            self.__initialize_tmx_summary()
            # Load the map file
            self.__load_map_file()
            # Process the map layers and extract recurrent information
            self.__process_map_layers()
        except Exception as error:
            raise AttributeError(
                "Error loading the map file %s: %s" % 
                (self.tmx_file, error)
            )

    def __get_gid_from_layer(self, tmx_layer: pytmx.TiledTileLayer, position: Tuple[int, int]):
        layer_walkable_index = self.tmx_map.layers.index(tmx_layer)

        tile_x, tile_y = self.get_coordinates(position)
        tile_gid = self.tmx_map.get_tile_gid(tile_x, tile_y, layer_walkable_index)

        return tile_gid
    
    def __is_invalid_position(self, position: Tuple[int, int]):
        """
        Return if the position is invalid.

        Args:
            position (Tuple[int, int]): Position to check. Position coordinates are in pixels.
        """
        x, y = position
        
        if x < 0 or y < 0:
            return True
        
        if x >= self.size_w or y >= self.size_h:
            return True
        
        return False
    
    def is_walkable(self, position: Tuple[int, int]) -> bool:
        """
        Check if the position is a floor.

        Args:
            position (Tuple[int, int]): Position to check. Position coordinates are in pixels.
        
        Returns:
            bool: True if the position is a floor, False otherwise.
        """
        if self.__is_invalid_position(position):
            return False
        
        layer_walkable = self.tmx_summary.get(self.LAYER_WALKABLE, None)

        if layer_walkable is None:
            return False

        tile_gid = self.__get_gid_from_layer(layer_walkable, position)
    
        return tile_gid != self.GID_EMPTY
        


    def is_obstacle(self, position: Tuple[int, int]) -> bool:
        """
        Check if the position is an obstacle.

        Args:
            position (Tuple[int, int]): Position to check. Position coordinates are in pixels.
        
        Returns:
            bool: True if the position is an obstacle, False otherwise.
        """
        if self.__is_invalid_position(position):
            return False
        
        layer_obstacle = self.tmx_summary.get(self.LAYER_OBSTACLE, None)

        if layer_obstacle is None:
            return False

        tile_gid = self.__get_gid_from_layer(layer_obstacle, position)
    
        return tile_gid != self.GID_EMPTY
    
    def is_asset(self, position: Tuple[int, int]) -> bool:
        """
        Check if the position is a asset.
        """
        raise NotImplementedError("is_asset method must be implemented in the subclass")
    
    def get_coordinates(self, position: Tuple[int, int]) -> Tuple[int, int]:
        """
        Get the coordinates of the position.
        """
        x, y = position
        return (x // self.tile_w, y // self.tile_h)
    
    def update_state(self):
        """
        Update the state of the map.
        """
        raise NotImplementedError("update_state method must be implemented in the subclass")
    
    def render_map(self):
        """
        Render the map on the screen.
        """
        min_x, min_y, max_x, max_y = self.get_visible_area()
        """
        Draw Map Layer
        """
        for map_layer in self.tmx_map.visible_layers:
            """
            En visible layers se muestran también las agrupadas en assets
            """
            if isinstance(map_layer, pytmx.TiledTileLayer):
                for x, y, tile_obj in map_layer.tiles():
                    try:
                        pixel_x = x * self.tile_w
                        pixel_y = y * self.tile_h
                        x_in_range = pixel_x >= min_x and pixel_x <= max_x
                        y_in_range = pixel_y >= min_y and pixel_y <= max_y 

                        if x_in_range and y_in_range:
                            map_coordinates = (
                                    (x * self.tile_w),
                                    (y * self.tile_h)
                            )
                            print(f"Painting ({x, y}) at {map_coordinates}")
                            self.game_surface.blit(tile_obj, map_coordinates)
                    except TypeError:
                        log.error("Error drawing tile %s" % tile_obj)

    def get_visible_area(self):
        """
        Get the visible area of the map.

        Returns:
            Tuple[int, int, int, int]: 
                A tuple with the coordinates of the visible area. (min_x, min_y, max_x, max_y)
        """
        min_x = max(0, self.center_x - self.game_surface.get_width() // 2)
        min_y = max(0, self.center_y - self.game_surface.get_height() // 2)

        max_x = min_x + self.game_surface.get_width()
        max_y = min_y + self.game_surface.get_height()

        return (min_x, min_y, max_x, max_y)

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
        self.center_x = x
        self.center_y = y
    
    def distance_to_border(self, position):
        """
        Get the distance of the position to the anchor.

        This method is used to get the distance of the position to the anchor.
        """
        raise NotImplementedError("distance_to_anchor method must be implemented in the subclass")