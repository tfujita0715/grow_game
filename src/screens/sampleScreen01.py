# screen/screen01.py
import pyxel

from .base import Setting

class Screen01(Setting):
    def __init__(self):
        super().__init__()
        self.message = "This is sample"

    def update(self):
        self.update_common()

    def draw(self):
        pyxel.text(160, 120, "debug01",5)
        pyxel.text(100, 120, self.message, 5)
        self.draw_common()