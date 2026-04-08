import pyxel
from .base import BaseScreen,Popup

class RoomScreen(Popup):
    def __init__(self, game_data,chara_data):
        super().__init__(game_data,chara_data)
        self.chara_data = chara_data
        self.popup = Popup(game_data, chara_data)


    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            self.next_turn()

    def nextturn(self):
        #次の日
        self.game_data.day += 1

    def draw(self):
        pyxel.cls(0)
        pyxel.text(80, 120, "room", 20)
        pyxel.text(10, 10, f"DAY: {self.chara_data.day}", 7)
        pyxel.text(10, 30, f"HP: {self.chara_data.HP}", 8)

        self.popup.draw()

