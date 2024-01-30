from Model.GameConfig import GameConfig


class Profile:
    def __init__(self, config: GameConfig):
        self.Config = config
        self.FirstItem = None
        self.SecondItem = None
