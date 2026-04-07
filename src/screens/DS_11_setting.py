import pyxel
from .base import BaseScreen

class Setting(BaseScreen):
    def __init__(self,game_data):
        super().__init__(game_data)
        self.number = False

    def update_common(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
           if 0 <= pyxel.mouse_x <= 64 and 0 <= pyxel.mouse_y <= 64:
              #ボタンが押されたら遷移先を指定する
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
        pyxel.text(80, 100, f"SETTING - VOLUME: {self.game_data.volume}", 7)

        #音量バーの描画
        pyxel.text(80, 120, "VOLUME:", 7)
        #枠を表示
        pyxel.rectb(115, 119, 52, 7, 7)
        #現在の音量（volume * 5 ピクセル分）を塗りつぶす
        pyxel.rect(116, 120, self.game_data.volume * 5, 5, 10)

        pyxel.text(80, 140, "←→key voluemu change", 6)
        pyxel.text(80, 160, "ESC:back", 6)