from kivy.app import App
from kivy.uix.bubble import Bubble
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
import globalVariable as gv
from kivy.uix.colorpicker import ColorPicker


class StorePage(Screen):
    def __init__(self, **kwargs):
        super(StorePage, self).__init__(**kwargs)
        box = BoxLayout()
        box.add_widget(Button(text="Store", on_press=self.OnPressMain))
        box.add_widget(ColorPicker())
        self.add_widget(box)

    def OnPressMain(self, *args):
        gv.screenManager.current = "main"
