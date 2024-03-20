from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty


class SliderWithEntry(GridLayout):
    slider_val = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.Value = 0
        self.textInput = TextInput(size_hint=(0.2, 1), text=str(self.slider_val))
        self.slider = Slider(size_hint=(0.8, 1), step=1)
        self.slider.fbind('value', self.on_slider_val)

        self.add_widget(self.slider)
        self.add_widget(self.textInput)

    def on_slider_val(self, instance, val):
        self.textInput.text = str(val)
