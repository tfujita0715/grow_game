# screen/screen01.py
import pyxel

from .base import Setting

class Screen01(Setting):
    def __init__(self):
        super().__init__()
        self.is_started = False

    def update(self):
        if self.is_started == True:
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.is_started = True
        else:
            self.update_common()

    def draw(self):
        if self.is_started == True:
            pyxel.text(80, 120, "PRESS SPACE TO START", 7)
            pyxel.text(190, 120, "plz push space",5)
        pyxel.text(100, 120, self.message, 20)
        self.draw_common()