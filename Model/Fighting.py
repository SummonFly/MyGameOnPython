import random

from multipledispatch import dispatch

from Model.Damageable import Player
from Model.Potion import Potion
from Model.Weapon import Weapon, WeaponImprovementItem
from Model.Inventory import Inventory, Item


class Fighting:
    def __init__(self, player: Player, enemy: Player):
        self.Player = player
        self.Enemy = enemy
        self.OnGameOver = lambda: print("GameOver")
        self.OnPlayerWin = lambda: print("The player Win")
        self.OnPlayerLost = lambda: print("The player lost")

    def MakeDamage(self, player: Player, weapon: Weapon):
        player.AcceptDamage(weapon)

    @dispatch(Player, Potion)
    def MakeEffectAt(self, player: Player, potion: Potion):
        player.Improve(potion)
        potion.PopItem(1)

    @dispatch(Weapon, WeaponImprovementItem)
    def MakeEffectAt(self, weapon: Weapon, improvement: WeaponImprovementItem):
        weapon.Improve(improvement)
        improvement.PopItem(1)


class FightingSetup:
    def __init__(self, player: Player):
        self.__player = player
        self.MaxHealth = 900
        self.MinHealth = 1
        self.MaxArmor = 100
        self.MinArmor = 900
        self.MaxDamage = 100
        self.MinDamage = 1
        self.__fighting = None

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

    def GetFighting(self) -> Fighting:
        self.__fighting = Fighting(self.__player, self.__GeneratePlayer())
        return self.__fighting
