from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
import globalVariable as globalVar


class FightPage(Screen):
    def __init__(self, **kwargs):
        super(FightPage, self).__init__(**kwargs)
        box = BoxLayout(orientation="vertical")

        box.canvas.add(Color(178/255, 255/255, 255/255))
        box.canvas.add(Rectangle(size=Window.size, pos=box.pos))

        box.add_widget(Button(text="Menu", on_press=self.OnPressMain, size_hint_y=0.05))

        floatLay = FloatLayout(size_hint_y=0.5)
        box.add_widget(floatLay)

        grid = GridLayout(cols=7, size_hint_y=0.3)
        for i in range(21):
            grid.add_widget(Button(text=str(i)))
        box.add_widget(grid)

        self.add_widget(box)

    def OnPressMain(self, *args):
        globalVar.screenManager.current = "main"
