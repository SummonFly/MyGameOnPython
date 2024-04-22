from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color
from kivy.utils import *


class PROBoxLayout:
    pass


class PROLabel(Label):
    def __init__(self, **kwargs):
        try:
            color = kwargs.pop("backgroundColor")
        except KeyError as e:
            color = (0, 0, 0)
            print(e)
        super().__init__(**kwargs)
        if color[0] == '#':
            self.backgroundColor = get_color_from_hex(color)
        else:
            self.backgroundColor = Color(*color).rgb
        self.on_size()

    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*self.backgroundColor),
            Rectangle(pos=self.pos, size=self.size)


