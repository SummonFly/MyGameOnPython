import copy


class Item:
    def __init__(self, name: str, count: int, maxCount: int = -1):
        self.__name = name
        self.__count = abs(count)
        self.__maxCount = self.__count if abs(maxCount) == -1 else abs(maxCount)

    def GetName(self):
        return self.__name

    def GetCount(self):
        return self.__count

    def GetMaxCount(self):
        return self.__maxCount

    def PopItem(self, count: int):
        count = abs(count)
        if(self.__count < count):
            raise ValueError(count)
        self.__count -= count
        return Item(self.__name, count, self.__maxCount)

    def PushItem(self, item):
        if(item.GetName() != self.__name):
            raise ValueError(f"Name of {item}")
        if(self.IsFill()):
            return item
        emptySpace = self.__maxCount - self.__count
        if(emptySpace > item.GetCount()):
            self.__count += item.GetCount()
            item.PopItem(item.GetCount())
            return item
        else:
            self.__count = self.__maxCount
            item.PopItem(emptySpace)
            return item


    def IsFill(self) -> bool:
        return self.__count == self.__maxCount


class Inventory:
    def __init__(self):
        self.__items = list()

    def GetItems(self) -> list:
        return self.__items.copy()
    def AddItem(self, obj: Item):
        item = copy.deepcopy(obj)
        for i in filter(lambda i: i.GetName() == item.GetName() and not i.IsFill(), self.__items):
            i.PushItem(item)
            if(item.GetCount() == 0):
                break
        if(item.GetCount() > 0):
            self.__items.append(item)

    def RemoveItem(self, item: Item):
        for i in filter(lambda i: i.GetName() == item.GetName(), self.__items):
            if(i.GetCount() > item.GetCount()):
                i.PopItem(item.GetCount())
                item.PopItem(item.GetCount())


            else:
                item.PopItem(i.GetCount())
                i.PopItem(i.GetCount())
                if(i.GetCount() == 0):
                    self.__items.remove(i)
            if(item.GetCount() == 0):
                break

    def Clear(self):
        self.__items = list()