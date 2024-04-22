import pickle
from Model.Inventory import Inventory


class GameConfig:
    def Load(self):
        try:
            with open(self.SavePath, "rb") as file:
                obj = pickle.load(file)
                self.Coins = obj.Coins
                self.GameInventory = obj.GameInventory
                self.Player = obj.Player
        except FileNotFoundError as e:
            print(e)

    def Save(self):
        with open(self.SavePath, "wb") as file:
            pickle.dump(self, file)

    def __init__(self, savePath: str, potionsPath: str = "potions.txt"):
        self.SavePath = savePath
        self.PotionPath = potionsPath
        self.Player = None
        self.GameInventory = Inventory()
        self.Coins = 200
