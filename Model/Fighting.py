import random

from Model.Damageable import Player
from Model.Weapon import Weapon
from Model.Inventory import Inventory, Item


class FightingPresets:
    pass


class Fighting:
    pass


class FightingSetup:
    def __init__(self):
        self.MaxHealth = 900
        self.MinHealth = 1
        self.MaxArmor = 100
        self.MinArmor = 900
        self.MaxDamage = 100
        self.MinDamage = 1
        self.__fighting = None

    def SetPresets(self):
        pass

    def GetFighting(self, player: Player) -> Fighting:
        pass

    def __GeneratePlayer(self) -> Player:
        player = Player(random.randint(self.MinHealth, self.MaxHealth), random.randint(self.MinArmor, self.MaxArmor))
        player.Weapon = Weapon(damage=random.randint(self.MinDamage, self.MaxDamage),
                               speed=random.randint(1, 3),
                               multiplier=random.randint(0, 3),
                               chance=random.randint(0, 45)/100)
        player.Inventory = Inventory()
        player.Inventory.AddItem(Item("Тестовый Item 2.0", 32))
        player.Inventory.AddItem(Item("Тестовый Item 2.5", 47))
        return player
