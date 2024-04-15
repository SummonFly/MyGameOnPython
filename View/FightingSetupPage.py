from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

import globalVariable as globalVar
from Model.Fighting import Fighting, FightingSetup
from Model.Damageable import Player
from Model.GameManager import GameManager

from View.PROWidget import PROLabel
from View.FightingPage import FightingPage


class FightingSetupPage(Screen):
    def __init__(self, fightingSetup: FightingSetup, **kwargs):
        super(FightingSetupPage, self).__init__(**kwargs)
        self.__fighting = None
        self.setup = fightingSetup

        box = BoxLayout(orientation="vertical", spacing=6)
        box.add_widget(Button(text="Menu", on_press=self.OnPressMain,
                              background_color=globalVar.buttonColor,
                              color=globalVar.buttonTextColor,
                              size_hint_y=0.05))

        grid = GridLayout(cols=2, spacing=6)
        grid.add_widget(PROLabel(text="Max Health",
                                 backgroundColor=globalVar.labelBackgroundColor,
                                 color=globalVar.textColor))

        self.MaxHealthEntry = TextInput(input_filter='int', multiline=False)
        grid.add_widget(self.MaxHealthEntry)

        grid.add_widget(PROLabel(text="Min Health",
                                 backgroundColor=globalVar.labelBackgroundColor,
                                 color=globalVar.textColor))

        self.MinHealthEntry = TextInput(input_filter='int', multiline=False)
        grid.add_widget(self.MinHealthEntry)

        grid.add_widget(PROLabel(text="Max Armor",
                                 backgroundColor=globalVar.labelBackgroundColor,
                                 color=globalVar.textColor))

        self.MaxArmorEntry = TextInput(input_filter='int', multiline=False)
        grid.add_widget(self.MaxArmorEntry)

        grid.add_widget(PROLabel(text="Min Armor",
                                 backgroundColor=globalVar.labelBackgroundColor,
                                 color=globalVar.textColor))

        self.MinArmorEntry = TextInput(input_filter='int', multiline=False)
        grid.add_widget(self.MinArmorEntry)

        grid.add_widget(PROLabel(text="Max Damage",
                                 backgroundColor=globalVar.labelBackgroundColor,
                                 color=globalVar.textColor))

        self.MaxDamageEntry = TextInput(input_filter='float', multiline=False)
        grid.add_widget(self.MaxDamageEntry)

        grid.add_widget(PROLabel(text="Min Damage",
                                 backgroundColor=globalVar.labelBackgroundColor,
                                 color=globalVar.textColor))

        self.MinDamageEntry = TextInput(input_filter='float', multiline=False)
        grid.add_widget(self.MinDamageEntry)

        box.add_widget(grid)
        box.add_widget(Button(text="Fight", background_color=globalVar.buttonColor, color=globalVar.buttonTextColor,
                              on_press=self.OnPressFighting, size_hint_y=0.05, background_normal=''))

        self.add_widget(box)

    def __BuildFighting(self):
        self.setup.MaxArmor = int(self.MaxArmorEntry.text)
        self.setup.MinArmor = int(self.MinArmorEntry.text)
        self.setup.MaxDamage = int(self.MaxDamageEntry.text)
        self.setup.MinDamage = int(self.MinDamageEntry.text)
        self.setup.MaxHealth = int(self.MaxHealthEntry.text)
        self.setup.MinHealth = int(self.MinHealthEntry.text)
        self.__fighting = self.setup.GetFighting()

    def OnPressMain(self, *args):
        globalVar.screenManager.current = "main"

    def OnPressFighting(self, *args):
        self.__BuildFighting()
        fightingPage = FightingPage(self.__fighting, name="fighting")
        globalVar.screenManager.add_widget(fightingPage)
        globalVar.screenManager.current = "fighting"
