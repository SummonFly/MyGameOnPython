from kivy.app import App
from View.MainPage import *
from View.FightPage import *
from View.StorePage import *
from View.ProfilePage import *
from View.SettingsPage import *
import globalVariable as globalVar

from Model.GameManager import GameManager


class GameApp(App):
    def build(self):
        globalVar.screenManager.add_widget(MainPage(name="main"))
        globalVar.screenManager.add_widget(StorePage(self.__gameManager.Store, name="store"))
        globalVar.screenManager.add_widget(FightPage(name="fight"))
        globalVar.screenManager.add_widget(ProfilePage(self.__gameManager.Profile, name="profile"))
        globalVar.screenManager.add_widget(SettingsPage(name="settings"))
        return globalVar.screenManager

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__gameManager = GameManager()


if __name__ == "__main__":
    GameApp().run()
