from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
import globalVariable as globalVar
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

from Model.Store import Store, Good
from View.GoodView import GoodStatsView


class StorePage(Screen):
    def __init__(self, store: Store, **kwargs):
        super(StorePage, self).__init__(**kwargs)
        self.__store = store
        self.__currentGood = Good.NoneGood()
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
                background_color=globalVar.buttonColor))

        subBox = BoxLayout(
            size_hint=(1, 0.9))

        leftBox = BoxLayout(
            orientation="vertical",
            size_hint=(0.5, 1))
        gridText = GridLayout(
            cols=2,
            size_hint=(1, 0.1))
        gridText.add_widget(
            Label(text="NAME",
                  size_hint=(0.7, 1),
                  color=globalVar.labelColor))
        gridText.add_widget(
            Label(text="COST",
                  size_hint=(0.3, 1)))
        leftBox.add_widget(gridText)

        self.__goodsView = ScrollView(
            size=Window.size,
            size_hint=(1, 0.9))
        self.__BuildGoods(self.__goodsView)
        leftBox.add_widget(self.__goodsView)

        rightBox = BoxLayout(
            size_hint=(0.5, 1),
            orientation="vertical")
        icon = Image(
            source=globalVar.mainBackgroundSource,
            size_hint=(1, 0.35))
        rightBox.add_widget(icon)

        rightBox.add_widget(
            Label(text="STATS",
                  size_hint=(1, 0.07)))

        self.statsScroll = ScrollView(
            size=Window.size,
            size_hint=(1, 0.4))
        if self.__currentGood is not None:
            self.statsScroll.add_widget(GoodStatsView().GetView(self.__currentGood.Item))
        rightBox.add_widget(self.statsScroll)

        # self.__goodCount = Slider(size_hint=(0.8, 1))
        # rightBox.add_widget(self.__goodCount)

        rightBox.add_widget(
            Button(text="BUY",
                   size_hint=(1, 0.08),
                   on_press=self.OnPressBuy,
                   background_color=globalVar.buttonColor))

        subBox.add_widget(leftBox)
        subBox.add_widget(rightBox)
        mainBox.add_widget(subBox)
        self.add_widget(mainBox)

    def __BuildGoods(self, scroll: ScrollView):
        box = BoxLayout(orientation="vertical", size_hint_y=None, height=0)
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
                   background_color=globalVar.buttonColor))
        view.add_widget(
            Label(
                text=str(good.Cost),
                size_hint=(0.3, 1)))
        return view

    def OnPressMain(self, *args):
        globalVar.screenManager.current = "main"

    def OnGoodPress(self, good: Good):
        self.__currentGood = good
        self.__UpdateStatsView(good)

    def OnPressBuy(self, *args):
        if self.__currentGood is None:
            return
        self.__store.BuyItem(self.__currentGood, 10)
        self.__BuildGoods(self.__goodsView)
        self.__UpdateStatsView(self.__currentGood)

    def __UpdateStatsView(self, good: Good):
        self.__currentGoods = good
        self.statsScroll.clear_widgets()
        self.statsScroll.add_widget(GoodStatsView().GetView(good.Item))

