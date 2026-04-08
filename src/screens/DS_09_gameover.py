import pyxel
from .base import BaseScreen
pyxel.load("gameover.pyxres")

class Gameover:
    def __init__(self):
        pass
        
    def update(self):
        #タイトル画面に戻る処理
        #if 40 < pyxel.mouse_x < 216 and 220 < pyxel.mouse_y < 256:
        pass


    def draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, 255, 255)
        pyxel.text(70, 30, "GAME OVER" ,7)
        pyxel.text(40, 220, "タイトルに戻る", 7)
