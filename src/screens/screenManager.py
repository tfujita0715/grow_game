import pyxel

#画面インポート
from .sampleScreen01 import Screen01


#現在mainから01を直接呼んでいます。将来的にここから画面遷移を行いま。

# from .settingScreen import SettingScreen 

class ScreenManager:
    @staticmethod
    def get_screen(screen_name):
        if screen_name == "01":
            return Screen01()
        # if screen_name == "setting":
        #     return SettingScreen()
        return None