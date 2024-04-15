from Model.GameConfig import GameConfig
from Model.Store import Store
from Model.Profile import Profile
from Model.Fighting import FightingSetup

from Model.Damageable import Player
from Model.Weapon import Weapon

from kivy.lang.builder import Builder


class GameManager:
    __configPath = "GameConfig.json"

    def __init__(self):
        self.Config = GameConfig(self.__configPath)
        self.Config.Load()
        Builder.load_file("View/Styles.kv")
        self.Store = Store(self.Config)
        self.Profile = Profile(self.Config)

        if not self.Config.Player:
            self.Config.Player = Player()

        if not self.Config.Player.Weapon:
            self.Config.Player.Weapon = Weapon()

        self.FightingSetup = FightingSetup(self.Config.Player)
