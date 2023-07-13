import pytmx
import pygame


def render_tmx_map(
        tmx_map: pytmx.TiledMap, 
        target_surface: pygame.Surface,
        min_grid_coord: tuple = (0,0),
        max_grid_coord: tuple = (-1, -1)
        ) -> None:
    
    grid_size_x = tmx_map.tilewidth
    grid_size_y = tmx_map.tileheight
    min_x, min_y = min_grid_coord
    max_x, max_y = max_grid_coord

    """
    Draw Map Layer
    """
    for map_layer in tmx_map.visible_layers:
        """
        En visible layers se muestran también las agrupadas en assets
        """
        if isinstance(map_layer, pytmx.TiledTileLayer):
            for x, y, tile_obj in map_layer.tiles():
                x_in_range = x >= min_x and x <= max_x
                y_in_range = y >= min_y and y <= max_y 
                if x_in_range and y_in_range:
                    map_coordinates = (
                            (x - min_x) * grid_size_x,
                            (y - min_y) * grid_size_y
                    )
                    target_surface.blit(tile_obj, map_coordinates)
    