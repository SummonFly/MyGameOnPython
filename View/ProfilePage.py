from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
import globalVariable as gv


class ProfilePage(Screen):
    def __init__(self, **kwargs):
        super(ProfilePage, self).__init__(**kwargs)
        btn = Button(text="toMain")
        btn.bind(on_press=self.OnPressMain)
        self.add_widget(btn)

    def OnPressMain(self, *args):
        gv.screenManager.current = "main"
