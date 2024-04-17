from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

import globalVariable as globalVar

from Model.Fighting import Fighting
from Model.Damageable import Player
from Model.Potion import Potion
from Model.Weapon import WeaponImprovementItem, Weapon
from Model.Inventory import Inventory, Item

from View.Drawer import Drawer
from View.PROWidget import PROLabel


class FightingPage(Screen):
    def __init__(self, fighting: Fighting, **kwargs):
        super(FightingPage, self).__init__(**kwargs)
        self.__fighting = fighting
        self.__selectedItem = None

        self.__fighting.Player.Inventory.AddItem(WeaponImprovementItem(name="Lolll", damage=34, speed=-5))

        mainBox = BoxLayout(orientation="horizontal", spacing=10)
        leftBox = BoxLayout(orientation="vertical", spacing=6, size_hint=(0.5, 1))
        middleBox = BoxLayout(orientation="vertical", spacing=3)
        rightBox = BoxLayout(orientation="vertical", spacing=6, size_hint=(0.5, 1))

        self.__playerStats = BoxLayout()
        self.__playerStats.add_widget(self.__GetPlayerStatsView(self.__fighting.Player))
        leftBox.add_widget(self.__playerStats)

        self.__playerWeaponStats = BoxLayout()
        self.__playerWeaponStats.add_widget(self.__GetWeaponStatsView(self.__fighting.Player.Weapon))
        leftBox.add_widget(self.__playerWeaponStats)

        self.__selectedItemView = BoxLayout()
        self.__selectedItemView.add_widget(self.__GetSelectedItemView(self.__selectedItem))
        leftBox.add_widget(self.__selectedItemView)

        middleBox.add_widget(Button(text="Menu", on_press=self.OnPressMain, size_hint_y=0.05,
                                    color=globalVar.buttonTextColor,
                                    background_color=globalVar.buttonColor, ))
        middleBox.add_widget(self.__GetFightingMenu())
        middleBox.add_widget(self.__GetInventoryView(self.__fighting.Player.Inventory))

        self.__enemyStats = BoxLayout()
        self.__enemyStats.add_widget(self.__GetPlayerStatsView(self.__fighting.Enemy))
        rightBox.add_widget(self.__enemyStats)

        self.__enemyWeaponStats = BoxLayout()
        self.__enemyWeaponStats.add_widget(self.__GetWeaponStatsView(self.__fighting.Enemy.Weapon))
        rightBox.add_widget(self.__enemyWeaponStats)

        mainBox.add_widget(leftBox)
        mainBox.add_widget(middleBox)
        mainBox.add_widget(rightBox)
        self.add_widget(mainBox)

    def __GetFightingMenu(self) -> BoxLayout:
        box = BoxLayout(size_hint=(1, 0.4), orientation="vertical", spacing=2)
        box.add_widget(Button(text="Skip a turn",
                              on_press=self.onPressSkipTurn,
                              color=globalVar.buttonTextColor,
                              size_hint=(1, 0.25),
                              background_color=globalVar.buttonColor))
        box.add_widget(Button(text="Attack player",
                              on_press=self.onPressAttackPlayer,
                              color=globalVar.buttonTextColor,
                              size_hint=(1, 0.25),
                              background_color=globalVar.buttonColor))
        box.add_widget(Button(text="Attack enemy",
                              on_press=self.onPressAttackEnemy,
                              color=globalVar.buttonTextColor,
                              size_hint=(1, 0.25),
                              background_color=globalVar.buttonColor))
        box.add_widget(Button(text="Make effect at enemy",
                              on_press=self.onPressEffectEnemy,
                              color=globalVar.buttonTextColor,
                              size_hint=(1, 0.25),
                              background_color=globalVar.buttonColor))
        box.add_widget(Button(text="Make effect at player",
                              on_press=self.onPressEffectPlayer,
                              color=globalVar.buttonTextColor,
                              size_hint=(1, 0.25),
                              background_color=globalVar.buttonColor))
        box.add_widget(Button(text="Make effect at player weapon",
                              on_press=self.onPressEffectPlayerWeapon,
                              color=globalVar.buttonTextColor,
                              size_hint=(1, 0.25),
                              background_color=globalVar.buttonColor))
        box.add_widget(Button(text="Make effect at enemy weapon",
                              on_press=self.onPressEffectEnemyWeapon,
                              color=globalVar.buttonTextColor,
                              size_hint=(1, 0.25),
                              background_color=globalVar.buttonColor))
        return box

    def __SetSelectedItem(self, item: Item):
        self.__selectedItem = item
        self.__selectedItemView.clear_widgets()
        self.__selectedItemView.add_widget(self.__GetSelectedItemView(self.__selectedItem))

    def __GetSelectedItemView(self, item: Item) -> GridLayout:
        return Drawer().GetView(item)

    def __GetPlayerStatsView(self, player: Player) -> BoxLayout:
        return Drawer().GetView(player)

    def __GetWeaponStatsView(self, weapon: Weapon) -> BoxLayout:
        return Drawer().GetView(weapon)

    def __GetItemView(self, item: Item) -> BoxLayout:
        box = BoxLayout(orientation="horizontal")
        box.add_widget(Button(text=item.GetName(),
                              size_hint=(1, 0.5),
                              on_press=lambda a: self.__SetSelectedItem(item),
                              background_color=globalVar.buttonColor,
                              color=globalVar.buttonTextColor))
        return box

    def __GetInventoryView(self, inventory: Inventory) -> BoxLayout:
        box = BoxLayout(orientation="vertical", size_hint=(1, 0.4))
        box.add_widget(PROLabel(text="Inventory",
                                size_hint=(1, 0.2),
                                color=globalVar.textColor,
                                backgroundColor=globalVar.labelBackgroundColor))
        inventoryBox = BoxLayout(orientation="vertical", spacing=3, size_hint=(1, 0.8))
        for i in inventory.GetItems():
            inventoryBox.add_widget(self.__GetItemView(i))

        scroll = ScrollView(size_hint=(1, 1), size=Window.size)
        scroll.add_widget(inventoryBox)
        box.add_widget(scroll)
        return box

    def onPressSkipTurn(self, *args):
        pass

    def __UpdatePlayerStats(self):
        self.__playerStats.clear_widgets()
        self.__playerStats.add_widget(self.__GetPlayerStatsView(self.__fighting.Player))

    def __UpdateEnemyStats(self):
        self.__enemyStats.clear_widgets()
        self.__enemyStats.add_widget(self.__GetPlayerStatsView(self.__fighting.Enemy))

    def __UpdatePlayerWeaponStats(self):
        self.__playerWeaponStats.clear_widgets()
        self.__playerWeaponStats.add_widget(self.__GetWeaponStatsView(self.__fighting.Player.Weapon))

    def __UpdateEnemyWeaponStats(self):
        self.__enemyWeaponStats.clear_widgets()
        self.__enemyWeaponStats.add_widget(self.__GetWeaponStatsView(self.__fighting.Enemy.Weapon))

    def onPressAttackPlayer(self, *args):
        self.__fighting.MakeDamage(self.__fighting.Player,
                                   self.__fighting.Player.Weapon)
        self.__UpdatePlayerStats()

    def onPressAttackEnemy(self, *args):
        self.__fighting.MakeDamage(self.__fighting.Enemy,
                                   self.__fighting.Player.Weapon)
        self.__UpdateEnemyStats()

    def onPressEffectPlayer(self, *args):
        if not isinstance(self.__selectedItem, Potion):
            return
        self.__fighting.MakeEffectAt(self.__fighting.Player,
                                     self.__selectedItem)
        self.__UpdatePlayerStats()

    def onPressEffectEnemy(self, *args):
        if not isinstance(self.__selectedItem, Potion):
            return
        self.__fighting.MakeEffectAt(self.__fighting.Enemy,
                                     self.__selectedItem)
        self.__UpdateEnemyStats()

    def onPressEffectPlayerWeapon(self, *args):
        if not isinstance(self.__selectedItem, WeaponImprovementItem):
            return
        self.__fighting.MakeEffectAt(self.__fighting.Player.Weapon,
                                     self.__selectedItem)
        self.__UpdatePlayerWeaponStats()

    def onPressEffectEnemyWeapon(self, *args):
        if not isinstance(self.__selectedItem, WeaponImprovementItem):
            return
        self.__fighting.MakeEffectAt(self.__fighting.Enemy.Weapon,
                                     self.__selectedItem)
        self.__UpdateEnemyWeaponStats()

    def OnPressMain(self, *args):
        globalVar.screenManager.remove_widget(self)
        globalVar.screenManager.current = "main"
