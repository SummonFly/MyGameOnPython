from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.sandbox import Sandbox
import globalVariable as globalVar


class SettingsPage(Screen):
    def __init__(self, **kwargs):
        super(SettingsPage, self).__init__(**kwargs)
        box = BoxLayout()
        box.add_widget(Button(text="toMain", on_press=self.OnPressMain))
        box.add_widget(ColorPicker())
        sandbox = Sandbox()
        sandbox.add_widget(box)
        self.add_widget(sandbox)

    def OnPressMain(self, *args):
        globalVar.screenManager.current = "main"
