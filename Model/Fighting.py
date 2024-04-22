import copy
import random

from multipledispatch import dispatch

from Model.Damageable import Player
from Model.GameConfig import GameConfig
from Model.Potion import Potion
from Model.Weapon import Weapon, WeaponImprovementItem
from Model.Inventory import Inventory, Item


class Fighting:
    def __init__(self, player: Player, enemy: Player):
        self.Player = copy.copy(player)
        self.Enemy = enemy
        self.OnGameOver = lambda: print("GameOver")
        self.OnPlayerWin = lambda: print("The player Win")
        self.OnPlayerLost = lambda: print("The player lost")

    def __CheckPlayersHealth(self):
        if self.Player.Health <= 0:
            self.OnGameOver()
            self.OnPlayerLost()
        if self.Enemy.Health <= 0:
            self.OnGameOver()
            self.OnPlayerWin()

    def MakeDamage(self, player: Player, weapon: Weapon):
        player.AcceptDamage(weapon)
        self.__CheckPlayersHealth()

    @dispatch(Player, Potion)
    def MakeEffectAt(self, player: Player, potion: Potion):
        if potion.GetCount() <= 0:
            return
        player.Improve(potion)
        potion.PopItem(1)
        self.__CheckPlayersHealth()

    @dispatch(Weapon, WeaponImprovementItem)
    def MakeEffectAt(self, weapon: Weapon, improvement: WeaponImprovementItem):
        if improvement.GetCount() <= 0:
            return
        weapon.Improve(improvement)
        improvement.PopItem(1)
        self.__CheckPlayersHealth()


class FightingSetup:
    def __init__(self, config: GameConfig):
        self.__player = config.Player
        self.__config = config
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
        self.__fighting.OnPlayerWin = self.OnPlayerWin
        return self.__fighting

    def OnPlayerWin(self):
        health = self.__fighting.Enemy.Health / self.__player.Health
        armor = self.__fighting.Enemy.Armor / self.__player.Armor
        damage = self.__fighting.Enemy.Weapon.Damage / self.__player.Weapon.Damage
        result = health + armor + damage

        if result > 0:
            self.__config.Coins += int(15 * result)
