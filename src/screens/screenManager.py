import pyxel

#画面インポート
from .DS01_title import title
from .base import SettingScreen
#ここで画面遷移を行います。
# インポート例from .settingScreen import SettingScreen 

class ScreenManager:
    def __init__(self,game_data):
        self.game_data = game_data #データを持つ
        self.current_screen = title(self.game_data) #データ引き渡し
        self.before_screen = None #呼び出し元
        #画面とクラスの対応表
        self.screen_map = {
            "title": title,
            "setting": SettingScreen
        }
    def update(self):
        self.current_screen.update()
        key = self.current_screen.get_next_screen()

        #元の画面に戻る処理
        if key == "back":
            if self.before_screen:
                self.current_screen = self.before_screen
                if hasattr(self.current_screen,"number"):
                    self.current_screen.number = False
                #baseのnext.screen
                self.current_screen.next_screen = None
                self.before_screen = None

        elif key in self.screen_map:

            if key == "setting":
                self.before_screen = self.current_screen

            #新しい画面にデータ引き渡し
            self.before_screen = self.current_screen
            #新しい画面に切り替え
            self.current_screen = self.screen_map[key](self.game_data)
            #遷移フラグをクリアしておく
            self.current_screen.next_screen = None


    def draw(self):
        self.current_screen.draw()