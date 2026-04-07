import pyxel
from .DS_11_setting import Setting

class title(Setting):
    def __init__(self,game_data):
        super().__init__(game_data)
        self.is_started = False

    def update(self):
        self.update_common()
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.next_screen = "room"

    def draw(self):
        pyxel.text(80, 120, "title", 20)
        pyxel.text(190, 120, "plz push space",5)
        self.draw_common()
