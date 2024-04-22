from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
import globalVariable as globalVar

from Model.Profile import Profile
from Model.Inventory import Inventory, Item
from Model.Weapon import Weapon, WeaponItem, WeaponImprovementItem
from View.Drawer import Drawer
from View.PROWidget import PROLabel


class ProfilePage(Screen):
    def __init__(self, profile: Profile, **kwargs):
        super(ProfilePage, self).__init__(**kwargs)
        self.__profile = profile
        self.__currentItem = None
        self.__initViewTest()

    def __initViewTest(self):
        main = BoxLayout(orientation="vertical", size_hint=(1, 1), spacing=6)
        main.add_widget(Button(text="toMain",
                               size_hint=(1, 0.1),
                               on_press=self.OnPressMain,
                               background_color=globalVar.buttonColor,
                               color=globalVar.buttonTextColor))

        secondaryBox = BoxLayout(size_hint=(1, 0.9), spacing=6)

        self.__inventory = BoxLayout(size_hint=(0.3, 1))
        self.__inventory.add_widget(self.__GetInventoryView(self.__profile.Config.GameInventory))
        secondaryBox.add_widget(self.__inventory)

        secondarySubBox = BoxLayout(orientation='vertical', size_hint=(0.3, 1))

        secondarySubBox.add_widget(self.__GetToolPanel())

        self.__stats = BoxLayout(size_hint=(1, 0.5))
        self.__stats.add_widget(self.__GetStatsView(self.__currentItem))
        secondarySubBox.add_widget(self.__stats)

        secondaryBox.add_widget(secondarySubBox)

        self.__playerTab = BoxLayout(size_hint=(0.3, 1),
                                     orientation='vertical',
                                     spacing=5)
        self.__UpdatePlayerTab()
        secondaryBox.add_widget(self.__playerTab)

        main.add_widget(secondaryBox)
        self.add_widget(main)

    def __initView(self):
        main = BoxLayout(orientation="vertical", size_hint=(1, 1), spacing=6)
        main.add_widget(Button(text="toMain",
                               size_hint=(1, 0.1),
                               on_press=self.OnPressMain,
                               background_color=globalVar.buttonColor,
                               color=globalVar.buttonTextColor))

        second = BoxLayout(size_hint=(1, 0.9), spacing=6)

        self.__inventory = BoxLayout(size_hint=(1, 0.3))
        self.__inventory.add_widget(self.__GetInventoryView(self.__profile.Config.GameInventory))
        second.add_widget(self.__inventory)

        itemStats = self.__GetStatsView()

        second.add_widget(itemStats)

        main.add_widget(second)
        self.add_widget(main)

    def __GetToolPanel(self) -> BoxLayout:
        box = BoxLayout(orientation="vertical", size_hint=(1, 0.2), spacing=5)
        box.add_widget(PROLabel(text="TOOLS",
                                backgroundColor=globalVar.labelBackgroundColor,
                                color=globalVar.textColor))
        box.add_widget(Button(text="change inventory",
                              on_press=self.OnPressChangeInventory,
                              size_hint=(1, 1),
                              background_color=globalVar.buttonColor,
                              color=globalVar.buttonTextColor))
        box.add_widget(Button(text="equip a weapon",
                              on_press=self.OnPressUpgradeWeapon,
                              size_hint=(1, 1),
                              background_color=globalVar.buttonColor,
                              color=globalVar.buttonTextColor))
        return box

    def __GetButtonFromItem(self, item: Item) -> Button:
        return Button(text=f"{item.GetName()}", on_press=lambda *args: self.OnPressItem(item),
                      height=80, size_hint_y=None, background_color=globalVar.buttonColor,
                      color=globalVar.buttonTextColor)

    def __GetInventoryView(self, inventory: Inventory, text='Inventory') -> BoxLayout:
        view = BoxLayout(orientation="vertical", size_hint=(1, 1), spacing=5)
        view.add_widget(PROLabel(text=text,
                                 size_hint=(1, 0.1),
                                 backgroundColor=globalVar.labelBackgroundColor,
                                 color=globalVar.textColor))
        listItem = BoxLayout(orientation="vertical", size_hint=(1, None), spacing=5)
        for item in inventory.GetItems():
            listItem.add_widget(self.__GetButtonFromItem(item))
        listItem.height = 80 * (len(inventory.GetItems()) + 1)
        inventoryScroll = ScrollView(bar_width=20, size_hint=(1, 1), size=Window.size)
        inventoryScroll.add_widget(listItem)
        view.add_widget(inventoryScroll)
        return view

    def __GetWeaponStatsView(self, weapon: Weapon) -> BoxLayout:
        box = BoxLayout(orientation='vertical', spacing=5)
        box.add_widget(PROLabel(text="Weapon",
                                size_hint=(1, 0.1),
                                backgroundColor=globalVar.labelBackgroundColor,
                                color=globalVar.textColor))
        box.add_widget(Drawer().GetView(weapon))
        return box

    def __GetStatsView(self, item=None):
        itemStats = BoxLayout(orientation="vertical", size_hint=(1, 1), spacing=5)
        itemStats.add_widget(PROLabel(text="Stats",
                                      size_hint=(1, 0.1),
                                      color=globalVar.textColor,
                                      backgroundColor=globalVar.labelBackgroundColor))
        statsScroll = ScrollView(size_hint=(1, 1), size=Window.size)
        statsScroll.add_widget(Drawer().GetView(item))
        itemStats.add_widget(statsScroll)
        return itemStats

    def OnPressChangeInventory(self, *args):
        if self.__currentItem in self.__profile.Config.GameInventory.GetItems():
            self.__profile.Config.GameInventory.RemoveReference(self.__currentItem)
            self.__profile.Config.Player.Inventory.AddItem(self.__currentItem)
        elif self.__currentItem in self.__profile.Config.Player.Inventory.GetItems():
            self.__profile.Config.Player.Inventory.RemoveReference(self.__currentItem)
            self.__profile.Config.GameInventory.AddItem(self.__currentItem)
        self.__UpdatePlayerTab()
        self.Update()

    def OnPressUpgradeWeapon(self, *args):
        if not isinstance(self.__currentItem, WeaponImprovementItem):
            return
        self.__profile.Config.Player.Weapon.Improve(self.__currentItem)
        self.__currentItem.PopItem(1)
        self.__UpdatePlayerTab()
        self.Update()

    def OnPressMain(self, *args):
        globalVar.screenManager.current = "main"

    def OnPressItem(self, item):
        self.__currentItem = item
        self.__UpdateStatsView(item)

    def __UpdateStatsView(self, item: Item):
        self.__stats.clear_widgets()
        self.__stats.add_widget(self.__GetStatsView(item))

    def __UpdatePlayerTab(self):
        self.__playerTab.clear_widgets()
        self.__playerTab.add_widget(self.__GetWeaponStatsView(self.__profile.Config.Player.Weapon))
        self.__playerTab.add_widget(self.__GetInventoryView(self.__profile.Config.Player.Inventory,
                                                            text='Player Inventory'))

    def Update(self):
        self.__inventory.clear_widgets()
        self.__inventory.add_widget(self.__GetInventoryView(self.__profile.Config.GameInventory))
        self.__UpdatePlayerTab()
