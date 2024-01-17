from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
import globalVariable as globalVar


class SettingsPage(Screen):
    def __init__(self, **kwargs):
        super(SettingsPage, self).__init__(**kwargs)
        btn = Button(text="toMain")
        btn.bind(on_press=self.OnPressMain)
        self.add_widget(btn)

    def OnPressMain(self, *args):
        globalVar.screenManager.current = "main"
