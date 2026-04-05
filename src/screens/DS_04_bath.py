import pyxel
from .base import BaseScreen

class Bath(BaseScreen):
    def __init__(self):
        pass
    
    def update(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            pass

    def draw(self):
        pyxel.load("bath.pyxres")
        pyxel.blt(0, 0, 0, 0, 0, 255, 255, 0)
        pyxel.text(95, 123, "", 0)
        pyxel.text(91, 230, "", 0)

        