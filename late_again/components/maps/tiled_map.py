
class Scene:
    def __init__(
        self,
        grid_size,
        drawable_surface_x,
        drawable_surface_y,
        user_interface,
        map_file,
    ):
        self.map_data = load_pygame(map_file)
        self.user_interface = user_interface
        self.grid_size = grid_size
        self.drawable_surface_x = drawable_surface_x
        self.drawable_surface_y = drawable_surface_y

    def is_walkable(self, x, y):
        if x < 0 or y < 0:
            return False
        """
        Esto lo que hace es comprobar si se puede caminar 
        """
        base_layer = self.map_data.get_layer_by_name("Base")
        base_layer_index = self.map_data.layers.index(base_layer)
        tile_gid_info = self.map_data.get_tile_gid(x, y, base_layer_index)
        if tile_gid_info != 0:
            return True
        return False
        

    def is_colliding(self, x, y):
        """
        Se define como collision aquella en la que la capa tiene la propiedad Asset.
        Esto se puede generar al principio.
        """
        asset_layers = [
            asset for asset in self.map_data.visible_layers 
            if ('Asset' in asset.properties and asset.properties['Asset'])
        ]

        for asset_obj in asset_layers:
            asset_obj_index = self.map_data.layers.index(asset_obj)
            gid_id = self.map_data.get_tile_gid(x, y, asset_obj_index)
            if gid_id != 0:
                return (True, asset_obj)
        return (False, None)

    def visible_range(self, player_position):
        min_x = max(0, player_position[0] - self.drawable_surface_x // 2)
        min_y = max(0, player_position[1] - self.drawable_surface_y // 2)
        return min_x, min_y

    def render(self, screen: "pygame.Surface", player_position):
        min_x, min_y = self.visible_range(player_position)
        max_x, max_y = min_x + self.drawable_surface_x, min_y + self.drawable_surface_y

        """
        Draw Map Layer
        """
        for map_layer in self.map_data.visible_layers:
            """
            En visible layers se muestran también las agrupadas en assets
            """
            if isinstance(map_layer, pytmx.TiledTileLayer):
                for x, y, tile_obj in map_layer.tiles():
                    try:
                        x_in_range = x >= min_x and x <= max_x
                        y_in_range = y >= min_y and y <= max_y 
                        if x_in_range and y_in_range:
                            map_coordinates = (
                                    (x - min_x) * self.grid_size,
                                    (y - min_y) * self.grid_size
                            )
                            screen.blit(tile_obj, map_coordinates)
                    except TypeError:
                        print(x, y, tile_obj)

    def handle_interaction(self, player, asset):
        self.user_interface: UserInterfaceInteractive
        self.user_interface.ui_dialog_panel.show()
        self.user_interface.update_dialog(f"New interaction with {asset.name}")
        self.user_interface.enable_action_buttons({})
        
    def clear_interaction(self, player):
        self.user_interface: UserInterfaceInteractive
        self.user_interface.ui_dialog_panel.hide()

    def update(self, player, key_event):
        pass  # No update needed for the scene in this example, but you can add more logic here if needed.




class TileMap:
    """
    TileMap class

    TileMap class is a wrapper for the pytmx.TiledMap class. It is used to load
    the Tiled map file and render the map on the screen. It also provides
    methods to access different layers of the map using the collide method.

    It also ensures the map is rendered in the center of the screen and 
    the player is always in the center of the map.
    """

    def __init__(self, game_engine: GameEngine, map_file: str) -> None:
        self.game_engine = game_engine
        self.map_file = map_file

    def load_resources(self):
        """
        Load map and prepare map layers for rendering.
        """
        self.tiled_map = pytmx.load_pygame(self.map_file)
        self.map_width = self.tiled_map.width * self.tiled_map.tilewidth
        self.map_height = self.tiled_map.height * self.tiled_map.tileheight
        self.map_surface = pygame.Surface((self.map_width, self.map_height))
        self.map_surface.fill((255, 255, 255))
        self.map_surface.set_colorkey((255, 255, 255))
        self.map_surface.convert_alpha()

        self.map_layers = []
        for layer in self.tiled_map.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                self.map_layers.append(layer)
        
        self.map_layers.sort(key=lambda x: x.properties.get('z', 0))

    def render(self, screen: pygame.Surface, player: Player) -> None:
        """
        Render the map on the screen.
        """
        self.map_surface.fill((255, 255, 255))
        for layer in self.map_layers:
            for x, y, gid in layer:
                tile = self.tiled_map.get_tile_image_by_gid(gid)
                if tile:
                    self.map_surface.blit(tile, (x * self.tiled_map.tilewidth, y * self.tiled_map.tileheight))

        screen.blit(self.map_surface, self.get_map_position(player))
