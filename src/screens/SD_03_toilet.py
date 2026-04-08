import pyxel
import random
from .base import BaseScreen

class ToiletScreen(BaseScreen):
    def __init__(self):
        super().__init__()

        # キャッシュ状態（ここで管理）
        self.cache = 0
        self.max_cache = 100
        self.used_today = False

        self.result = ""

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            self.next_screen = "back"

        # クリック
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if 80 < pyxel.mouse_x < 180 and 100 < pyxel.mouse_y < 140:
                self.use_toilet()

    def use_toilet(self):
        if self.used_today:
            self.result = "今日はもう無理"
            return

        self.used_today = True

        r = random.random()

        if r < 0.2:
            self.cache = 0
            self.result = "トイレ失敗"
        elif r > 0.8:
            self.cache = 0
            self.result = "トイレ大成功"
        else:
            amount = random.choice([30, 50, 70])
            self.cache = max(0, self.cache - amount)
            self.result = "トイレ成功"

    def draw(self):
        pyxel.cls(0)

        pyxel.text(90, 20, "TOILET", 7)

        pyxel.text(80, 50, f"CACHE: {self.cache}%", 7)
        pyxel.rect(80, 60, self.cache * 1.5, 10, 11)

        # ボタン
        pyxel.rect(80, 100, 100, 40, 8)
        pyxel.rectb(80, 100, 100, 40, 7)
        pyxel.text(100, 115, "CLEAR", 7)

        pyxel.text(80, 160, self.result, 7)