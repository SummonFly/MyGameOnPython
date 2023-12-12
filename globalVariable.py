from kivy.uix.screenmanager import ScreenManager


def init():
    global screenManager
    screenManager = ScreenManager()
    global buttonRed
    buttonRed = [100, 1, 1]
    global buttonBlack
    buttonBlack = [0, 0, 0]
    global mainBackground
    mainBackground = "resources/background.png"
