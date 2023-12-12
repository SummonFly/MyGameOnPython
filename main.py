from View.MainPage import *
from View.FightPage import *
from View.StorePage import *
from View.ProfilePage import *
from View.SettingsPage import *
import globalVariable as gv


class GameApp(App):
    def build(self):
        gv.screenManager.add_widget(MainPage(name="main"))
        gv.screenManager.add_widget(StorePage(name="store"))
        gv.screenManager.add_widget(FightPage(name="fight"))
        gv.screenManager.add_widget(ProfilePage(name="profile"))
        gv.screenManager.add_widget(SettingsPage(name="settings"))
        return gv.screenManager


if __name__ == "__main__":
    gv.init()
    GameApp().run()
