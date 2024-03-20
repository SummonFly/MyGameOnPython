from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
import globalVariable as globalVar
from View.PROLabel import PROLabel


class FightingSetupPage(Screen):
    def __init__(self, **kwargs):
        super(FightingSetupPage, self).__init__(**kwargs)
        box = BoxLayout(orientation="vertical")

        box.add_widget(Button(text="Menu", on_press=self.OnPressMain, size_hint_y=0.05))



        self.add_widget(box)

    def OnPressMain(self, *args):
        globalVar.screenManager.current = "main"
