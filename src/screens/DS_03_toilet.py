import pyxel
import random
from .base import BaseScreen

class ToiletScreen(BaseScreen):
    def __init__(self, game_data, chara_data):
        super().__init__(game_data, chara_data)

        self.game_data = game_data
        self.chara_data = chara_data

        self.used_today = False
        self.result = ""
        self.chara_data.size = self.chara_data.size + 3.2

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            self.next_screen = "back"

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            mx = pyxel.mouse_x
            my = pyxel.mouse_y

            # トイレボタン
            if 80 < mx < 180 and 100 < my < 140:
                self.use_toilet()
                return

            # BACK TO ROOM
            if 80 < mx < 160 and 180 < my < 195:
                self.next_screen = "room"
                return

    def use_toilet(self):
        if self.used_today:
            self.result = "今日はもう無理"
            return

        # ターン消費
        if self.chara_data.turn <= 0:
            self.result = "ターンが足りない"
            return

        self.chara_data.turn -= 1
        self.used_today = True

        current = self.game_data.unko

        if current <= 0:
            self.result = "何も出ない"
            return

        r = random.random()

        # 失敗（20%）
        if r < 0.2:
            rate = random.uniform(1.1, 1.5)  # 110%〜150%
            removed = int(current * rate)
            self.game_data.unko = max(0, current - removed)
            self.result = f"トイレ失敗！({int(rate*100)}%除去)"

        # 大成功（20%）
        elif r > 0.8:
            removed = current
            self.game_data.unko = 0
            self.result = "トイレ大成功！(100%除去)"

        # 成功（60%）
        else:
            rate = random.choice([0.3, 0.5, 0.7])
            removed = int(current * rate)
            self.game_data.unko = current - removed
            self.result = f"トイレ成功！({int(rate*100)}%除去)"

    def draw(self):
        pyxel.cls(0)

        pyxel.text(90, 20, "TOILET", 7)

        pyxel.text(80, 50, f"UNKO: {self.game_data.unko}", 7)
        pyxel.rect(80, 60, self.game_data.unko * 1.5, 10, 11)

        pyxel.rect(80, 100, 100, 40, 8)
        pyxel.rectb(80, 100, 100, 40, 7)
        pyxel.text(100, 115, "CLEAR", 7)

        pyxel.text(80, 160, self.result, 7)

        pyxel.rect(80, 180, 80, 15, 5) 
        pyxel.text(88, 185, "BACK TO ROOM", 7)