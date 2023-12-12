from kivy.uix.screenmanager import Screen
from main import GameApp
from kivy.uix.button import Button
import globalVariable as gv
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window


class MainPage(Screen):
    def __init__(self, **kwargs):
        super(MainPage, self).__init__(**kwargs)
        anchor = AnchorLayout(anchor_x="left", anchor_y="top")
        box = BoxLayout(orientation="vertical", size_hint=(0.2, 0.4), spacing=10, padding=(10, 10))
        box.add_widget(Button(text="PLAY", on_press=self.OnPressFight, background_color=gv.buttonRed))
        box.add_widget(Button(text="STORE", on_press=self.OnPressStore, background_color=gv.buttonRed))
        box.add_widget(Button(text="PROFILE", on_press=self.OnPressProfile, background_color=gv.buttonRed))
        box.add_widget(Button(text="SETTING", on_press=self.OnPressSettings, background_color=gv.buttonRed))
        anchor.add_widget(box)
        with self.canvas:
            Color(200/256, 180/256, 100/256)
            Rectangle(size=(Window.size[0], Window.size[1]), source=gv.mainBackground)
        self.add_widget(anchor)

    def OnPressStore(self, *args):
        gv.screenManager.current = "store"

    def OnPressFight(self, *args):
        gv.screenManager.current = "fight"

    def OnPressProfile(self, *args):
        gv.screenManager.current = "profile"

    def OnPressSettings(self, *args):
        gv.screenManager.current = "settings"
