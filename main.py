from kivy.app import App

from View.MainPage import *
from View.FightingSetupPage import *
from View.StorePage import *
from View.ProfilePage import *
from View.SettingsPage import *
import globalVariable as globalVar

from Model.GameManager import GameManager


class GameApp(App):
    def build(self):
        Window.clearcolor = globalVar.mainBackgroundColor
        globalVar.screenManager.add_widget(self.mainPage)
        globalVar.screenManager.add_widget(self.storePage)
        globalVar.screenManager.add_widget(self.fightingSetupPage)
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
        self.fightingSetupPage = FightingSetupPage(self.__gameManager.FightingSetup, name="fightingSetup")
        self.profilePage = ProfilePage(self.__gameManager.Profile, name="profile")
        self.settingPage = SettingsPage(name="settings")


if __name__ == "__main__":
    globalVar.gameApp = GameApp()
    globalVar.gameApp.run()

