from kivy.uix.boxlayout import BoxLayout
from  kivy.uix.label import Label

from Model.Potion import Potion
from Model.Inventory import Item

from functools import singledispatchmethod


class GoodStatsView:

    @singledispatchmethod
    def GetView(self, target) -> BoxLayout:
        box = BoxLayout()
        box.add_widget(Label(text=f"Error of type"))
        return box

    @GetView.register(Potion)
    def _(self, target) -> BoxLayout:
        box = BoxLayout(orientation="vertical")
        box.add_widget(Label(text=f"Name: {target.GetName()}"))
        box.add_widget(Label(text=f"Count: {target.GetCount()}"))
        box.add_widget(Label(text=f"Armor: {target.Armor}"))
        box.add_widget(Label(text=f"Health: {target.Health}"))
        return box

    @GetView.register(Item)
    def _(self, target) -> BoxLayout:
        box = BoxLayout(orientation="vertical")
        box.add_widget(Label(text=f"Name: {target.GetName()}"))
        box.add_widget(Label(text=f"Count: {target.GetCount()}"))
        return box
