from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import globalVariable as globalVar

from Model.Profile import Profile


class ProfilePage(Screen):
    def __init__(self, profile: Profile, **kwargs):
        super(ProfilePage, self).__init__(**kwargs)
        self.__profile = profile
        self.__initView()

    def __initView(self):
        box = BoxLayout()
        box.add_widget(Button(text="toMain", on_press=self.OnPressMain))
        self.add_widget(box)

    def OnPressMain(self, *args):
        globalVar.screenManager.current = "main"
