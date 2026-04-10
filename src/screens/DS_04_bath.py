import pyxel
from .base import BaseScreen
from .imageObj import ImageObj

class Bath(BaseScreen):
    def __init__(self, game_data, chara_data):
        super().__init__(game_data, chara_data)
        self.chara_data = chara_data
        self.game_data = game_data
        self.font = pyxel.Font("misaki_gothic.bdf")
        #画像表示
        self.image = ImageObj("item_+G.png", 0, 0, 0)
        pyxel.load("assets/bath.pyxres")

    def update(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            #セキュリティ風呂ボタン
            if (17 < pyxel.mouse_x < 118) and (192 < pyxel.mouse_y < 224):
                #データ更新
                self.chara_data.security = 100
                self.chara_data.turn -= 1
            #色風呂ボタン
            elif (140 < pyxel.mouse_x < 240) and (193 < pyxel.mouse_y < 225):
                pass
            #戻るボタン
            elif 9 < pyxel.mouse_x < 41 and 9< pyxel.mouse_y < 21:
                self.next_screen = "room"

    def draw(self):
        pyxel.blt(0, 0, 0, 0, 0, 255, 255, 0)
        pyxel.rect(10, 10, 30, 10, 7)
        self.image.draw()
        #pyxel.text(17, 192, "セキュリティ風呂", 0, self.font)
        #pyxel.text(140, 193, "色風呂", 0, self.font)
        pyxel.text(12, 12, "もどる", 6, self.font)

        