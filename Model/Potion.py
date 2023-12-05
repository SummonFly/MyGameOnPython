from Model.Damageable import *
from Model.Inventory import *


class Potion(DamageableImprovement, Item):
    def __init__(self, name: str, count: int = 1, maxCount: int = -1, health: int = 0, armor: int = 0):
        DamageableImprovement.__init__(self, health, armor)
        Item.__init__(self, name, count, maxCount)
