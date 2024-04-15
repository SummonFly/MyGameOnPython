from kivy.uix.screenmanager import ScreenManager
from kivy.uix.settings import Settings, ConfigParser

global gameApp
gameApp = None
global screenManager
screenManager = ScreenManager()
global setting
setting = Settings()
global config
config = ConfigParser()
config.read("View/SettingConfig.ini")


global mainBackgroundColor
mainBackgroundColor = config.get(section='graphics', option='mainbackgroundcolor')
global buttonColor
buttonColor = config.get(section='graphics', option='buttoncolor')
global buttonTextColor
buttonTextColor = config.get(section='graphics', option='buttontextcolor')
global labelBackgroundColor
labelBackgroundColor = config.get(section='graphics', option='labelbackgroundcolor')
global textColor
textColor = config.get(section='graphics', option='textcolor')
global mainBackgroundSource
mainBackgroundSource = "resources/background.png"
