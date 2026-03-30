import pyxel
from .base import BaseScreen
pyxel.load("meal.pysres")

class meal:
    def __init__(self):
        pass
        

    def update(self):
        #ごはんの入力受け取り、数字は仮
        #if 100 < pyxel.mouse_x < 120 and 210 < pyxel.mouse_y < 230:
        pass    
    
    def draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, 255, 255)
        pyxel.text(16, 8, "ご飯を選んでください", 10)
        pyxel.text()

