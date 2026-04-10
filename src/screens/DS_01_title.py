import pyxel
import os
from .base import Popup

class title(Popup):
    def __init__(self, game_data, chara_data):
        super().__init__(game_data, chara_data)
        self.is_started = False
        self.chara_data = chara_data

        #pyxel.load("c:/pyxel/grow2/grow_game/src/screens/../../assets/room.pyxres")

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.next_screen = "room"

    def draw(self):

        #pyxel.bltm(0, 0, 0, 0, 0, 256, 256)
        pyxel.text(80, 120, "Turing Pet", 20)
        pyxel.text(190, 120, "plz push space",5)
