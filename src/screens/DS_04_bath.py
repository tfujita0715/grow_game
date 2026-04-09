import pyxel
from .base import BaseScreen

class Bath(BaseScreen):
    def __init__(self):
        pass
    
    def update(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            #17,192,,,118,224
            #140,193,,,240,225
            #セキュリティ風呂ボタン
            if (17 < pyxel.mouse_x < 118) and (192 < pyxel.mouse_y < 224):
                pass
            #色風呂ボタン
            elif (140 < pyxel.mouse_x < 240) and (193 < pyxel.mouse_y < 225):
                pass

    def draw(self):
        pyxel.load("bath.pyxres")
        pyxel.blt(0, 0, 0, 0, 0, 255, 255, 0)
        pyxel.text(17, 192, "セキュリティ風呂", 0)
        pyxel.text(140, 193, "色風呂", 0)

        