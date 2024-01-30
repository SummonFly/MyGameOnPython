from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
import globalVariable as globalVar

from Model.Profile import Profile
from Model.Inventory import Inventory, Item


class ProfilePage(Screen):
    def __init__(self, profile: Profile, **kwargs):
        super(ProfilePage, self).__init__(**kwargs)
        self.__profile = profile
        self.__initView()

    def __initView(self):
        main = BoxLayout(orientation="vertical", size_hint=(1, 1))
        main.add_widget(Button(text="toMain", size_hint=(1, 0.1), on_press=self.OnPressMain))

        second = BoxLayout(size_hint=(1, 0.9))

        inventory = BoxLayout(size_hint=(0.5, 1), orientation="vertical")

        self.__inventoryScroll = ScrollView(bar_width=20, size_hint=(1, 1), size=Window.size)
        self.__inventoryScroll.add_widget(self.__GetInventoryView(self.__profile.Config.GameInventory))
        inventory.add_widget(self.__inventoryScroll)
        second.add_widget(inventory)

        itemStats = BoxLayout(orientation="vertical", size_hint=(0.5, 1))
        self.__statsScroll = ScrollView(size_hint=(1, 0.7), size=Window.size)

        second.add_widget(itemStats)

        main.add_widget(second)
        self.add_widget(main)

    @staticmethod
    def __GetInventoryView(inventory: Inventory) -> GridLayout:
        listItem = BoxLayout(orientation="vertical", size_hint=(1, None), spacing=5)
        for item in inventory.GetItems():
            listItem.add_widget(Button(text=f"{item.GetName()}", height=80, size_hint_y=None, background_color=globalVar.buttonColor))
        listItem.height = 80 * len(inventory.GetItems())
        return listItem

    @staticmethod
    def __GetItemStatsView(item: Item) -> BoxLayout:
        box = BoxLayout()
        box.add_widget(Button(text="Item"))
        return box

    @staticmethod
    def OnPressMain(*args):
        globalVar.screenManager.current = "main"

    def Update(self):
        self.__inventoryScroll.clear_widgets()
        self.__inventoryScroll.add_widget(self.__GetInventoryView(self.__profile.Config.GameInventory))
