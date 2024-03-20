from Model.Damageable import *
from Model.Inventory import *

from multipledispatch import dispatch


class Potion(DamageableImprovement, Item):
    @dispatch(str, int, int, int, int)
    def __init__(self, name: str, count: int = 1, maxCount: int = -1, health: int = 0, armor: int = 0):
        DamageableImprovement.__init__(self, health, armor)
        Item.__init__(self, name, count, maxCount)

    @dispatch(dict)
    def __init__(self, data: dict):
        for key, value in data.items():
            self.__setattr__(key, value)
