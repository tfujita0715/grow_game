import pyxel
import os
from .base import BaseScreen, Popup

class RoomScreen(Popup):
    def __init__(self, game_data, chara_data):
        super().__init__(game_data, chara_data)
        self.chara_data = chara_data

        # プログラムの場所を基準に assets フォルダ内のファイルを指定
        #path = os.path.join(os.path.dirname(__file__),"..", "assets", "room.pyxres")
        #pyxel.load(path)
        #print(path)
        #pyxel.load(r"assets\room.pyxres")
        #pyxel.load("C:/pyxel/grow2/grow_game/assets/room.pyxres")
        


    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            self.nextturn()
        #親クラスupdateを呼び出し、SPACEキーやクリック有効、必ず最後じゃないと一番上に表示されない
        super().update()

    def nextturn(self):
        self.chara_data.day += 1

        self.game_data.unko += 3

    def draw(self):
        
        pyxel.bltm(0, 0, 0, 0, 0, 256, 256)


        pyxel.text(80, 120, "room", 7) 
        
        pyxel.text(30, 10, f"DAY: {self.chara_data.day}", 7)
        pyxel.text(30, 30, f"HP: {self.chara_data.HP}", 8)
                
        #親クラスのdrawを呼び出して、メニューボタンやポップアップ
        super().draw()
