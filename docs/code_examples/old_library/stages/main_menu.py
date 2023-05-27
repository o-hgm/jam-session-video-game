from jam_session.lib.entities.stage import Stage
from jam_session.lib.entities import asset


class MainMenuStage(Stage):
    def load_assets(self):
        game_title = asset.from_image_resource('./jam_session/resources/sprites/scene_start_game_title.png', y_origin=200)
        return [game_title]