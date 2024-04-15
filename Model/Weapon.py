from Model.Improve import *
from Model.Inventory import Item


class Weapon(IImproveable):
    def __init__(self, damage: int = 1, speed: float = 1, multiplier: float = 1, chance: float = 0):
        self.Damage = damage
        self.Speed = speed
        self.CritDamageMultiplier = multiplier
        self.CritChance = chance


class WeaponImprovement(IImprovement):
    def __init__(self, damage: int = 0, speed: float = 0, multiplier: float = 0, chance: float = 0):
        self.Damage = damage
        self.Speed = speed
        self.CritDamageMultiplier = multiplier
        self.CritChance = chance

    def Accept(self, obj: Weapon):
        obj.Damage += self.Damage
        obj.Speed += self.Speed
        obj.CritDamageMultiplier += self.CritDamageMultiplier
        obj.CritChance += self.CritChance


class WeaponItem(Weapon, Item):
    def __init__(self, name: str, count: int = 1, maxCount: int = -1, damage: int = 0, speed: float = 0, multiplier: float = 0, chance: float = 0):
        Item.__init__(self, name, count, maxCount)
        Weapon.__init__(self, damage, speed, multiplier, chance)


class WeaponImprovementItem(WeaponImprovement, Item):
    def __init__(self, name: str, count: int = 1, maxCount: int = -1, damage: int = 0, speed: float = 0, multiplier: float = 0, chance: float = 0):
        Item.__init__(self, name, count, maxCount)
        WeaponImprovement.__init__(self, damage, speed, multiplier, chance)
