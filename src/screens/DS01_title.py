import pyxel
from .base import BaseScreen
from .base import Setting

class title(Setting):
    def __init__(self):
        super().__init__()
        self.is_started = False

    def update(self):
        self.update_common()
        if self.number:
            self.next_screen = "setting"

    def draw(self):
        pyxel.text(80, 120, "title", 20)
        pyxel.text(190, 120, "plz push space",5)
        self.draw_common()