import pyxel
#画面の基底クラス共通の機能、初期化

class BaseScreen:
    def __init__(self):
        self.next_screen = None #Noneの場合は遷移なし
    def update(self):
        pass
    def draw(self):
        pass

    def get_next_screen(self):
        return self.next_screen

class Setting(BaseScreen):
    def __init__(self):
        super().__init__()
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
    def __init__(self):
        super().__init__()
        self.next_screen = None

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            self.next_screen = "back" #元の画面に戻るときはback

    def draw(self):
        pyxel.cls(2)
        pyxel.text(80, 120, "SETTING SCREEN (PRESS ESCAPE TO BACK)", 7)
