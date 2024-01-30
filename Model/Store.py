import random

from Model.GameConfig import GameConfig
from Model.Inventory import Item
from Model.Potion import Potion


class Good:
    @staticmethod
    def NoneGood():
        return Good(Item(name="Empty", count=1), 1)

    def Equal(self, good):
        if good.Cost != self.Cost:
            return False
        if good.Item.GetName() != self.Item.GetName():
            return False
        return True

    def __init__(self, item: Item, cost: int):
        self.Item = item
        self.Cost = cost


class Store:
    def BuyItem(self, good: Good, count: int):
        if good.Equal(Good.NoneGood()):
            return
        if self.Goods.count(good) == 0:
            raise ValueError(f"Goods not contained {good}")
        if good.Cost * count > self.Config.Coins:
            print("low coin")
            return
        if count > good.Item.GetCount():
            print(count, good.Item.GetCount())
            return
        self.Config.GameInventory.AddItem(good.Item.PopItem(count))
        print(self.Config.GameInventory.GetItems())
        self.Config.Coins -= good.Cost * count
        if good.Item.GetCount() == 0:
            good = Good.NoneGood()
        self.__OnGoodsChanged()

    def __init__(self, config: GameConfig):
        self.Config = config
        self.Goods = self.__GetRandomGoods(45)
        self.OnGoodsChanged = list()

    def __GetRandomGoods(self, count: int) -> list:
        goods = list()
        for i in range(count):
            item = Potion(name=f"Товар #{i}", count=random.randint(1, 100), health=random.randint(-50, 50), armor=random.randint(-50, 50))
            good = Good(item, random.randint(10, 500))
            goods.append(good)
        return goods

    def __OnGoodsChanged(self):
        for observer in self.OnGoodsChanged:
            observer()
