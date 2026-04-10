import pyxel

#画面インポート
from .DS_01_title import title
from .DS_11_setting import SettingScreen
from .DS_02_room import RoomScreen
from .DS_16_hospital import HospitalScreen
from .DS_08_meal import meal
from .DS_04_bath import Bath
from .DS_12_shop import ShopScreen
from .DS_03_toilet import ToiletScreen
from .DS_09_gameover import Gameover


#ここで画面遷移を行います。
# インポート例from .settingScreen import SettingScreen 

class ScreenManager:
    def __init__(self, game_data, chara_data): # 引数を追加
        self.chara_data = chara_data
        self.game_data = game_data #データを持つ
        self.current_screen = title(self.game_data, self.chara_data) #データ引き渡し
        self.before_screen = None #呼び出し元
        #画面とクラスの対応表
        self.screen_map = {
            "title": title,
            "setting": SettingScreen,
            "room": RoomScreen,
            "hospital": HospitalScreen,
            "meal": meal,
            "bath": Bath,
            "shop": ShopScreen,
            "toilet": ToiletScreen,
            "gameover": Gameover
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
            self.current_screen = self.screen_map[key](self.game_data,self.chara_data)
            #遷移フラグをクリアしておく
            self.current_screen.next_screen = None


    def draw(self):
        self.current_screen.draw()