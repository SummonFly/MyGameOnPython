from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
import globalVariable as globalVar
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window


class MainPage(Screen):
    def __init__(self, **kwargs):
        super(MainPage, self).__init__(**kwargs)
        anchor = AnchorLayout(anchor_x="left", anchor_y="top")
        box = BoxLayout(orientation="vertical", size_hint=(0.2, 0.4), spacing=10, padding=(10, 10))
        box.add_widget(Button(text="PLAY", on_press=self.OnPressFight, background_color=globalVar.buttonRed))
        box.add_widget(Button(text="STORE", on_press=self.OnPressStore, background_color=globalVar.buttonRed))
        box.add_widget(Button(text="PROFILE", on_press=self.OnPressProfile, background_color=globalVar.buttonRed))
        box.add_widget(Button(text="SETTING", on_press=self.OnPressSettings, background_color=globalVar.buttonRed))
        box.add_widget(Button(text="EXIT", on_press=exit, background_color=globalVar.buttonRed))
        anchor.add_widget(box)
        self.canvas.add(Color(200/256, 180/256, 100/256))
        self.canvas.add(Rectangle(size=(Window.size[0], Window.size[1]), source=globalVar.mainBackgroundSource))
        self.add_widget(anchor)

    def OnPressStore(self, *args):
        globalVar.screenManager.current = "store"

    def OnPressFight(self, *args):
        globalVar.screenManager.current = "fight"

    def OnPressProfile(self, *args):
        globalVar.screenManager.current = "profile"

    def OnPressSettings(self, *args):
        globalVar.screenManager.current = "settings"
