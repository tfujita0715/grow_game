import pyxel
#画面の基底クラス共通の機能、初期化

class BaseScreen:
    def __init__(self,game_data):
        self.next_screen = None #Noneの場合は遷移なし
    def update(self):
        pass
    def draw(self):
        pass

    def get_next_screen(self):
        return self.next_screen

class Setting(BaseScreen):
    def __init__(self,game_data):
        super().__init__(game_data)
        self.number = False

    def update_common(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
           if 0 <= pyxel.mouse_x <= 64 and 0 <= pyxel.mouse_y <= 64:
              # ボタンが押されたら遷移先を指定する
            self.next_screen = "setting"
    def draw_common(self):
        pyxel.cls(1) 
        pyxel.rect(0, 0, 64, 64, 8) # x, y, w, h, col
        pyxel.text(5, 25, "SETTING", 7)
    
class SettingScreen(BaseScreen):
    def __init__(self,game_data):
        super().__init__(game_data)
        self.next_screen = None

    def update(self):
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.game_data.volume = max(0, self.game_data.volume - 1)
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.game_data.volume = min(10, self.game_data.volume + 1)
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            self.next_screen = "back" #元の画面に戻るときはback
        

    def draw(self):
        pyxel.cls(2)
        pyxel.text(80, 120, "SETTING SCREEN (PRESS ESCAPE TO BACK)", 7)

        #音量バー
        pyxel.text(80, 120, "VOLUME:", 7)
        #（枠）
        pyxel.rectb(115, 119, 52, 7, 7)
        #音量バーロジック
        pyxel.rect(116, 120, self.game_data.volume * 5, 5, 10)
