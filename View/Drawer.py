from functools import singledispatchmethod
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

import globalVariable
from Model.Inventory import Item
from Model.Weapon import Weapon, WeaponImprovement, WeaponItem
from Model.Damageable import IDamageable, Player, DamageableImprovement
from Model.Potion import Potion
from View.PROLabel import PROLabel


class Drawer:
    def __CreateViewForValues(self,  **kwargs) -> GridLayout:
        view = GridLayout(cols=2, spacing=5)
        for i in kwargs.keys():
            view.add_widget(PROLabel(text=f"{i}:", backgroundColor=globalVariable.labelBackgroundColor, color=globalVariable.textColor))
            try:
                view.add_widget(PROLabel(text=f"{kwargs[i]}", backgroundColor=globalVariable.labelBackgroundColor, color=globalVariable.textColor))
            except Exception:
                print("Key have not Name")
        return view

    @singledispatchmethod
    def GetView(self, e) -> GridLayout:
        view = GridLayout(cols=1)
        view.add_widget(PROLabel(text=f"Choice Item"), backgroundColor=globalVariable.labelBackgroundColor)
        return view

    @GetView.register(Item)
    def _(self, e) -> GridLayout:
        return self.__CreateViewForValues(Name=e.GetName(), Count=e.GetCount(), Max=e.GetMaxCount())

    @GetView.register(Weapon)
    def _(self, e) -> GridLayout:
        return self.__CreateViewForValues(Damage=e.Damage, CritDamageMultiplier=e.CritDamageMultiplier,
                                          CritChance=e.CritChance, Speed=e.Speed)

    @GetView.register(WeaponImprovement)
    def _(self, e) -> GridLayout:
        return self.__CreateViewForValues(Damage=e.Damage, CritDamageMultiplier=e.CritDamageMultiplier,
                                          CritChance=e.CritChance, Speed=e.Speed)

    @GetView.register(WeaponItem)
    def _(self, e) -> GridLayout:
        return self.__CreateViewForValues(Name=e.GetName(), Count=e.GetCount(),
                                          Max=e.GetMaxCount(), Damage=e.Damage,
                                          CritDamageMultiplier=e.CritDamageMultiplier,
                                          CritChance=e.CritChance, Speed=e.Speed)

    @GetView.register(IDamageable)
    def _(self, e) -> GridLayout:
        return self.__CreateViewForValues(Health=e.Health, Armor=e.Armor)

    @GetView.register(DamageableImprovement)
    def _(self, e) -> GridLayout:
        return self.__CreateViewForValues(Health=e.Health, Armor=e.Armor)

    @GetView.register(Potion)
    def _(self, e) -> GridLayout:
        return self.__CreateViewForValues(Name=e.GetName(), Count=e.GetCount(), Health=e.Health, Armor=e.Armor)
