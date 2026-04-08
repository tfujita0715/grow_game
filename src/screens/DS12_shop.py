import pyxel
from .base import BaseScreen

class ShopScreen(BaseScreen):
    def __init__(self):
        super().__init__()

        self.status = {
            "tail": 0,
            "size": 0,
            "iq": 0,
            "hp": 100
        }

        self.money = 100
        self.msg = ""

        self.select_item = None
        self.mode = None

        self.items = [
            {"name": "Byte Bites", "price": 50, "tail": 0.5, "size": 0.5, "iq": 0.5, "hp": 0},
            {"name": "Cookie", "price": 80, "tail": 0.75, "size": 0.75, "iq": 0.75, "hp": 0},
            {"name": "Wi-Fiバームクーヘン", "price": 70, "tail": 1, "size": 0.1, "iq": 0.1, "hp": 0},
            {"name": "SSDサンド", "price": 70, "tail": 0.1, "size": 1, "iq": 0.1, "hp": 0},
            {"name": "Raspberry Pi", "price": 90, "tail": 0.1, "size": 0.1, "iq": 1, "hp": 0},
            {"name": "NullNullNatto", "price": 40, "tail": 0, "size": 0, "iq": 0, "hp": 10},
        ]

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            self.next_screen = "back"

        if self.mode:
            self.update_modal()
            return

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            mx = pyxel.mouse_x
            my = pyxel.mouse_y

            for i in range(len(self.items)):
                x = 40
                y = 50 + i * 30

                if x < mx < x + 200 and y < my < y + 25:
                    self.select_item = self.items[i]
                    self.mode = "confirm"

    def update_modal(self):
        if not pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            return

        mx = pyxel.mouse_x
        my = pyxel.mouse_y

        if 80 < mx < 140 and 140 < my < 170:
            if self.mode == "confirm":
                if self.money >= self.select_item["price"]:
                    self.buy(self.select_item)
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
        self.money -= item["price"]

        self.status["tail"] += item["tail"]
        self.status["size"] += item["size"]
        self.status["iq"] += item["iq"]
        self.status["hp"] += item["hp"]

    def draw(self):
        pyxel.cls(0)

        pyxel.text(90, 10, "SHOP", 7)
        pyxel.text(10, 20, f"MONEY: {self.money}", 10)

        pyxel.text(10, 30, f"TAIL:{self.status['tail']:.1f}", 7)
        pyxel.text(10, 40, f"SIZE:{self.status['size']:.1f}", 7)
        pyxel.text(10, 50, f"IQ:{self.status['iq']:.1f}", 7)
        pyxel.text(10, 60, f"HP:{self.status['hp']}", 7)

        for i in range(len(self.items)):
            item = self.items[i]
            x = 40
            y = 50 + i * 30

            pyxel.rect(x, y, 200, 25, 8)
            pyxel.rectb(x, y, 200, 25, 7)
            pyxel.text(x + 5, y + 5, f"{item['name']} {item['price']}G", 7)

        if self.mode:
            self.draw_modal()
        else:
            pyxel.text(40, 190, self.msg, 7)

    def draw_modal(self):
        pyxel.rect(30, 30, 200, 140, 1)
        pyxel.rectb(30, 30, 200, 140, 7)

        item = self.select_item

        if self.mode == "confirm":
            pyxel.text(50, 50, item["name"], 7)
            pyxel.text(50, 70, f"価格:{item['price']}", 7)
            pyxel.text(50, 90, f"所持金:{self.money}", 7)

            if self.money >= item["price"]:
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