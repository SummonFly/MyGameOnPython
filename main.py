from kivy.app import App

from View.MainPage import *
from View.FightingSetupPage import *
from View.StorePage import *
from View.ProfilePage import *
from View.SettingsPage import *
import globalVariable as globalVar

from Model.GameManager import GameManager

from Model.Potion import Potion

import json


class GameApp(App):
    def build(self):
        Window.clearcolor = globalVar.mainBackgroundColor
        globalVar.screenManager.add_widget(self.mainPage)
        globalVar.screenManager.add_widget(self.storePage)
        globalVar.screenManager.add_widget(self.fightPage)
        globalVar.screenManager.add_widget(self.profilePage)
        globalVar.screenManager.add_widget(self.settingPage)
        return globalVar.screenManager

    def SaveGame(self):
        self.__gameManager.Config.Save()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__gameManager = GameManager()
        self.mainPage = MainPage(name="main")
        self.storePage = StorePage(self.__gameManager.Store, name="store")
        self.fightPage = FightingSetupPage(name="fight")
        self.profilePage = ProfilePage(self.__gameManager.Profile, name="profile")
        self.settingPage = SettingsPage(name="settings")

'''"\b\w+\s\w+:\n(\b\w+:\s((0)|([+-]{,1}\d+,\s[+-]{,1}\d+,\s[+-]{,1}\d+))(\n|$)){2}"mg'''
'''":\s((0)|([+-]?\d+,\s[+-]?\d+,\s[+-]\d+))"gm'''


class PotionData:
    Name = None
    Health = None
    Armor = None

    def Potions(self, potions: list):
        for i in range(3):
            potions.append(Potion(name=self.Name, health=self.Health[i], armor=self.Armor[i]))


def Serialize():
    potions = list()
    data = None
    with open(file="Potion.txt", mode="r", encoding="UTF-8") as file:
        data = file.read().split('\n')
    for i in range(int(len(data)/3)):
        potion = PotionData()
        potion.Name = data[i*3]
        potion.Health = [int(val) for val in data[(i*3)+1].split()]
        potion.Armor = [int(val) for val in data[(i*3)+2].split()]
        potion.Potions(potions)

    with open(file="potions.txt", mode="w", encoding="UTF-8") as file:
        file.write(json.dumps(potions, default=lambda o: o.__dict__, sort_keys=True, indent=4))
    with open(file="potions.txt", mode="r", encoding="UTF-8") as file:
        data = json.loads(file.read())
    for i in data:
        print(i)


if __name__ == "__main__":
    globalVar.gameApp = GameApp()
    globalVar.gameApp.run()

