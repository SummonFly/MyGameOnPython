from Inventory import *


class GoodsStore:
    def __init__(self, targetInventory: Inventory):
        self.TargetInventory = targetInventory
        self.Goods = dict()
