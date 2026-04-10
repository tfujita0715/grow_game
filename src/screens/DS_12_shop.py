import pyxel
from .base import BaseScreen

class ShopScreen(BaseScreen):
    def __init__(self, game_data, chara_data):
        super().__init__(game_data, chara_data)

        self.game_data = game_data
        self.chara_data = chara_data

        self.msg = ""
        self.select_item = None
        self.mode = None

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            self.next_screen = "back"

        if self.mode:
            self.update_modal()
            return

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            mx = pyxel.mouse_x
            my = pyxel.mouse_y

            items = list(self.game_data.items.items())

            for i, (name, item) in enumerate(items):
                x = 40
                y = 50 + i * 30

                if x < mx < x + 200 and y < my < y + 25:
                    self.select_item = (name, item)
                    self.mode = "confirm"

    def update_modal(self):
        if not pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            return

        mx = pyxel.mouse_x
        my = pyxel.mouse_y

        if 80 < mx < 140 and 140 < my < 170:
            if self.mode == "confirm":
                name, item = self.select_item

                if self.game_data.money >= item["price"]:
                    self.buy(item)
                    self.msg = "購入しました"
                else:
                    self.msg = "お金が足りません"

                self.mode = "result"

            elif self.mode == "after":
                self.mode = None

        elif 160 < mx < 220 and 140 < my < 170:
            if self.mode == "confirm":
                self.mode = None
            elif self.mode == "after":
                self.next_screen = "back"

        elif self.mode == "result":
            self.mode = "after"

    def buy(self, item):
        self.game_data.money -= item["price"]

        self.chara_data.tail += item["tail"]
        self.chara_data.size += item["size"]
        self.chara_data.IQ += item["iq"]
        self.chara_data.HP += item["hp"]

    def draw(self):
        pyxel.cls(0)

        pyxel.text(90, 10, "SHOP", 7)
        pyxel.text(10, 20, f"MONEY: {self.game_data.money}", 10)

        pyxel.text(10, 30, f"TAIL:{self.chara_data.tail:.1f}", 7)
        pyxel.text(10, 40, f"SIZE:{self.chara_data.size:.1f}", 7)
        pyxel.text(10, 50, f"IQ:{self.chara_data.IQ:.1f}", 7)
        pyxel.text(10, 60, f"HP:{self.chara_data.HP}", 7)

        items = list(self.game_data.items.items())

        for i, (name, item) in enumerate(items):
            x = 40
            y = 50 + i * 30

            pyxel.rect(x, y, 200, 25, 8)
            pyxel.rectb(x, y, 200, 25, 7)
            pyxel.text(x + 5, y + 5, f"{name} {item['price']}G", 7)

        if self.mode:
            self.draw_modal()
        else:
            pyxel.text(40, 190, self.msg, 7)

    def draw_modal(self):
        pyxel.rect(30, 30, 200, 140, 1)
        pyxel.rectb(30, 30, 200, 140, 7)

        name, item = self.select_item

        if self.mode == "confirm":
            pyxel.text(50, 50, name, 7)
            pyxel.text(50, 70, f"価格:{item['price']}", 7)
            pyxel.text(50, 90, f"所持金:{self.game_data.money}", 7)

            if self.game_data.money >= item["price"]:
                pyxel.text(50, 110, "購入しますか？", 7)
            else:
                pyxel.text(50, 110, "お金が足りません", 8)

            pyxel.rect(80, 140, 60, 30, 8)
            pyxel.rectb(80, 140, 60, 30, 7)
            pyxel.text(95, 150, "YES", 7)

            pyxel.rect(160, 140, 60, 30, 8)
            pyxel.rectb(160, 140, 60, 30, 7)
            pyxel.text(175, 150, "NO", 7)

        elif self.mode == "result":
            pyxel.text(50, 90, self.msg, 7)
            pyxel.text(50, 120, "クリックで次へ", 7)

        elif self.mode == "after":
            pyxel.text(50, 80, "続けますか？", 7)

            pyxel.rect(80, 140, 60, 30, 8)
            pyxel.rectb(80, 140, 60, 30, 7)
            pyxel.text(85, 150, "続ける", 7)

            pyxel.rect(160, 140, 60, 30, 8)
            pyxel.rectb(160, 140, 60, 30, 7)
            pyxel.text(165, 150, "戻る", 7)