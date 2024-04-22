import copy


class Item:
    def __init__(self, name: str, count: int, maxCount: int = -1):
        self._name = name
        self._count = abs(count)
        self._maxCount = self._count if abs(maxCount) == -1 else abs(maxCount)

    def GetName(self):
        return self._name

    def GetCount(self):
        return self._count

    def GetMaxCount(self):
        if self._count > self._maxCount:
            self._maxCount = self._count
        return self._maxCount

    def PopItem(self, count: int):
        count = abs(count)
        if self._count < count:
            raise ValueError(count)
        item = copy.deepcopy(self)
        item._maxCount = count
        item._count = count
        self._count -= count
        return item

    def PushItem(self, item):
        if item.GetName() != self._name:
            raise ValueError(f"Name of {item}")
        if self.IsFill():
            return item
        emptySpace = self._maxCount - self._count
        if emptySpace > item.GetCount():
            self._count += item.GetCount()
            item.PopItem(item.GetCount())
            return item
        else:
            self._count = self._maxCount
            item.PopItem(emptySpace)
            return item

    def IsFill(self) -> bool:
        return self._count == self._maxCount


class Inventory:
    def __init__(self):
        self.__items = list()

    def GetItems(self) -> list:
        self.__DeleteNones()
        return self.__items.copy()

    def AddItem(self, obj: Item):
        item = copy.deepcopy(obj)
        for i in filter(lambda a: a.GetName() == item.GetName() and not a.IsFill(), self.__items):
            i.PushItem(item)
            if item.GetCount() == 0:
                break
        if item.GetCount() > 0:
            self.__items.append(item)
        self.__DeleteNones()

    def RemoveReference(self, item):
        if item in self.__items:
            self.__items.remove(item)

    def RemoveItem(self, item: Item):
        for i in filter(lambda a: a.GetName() == item.GetName(), self.__items):
            if i.GetCount() > item.GetCount():
                i.PopItem(item.GetCount())
                item.PopItem(item.GetCount())

            else:
                item.PopItem(i.GetCount())
                i.PopItem(i.GetCount())
                if i.GetCount() == 0:
                    self.__items.remove(i)
            if item.GetCount() == 0:
                break
        self.__DeleteNones()

    def __DeleteNones(self):
        for item in self.__items:
            if item is None:
                self.__items.remove(item)
            elif item.GetCount() == 0:
                self.__items.remove(item)

    def Clear(self):
        self.__items = list()
