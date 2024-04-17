class GameDB:
    __gameDB = None

    def __new__(cls, *args, **kwargs):
        if cls.__gameDB:
            return cls.__gameDB
        cls.__gameDB = cls.__new__(*args, **kwargs)
        return cls.__gameDB

    def GetPlayer(self):
        pass

    def SavePlayer(self):
        pass

    def GetGameInventory(self):
        pass

    def SaveGameInventory(self):
        pass

    def GetCoins(self):
        pass

    def SaveCoins(self):
        pass

    def GetPotions(self):
        pass

    def GetWeapons(self):
        pass

    def GetPriceList(self):
        pass
