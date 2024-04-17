import json
import random

from Model.GameConfig import GameConfig
from Model.Inventory import Item
from Model.Potion import Potion
from Model.Weapon import WeaponItem


class Good:
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
        if good is None:
            return
        if self.Goods.count(good) == 0:
            raise ValueError(f"Goods not contained {good}")
        if good.Cost * count > self.Config.Coins:
            print("low coin")
            return
        if count > good.Item.GetCount():
            print(count, good.Item.GetCount())
            return
        self.Config.Player.Inventory.AddItem(good.Item.PopItem(count))
        self.Config.Coins -= good.Cost * count
        if good.Item.GetCount() == 0:
            good = None
        self.__OnGoodsChanged()

    def __init__(self, config: GameConfig):
        self.Config = config
        self.Goods = self.__GetRandomGoodsPotion(45)
        self.Goods += self.__GetRandomGoodsWeapon(60)
        self.OnGoodsChanged = list()

    def __LoadPotionsList(self, path: str) -> list:
        with open(file=path, mode="r") as file:
            data = json.loads(file.read())
        return data

    def __GetRandomGoodsPotion(self, count: int) -> list:
        goods = list()
        potions = self.__LoadPotionsList(self.Config.PotionPath)
        for i in range(count):
            data = random.choice(potions)
            data["_count"] = random.randint(5, 27)
            potion = Potion(data)
            goods.append(Good(potion, random.randint(83, 124)))
        return goods

    def __GetRandomGoodsWeapon(self, count: int) -> list:
        goods = list()
        for i in range(count):
            item = WeaponItem(name=f"Товар Weapon#{i}", count=random.randint(1, 100), damage=random.randint(2, 50), speed=random.randint(0, 50))
            good = Good(item, random.randint(10, 500))
            goods.append(good)
        return goods

    def __OnGoodsChanged(self):
        for observer in self.OnGoodsChanged:
            observer()
