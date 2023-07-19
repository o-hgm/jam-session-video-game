import pygame

from typing import Tuple

class MapController:
    """
    Game Map (Base Class)

    A Map represents the game world. It contains all the information about the 
    capabilities of the world, the objects in it.

    A Map representation contains:
        - A Floor Surface: It represents the ground area of the map (Floor)
        - A Obstacle Surface: It represents the non-walkable area of the map.
        - A Asset Surface: It represents the assets of the map.

    Map coordinates are represented by a tuple of integers (x, y) in pixels. Maps may 
    do calculations to convert between pixels and other units.

    Map is linked to a PyGame Surface, which is used to draw the map on the screen.
    """
    def __init__(self, target_surface: pygame.Surface, **kwargs) -> None:
        self.game_surface = target_surface

    def load_resources(self):
        raise NotImplementedError("load_resources method must be implemented in the subclass")
    
    def is_floor(self, position: Tuple[int, int]) -> bool:
        raise NotImplementedError("is_floor method must be implemented in the subclass")
    
    def is_obstacle(self, position: Tuple[int, int]) -> bool:
        raise NotImplementedError("is_obstacle method must be implemented in the subclass")
    
    def is_asset(self, position: Tuple[int, int]) -> bool:
        raise NotImplementedError("is_asset method must be implemented in the subclass")
    
    def get_coordinates(self, position: Tuple[int, int]) -> Tuple[int, int]:
        raise NotImplementedError("get_coordinates method must be implemented in the subclass")
    
    def update_state(self):
        raise NotImplementedError("update_state method must be implemented in the subclass")
    
    def render_map(self):
        raise NotImplementedError("render_map method must be implemented in the subclass")
    
    def get_visible_area(self):
        raise NotImplementedError("get_visible_area method must be implemented in the subclass")
    
    def get_center(self):
        raise NotImplementedError("get_center method must be implemented in the subclass")