import pyxel

#画面インポート
from .sampleScreen01 import Screen01
from .DS01_title import title
from .base import Setting
#ここで画面遷移を行います。
# インポート例from .settingScreen import SettingScreen 

class ScreenManager:
    @staticmethod
    def get_screen(screen_name):
        if screen_name == "01":
            return Screen01()
        # if screen_name == "setting":
        #     return SettingScreen()
        return None