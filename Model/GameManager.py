from Model.GameConfig import GameConfig
from Model.Store import Store
from Model.Profile import Profile


class GameManager:
    __configPath = "GameConfig.json"

    def __init__(self):
        self.Config = GameConfig(self.__configPath)
        self.Config.Load()
        self.Store = Store(self.Config)
        self.Profile = Profile(self.Config)
