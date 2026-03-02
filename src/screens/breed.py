import pyxel

class Breed:#[ ]繁殖にするか結婚にするか
    def update(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            #繁殖ボタン
            if 95 < pyxel.mouse_x < 167 and 123 < pyxel.mouse_y < 150:
                #TODO子供の姿を描画してから部屋に戻る
                pass
            #戻るボタン
            elif 91 < pyxel.mouse_x < 172 and 230 < pyxel.mouse_y < 251:
                #TODOお見合いに戻る
                pass

    def draw(self):
        pyxel.load("breed.pyxres")
        pyxel.blt(0, 0, 0, 0, 0, 255, 255, 0)
        pyxel.text(95, 123, "繁殖", 0)
        pyxel.text(91, 230, "選びなおす", 0)