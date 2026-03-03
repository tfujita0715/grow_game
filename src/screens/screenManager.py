import pyxel

#画面インポート
from .DS01_title import title
from .base import SettingScreen
#ここで画面遷移を行います。
# インポート例from .settingScreen import SettingScreen 

class ScreenManager:
    def __init__(self):
        self.current_screen = title()
        #画面とクラスの対応表
        self.screen_map = {
            "title": title,
            "setting": SettingScreen
        }
    def update(self):
        self.current_screen.update()
        next_screen = self.current_screen.get_next_screen()
        if next_screen == "setting":
            self.current_screen = setting()
        elif next_screen == "title":
            self.current_screen = title()

    def draw(self):
        self.current_screen.draw()