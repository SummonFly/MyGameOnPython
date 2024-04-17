from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
import globalVariable as globalVar

from Model.Profile import Profile
from Model.Inventory import Inventory, Item
from View.Drawer import Drawer


class ProfilePage(Screen):
    def __init__(self, profile: Profile, **kwargs):
        super(ProfilePage, self).__init__(**kwargs)
        self.__profile = profile
        self.__currentItem = None
        self.__initView()

    def __initView(self):
        main = BoxLayout(orientation="vertical", size_hint=(1, 1), spacing=6)
        main.add_widget(Button(text="toMain",
                               size_hint=(1, 0.1),
                               on_press=self.OnPressMain,
                               background_color=globalVar.buttonColor,
                               color=globalVar.buttonTextColor))

        second = BoxLayout(size_hint=(1, 0.9), spacing=6)

        inventory = BoxLayout(size_hint=(0.5, 1), orientation="vertical")

        self.__inventoryScroll = ScrollView(bar_width=20, size_hint=(1, 1), size=Window.size)
        self.__inventoryScroll.add_widget(self.__GetInventoryView(self.__profile.Config.GameInventory))
        inventory.add_widget(self.__inventoryScroll)
        second.add_widget(inventory)

        itemStats = BoxLayout(orientation="vertical", size_hint=(0.5, 1))
        self.__statsScroll = ScrollView(size_hint=(1, 0.7), size=Window.size)
        itemStats.add_widget(self.__statsScroll)

        second.add_widget(itemStats)

        main.add_widget(second)
        self.add_widget(main)

    def __GetItemButtonCrutch(self, item: Item) -> Button:
        return Button(text=f"{item.GetName()}", on_press=lambda *args: self.OnPressItem(item),
                      height=80, size_hint_y=None, background_color=globalVar.buttonColor,
                      color=globalVar.buttonTextColor)

    def __GetInventoryView(self, inventory: Inventory) -> GridLayout:
        listItem = BoxLayout(orientation="vertical", size_hint=(1, None), spacing=5)
        for item in inventory.GetItems():
            listItem.add_widget(self.__GetItemButtonCrutch(item))
        listItem.height = 80 * len(inventory.GetItems())
        return listItem

    @staticmethod
    def OnPressMain(*args):
        globalVar.screenManager.current = "main"

    def OnPressItem(self, item):
        self.__currentItem = item
        self.__UpdateStatsView(item)

    def __UpdateStatsView(self, item: Item):
        self.__statsScroll.clear_widgets()
        self.__statsScroll.add_widget(Drawer().GetView(item))

    def Update(self):
        self.__inventoryScroll.clear_widgets()
        self.__inventoryScroll.add_widget(self.__GetInventoryView(self.__profile.Config.GameInventory))
