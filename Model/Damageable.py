import random
from Model.Weapon import *
from Model.Improve import *
from Model.Inventory import *


class IDamageable(IImproveable):
    def __init__(self, health: int = 20, armor: int = 1):
        if(health <= 0 or armor < 0):
            raise ValueError(health, armor)
        self.Health = health
        self.Armor = armor

    def AceptDamage(self, weapon: Weapon):
        multiplier = weapon.CritDamageMultiplier if random.randint(0, 100) <= weapon.CritChance * 100 else 0
        additionDamage = weapon.Damage * multiplier
        cleanDamage = (weapon.Damage - self.Armor) * weapon.Speed if weapon.Damage > self.Armor else 0
        damage = cleanDamage + additionDamage
        
        if(damage > 0):
            if(self.Health > damage):
                self.Health -= damage
            else:
                self.Health = 0


class DamageableImprovement(IImprovement):
    def __init__(self, health: int = 0, armor: int = 0):
        self.Health = health
        self.Armor = armor

    def Accept(self, obj: IDamageable):
        obj.Health += self.Health
        obj.Armor += self.Armor


class Player(IDamageable):
    def __init__(self, health: int = 20, armor: int = 1):
        IDamageable.__init__(self, health, armor)
        self.Inventory = Inventory()
        self.Weapon = Weapon()

