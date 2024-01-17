from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
import globalVariable as globalVar
from kivy.uix.colorpicker import ColorPicker

from Model.Store import Store


class StorePage(Screen):
    def __init__(self, store: Store, **kwargs):
        super(StorePage, self).__init__(**kwargs)
        self.__store = store
        self.__initView()

    def __initView(self):
        box = BoxLayout()
        box.add_widget(Button(text="Store", on_press=self.OnPressMain))
        box.add_widget(ColorPicker())
        self.add_widget(box)

    def OnPressMain(self, *args):
        globalVar.screenManager.current = "main"
