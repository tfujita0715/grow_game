import pyxel
#画面の基底クラス共通の機能、初期化

class BaseScreen:
    def __init__(self,game_data, chara_data):
        self.game_data = game_data, chara_data
        self.next_screen = None #Noneの場合は遷移なし
    def update(self):
        pass
    def draw(self):
        pass

    def get_next_screen(self):
        return self.next_screen

