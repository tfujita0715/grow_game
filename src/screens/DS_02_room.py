import pyxel
from .base import BaseScreen

class RoomScreen(BaseScreen):
    def __init__(self, game_data):
        super().__init__(game_data)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            self.next_turn()

    def nextturn(self):
        #次の日
        self.game_data.day += 1

    def draw(self):
        pyxel.cls(0)
        pyxel.text(10, 10, f"DAY: {self.game_data.day}", 7)
        pyxel.text(10, 30, f"HP: {self.game_data.hp}", 8)

