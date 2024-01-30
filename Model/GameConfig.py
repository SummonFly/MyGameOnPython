import pickle
from Model.Inventory import Inventory


class GameConfig:
    def Load(self):
        try:
            with open(self.Path, "rb") as file:
                obj = pickle.load(file)
                self.Coins = obj.Coins
                self.GameInventory = obj.GameInventory
                self.Player = obj.Player
        except FileNotFoundError as e:
            print(e)

    def Save(self):
        with open(self.Path, "wb") as file:
            pickle.dump(self, file)

    def __init__(self, path: str):
        self.Path = path
        self.Player = None
        self.GameInventory = Inventory()
        self.Coins = 100_000_000
