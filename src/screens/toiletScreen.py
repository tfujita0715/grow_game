import pyxel

from .base import BaseScreen

class ToiletScreen(BaseScreen):
    def __init__(self, toilet_system):
        super().__init__()
        self.toilet_system = toilet_system
        self.result = ""

    def update(self):
        # クリックでキャッシュ削除
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            if 80 < pyxel.mouse_x < 180 and 100 < pyxel.mouse_y < 140:
                self.result = self.toilet_system.clear_cache()

        # ESCで戻る
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            self.next_screen = "back"

    def draw(self):
        pyxel.cls(0)

        pyxel.text(90, 20, "TOILET", 7)

        # キャッシュ表示
        pyxel.text(80, 50, f"CACHE: {self.toilet_system.cache}%", 7)
        pyxel.rect(80, 60, self.toilet_system.cache * 1.5, 10, 11)

        # ボタン
        pyxel.rect(80, 100, 100, 40, 8)
        pyxel.text(100, 115, "CLEAR", 7)

        # 結果表示
        pyxel.text(80, 160, f"RESULT: {self.result}", 7)