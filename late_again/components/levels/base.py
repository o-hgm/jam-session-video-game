class GameLevel:
    """
    Base class for all game levels.
    """

    def __init__(self, *args, **kwargs) -> None:
        self.game_map = None
        # self.level_assets = []