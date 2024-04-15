from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.settings import Settings, ConfigParser

import globalVariable as globalVar


class SettingsPage(Screen):
    def __init__(self, **kwargs):
        super(SettingsPage, self).__init__(**kwargs)
        box = BoxLayout(orientation="vertical")
        globalVar.setting.on_close = self.OnPressMain
        globalVar.setting.add_json_panel("Setting panel", config=globalVar.config, filename="View/SettingStructure.json")
        box.add_widget(globalVar.setting)
        self.add_widget(box)

    def OnPressMain(self, *args):
        globalVar.config.write()
        globalVar.screenManager.current = "main"
