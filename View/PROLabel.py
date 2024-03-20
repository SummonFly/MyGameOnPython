from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color


class PROLabel(Label):
    def __init__(self, **kwargs):
        color = kwargs.pop("backgroundColor")
        super().__init__(**kwargs)
        self.backgroundColor = Color(*color)
        self.on_size()

    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(self.backgroundColor),
            Rectangle(pos=self.pos, size=self.size)
