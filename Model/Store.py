from Model.GameConfig import GameConfig
from Model.Inventory import Item


class Good:
    def __init__(self, item: Item, cost: int):
        self.Item = item
        self.Cost = cost


class Store:
    def BuyItem(self, good: Good, count: int):
        pass

    def __init__(self, config: GameConfig):
        self.Config = config
        self.Goods = list()
