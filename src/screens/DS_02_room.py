import pyxel
from .base import BaseScreen, Popup

class RoomScreen(Popup):
    def __init__(self, game_data, chara_data):
        super().__init__(game_data, chara_data)
        self.chara_data = chara_data


    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            self.nextturn()
        #親クラスupdateを呼び出し、SPACEキーやクリック有効、必ず最後じゃないと一番上に表示されない
        super().update()

    def nextturn(self):
        self.chara_data.day += 1

    def draw(self):
        pyxel.cls(0)


        pyxel.text(80, 120, "room", 7) 
        
        pyxel.text(30, 10, f"DAY: {self.chara_data.day}", 7)
        pyxel.text(30, 30, f"HP: {self.chara_data.HP}", 8)
                
        #親クラスのdrawを呼び出して、メニューボタンやポップアップ
        super().draw()
