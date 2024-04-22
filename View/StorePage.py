from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
import globalVariable as globalVar
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

from Model.Store import Store, Good
from View.Drawer import Drawer
from View.SliderWithEntry import SliderWithEntry
from View.PROWidget import PROLabel


class StorePage(Screen):
    def __init__(self, store: Store, **kwargs):
        super(StorePage, self).__init__(**kwargs)
        self.__store = store
        self.__currentGood = None
        self.__goodsView = None
        self.__initView()

    def __initView(self):
        mainBox = BoxLayout(
            orientation="vertical")
        mainBox.add_widget(
            Button(
                text="MENU",
                on_press=self.OnPressMain,
                size_hint=(1, 0.1),
                background_color=globalVar.buttonColor,
                color=globalVar.buttonTextColor,
                background_normal=''))

        subBox = BoxLayout(
            size_hint=(1, 0.9),
            padding=(10, 10, 10, 10),
            spacing=6)

        leftBox = BoxLayout(
            orientation="vertical",
            size_hint=(0.5, 1))
        gridText = GridLayout(
            cols=2,
            padding=3,
            size_hint=(1, 0.1))
        gridText.add_widget(
            PROLabel(text="NAME",
                     size_hint=(0.7, 1),
                     color=globalVar.textColor,
                     backgroundColor=globalVar.labelBackgroundColor))
        gridText.add_widget(
            PROLabel(text="COST",
                     size_hint=(0.3, 1),
                     color=globalVar.textColor,
                     backgroundColor=globalVar.labelBackgroundColor)),
        leftBox.add_widget(gridText)

        self.__goodsView = ScrollView(
            size=Window.size,
            size_hint=(1, 0.9))
        self.__BuildGoods(self.__goodsView)
        leftBox.add_widget(self.__goodsView)

        rightBox = BoxLayout(
            size_hint=(0.5, 1),
            spacing=3,
            orientation="vertical")
        self.__coinsView = BoxLayout(size_hint=(1, 0.07))
        self.__coinsView.add_widget(self.__GetCoinsView(self.__store.Config.Coins))
        rightBox.add_widget(self.__coinsView)

        rightBox.add_widget(
            PROLabel(text="STATS",
                     size_hint=(1, 0.07),
                     backgroundColor=globalVar.labelBackgroundColor))

        self.statsScroll = ScrollView(
            size=Window.size,
            size_hint=(1, 0.4))
        if self.__currentGood is not None:
            self.statsScroll.add_widget(Drawer().GetView(self.__currentGood.Item))
        rightBox.add_widget(self.statsScroll)

        self.__goodCount = SliderWithEntry(size_hint=(0.8, 0.1))
        rightBox.add_widget(self.__goodCount)

        rightBox.add_widget(
            Button(text="BUY",
                   size_hint=(1, 0.08),
                   on_press=self.OnPressBuy,
                   background_color=globalVar.buttonColor,
                   color=globalVar.buttonTextColor))

        subBox.add_widget(leftBox)
        subBox.add_widget(rightBox)
        mainBox.add_widget(subBox)
        self.add_widget(mainBox)

    def __BuildGoods(self, scroll: ScrollView):
        box = BoxLayout(orientation="vertical", size_hint_y=None, height=0, spacing=2)
        for good in self.__store.Goods:
            box.add_widget(self.__GetGoodView(good))
            box.height += 40
        scroll.clear_widgets()
        scroll.add_widget(box)

    def __GetGoodView(self, good: Good) -> GridLayout:
        view = GridLayout(
            cols=2,
            size_hint_y=None,
            height=40)
        view.add_widget(
            Button(text=good.Item.GetName(),
                   size_hint=(0.7, 1),
                   on_press=lambda *args: self.OnGoodPress(good),
                   background_color=globalVar.buttonColor,
                   color=globalVar.buttonTextColor))
        view.add_widget(
            PROLabel(
                text=str(good.Cost),
                backgroundColor=globalVar.labelBackgroundColor,
                color=globalVar.textColor,
                size_hint=(0.3, 1)))
        return view

    def __GetCoinsView(self, coins: int) -> BoxLayout:
        box = BoxLayout()
        box.add_widget(PROLabel(text="COINS:",
                                backgroundColor=globalVar.labelBackgroundColor,
                                color=globalVar.textColor))
        box.add_widget(PROLabel(text=str(coins),
                                backgroundColor=globalVar.labelBackgroundColor,
                                color=globalVar.textColor
                                ))
        return box

    def OnPressMain(self, *args):
        globalVar.screenManager.current = "main"

    def OnGoodPress(self, good: Good):
        self.__currentGood = good
        self.__goodCount.slider.max = good.Item.GetCount()
        self.__UpdateStatsView(good)
        self.__UpdateCoinsView()

    def OnPressBuy(self, *args):
        if self.__currentGood is None:
            return
        self.__store.BuyItem(self.__currentGood, self.__goodCount.slider.value)
        self.__BuildGoods(self.__goodsView)
        self.__UpdateStatsView(self.__currentGood)
        self.__UpdateCoinsView()

    def __UpdateStatsView(self, good: Good):
        self.statsScroll.clear_widgets()
        self.statsScroll.add_widget(Drawer().GetView(good.Item))

    def __UpdateCoinsView(self):
        self.__coinsView.clear_widgets()
        self.__coinsView.add_widget(self.__GetCoinsView(self.__store.Config.Coins))
