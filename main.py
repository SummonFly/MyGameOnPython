from Model.Inventory import *
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.app import App
from kivy.graphics import Color, Rectangle


class ItemConstructor(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__nameInput = TextInput(multiline=False)
        self.__countInput = TextInput(multiline=False)
        self.__maxCountInput = TextInput(multiline=False)
        layout = GridLayout()
        layout.cols = 2
        layout.add_widget(Label(text="Тип предмета"))
        layout.add_widget(self.__nameInput)
        layout.add_widget(Label(text="Колличество"))
        layout.add_widget(self.__countInput)
        layout.add_widget(Label(text="Максимальное колличество"))
        layout.add_widget(self.__maxCountInput)
        self.add_widget(layout)

    def GetItem(self):
        return Item(self.__nameInput.text, int(self.__countInput.text), int(self.__maxCountInput.text))

class ItemWidget(Widget):
    def __init__(self, item: Item, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout()
        layout.add_widget(Label(text=item.GetName()))
        layout.add_widget(Label(text=str(item.GetCount())))
        layout.add_widget(Label(text=str(item.GetMaxCount())))
        self.add_widget(layout)


class GameApp(App):
    def __init__(self, inventory: Inventory, **kwargs):
        super().__init__(**kwargs)
        self.stack = StackLayout()
        self.stack.orientation = "lr-tb"
        self.stack.spacing = (10, 10)
        for item in inventory.GetItems():
            self.stack.add_widget(ItemWidget(item))

    def build(self):
        layout = BoxLayout()
        layout.orientation = "vertical"
        layout.add_widget(ItemConstructor())
        layout.add_widget(self.stack)
        return ItemConstructor()


if __name__ == "__main__":
    inventory = Inventory()
    inventory.AddItem(Item("Item", 8, 10))
    GameApp(inventory).run()
