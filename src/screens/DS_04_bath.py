import pyxel
from .base import BaseScreen
from .imageObj import ImageObj

class Bath(BaseScreen):
    def __init__(self, game_data, chara_data):
        super().__init__(game_data, chara_data)
        self.font = pyxel.Font("misaki_gothic.bdf")
        self.chara_data = chara_data
        self.game_data = game_data
        self.security_btn = False
        self.color_btn = False
        self.bath_cancel = False
        self.showPopup = False
        #画像表示
        self.rp = ImageObj("item_+R.png", 76, 113, 0)
        self.rm = ImageObj("item_-R.png", 76, 137, 0)
        self.gp = ImageObj("item_+G.png", 107, 113, 0)
        self.gm = ImageObj("item_-G.png", 107, 137, 0)
        self.bp = ImageObj("item_+B.png", 138, 113, 0)
        self.bm = ImageObj("item_-B.png", 138, 137, 0)
        pyxel.load("assets/bath.pyxres")

    def update(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            #ポップアップ中
            if self.showPopup:
                if 103 < pyxel.mouse_x < 129 and 157 < pyxel.mouse_y < 168:
                    self.color_btn = False
                    self.showPopup = False
                return
            #戻るボタン
            if 9 < pyxel.mouse_x < 41 and 9 < pyxel.mouse_y < 21:
                self.next_screen = "room"
                return
            #風呂キャン
            if (self.game_data.isTakingBath) or (
                self.chara_data.turn == 0):
                self.bath_cancel = True
                return
            #セキュリティ風呂ボタン
            if (17 < pyxel.mouse_x < 118) and (192 < pyxel.mouse_y < 224):
                self.security_btn = True
                #キャラデータ更新
                self.chara_data.security = 100
                self.chara_data.turn -= 1
                self.game_data.isTakingBath = True
            #色風呂ボタン
            elif (140 < pyxel.mouse_x < 240) and (193 < pyxel.mouse_y < 225):
                self.color_btn = True

    def draw(self):
        pyxel.blt(0, 0, 0, 0, 0, 255, 255, 0)
        pyxel.rect(10, 10, 30, 10, 7)
        #self.image.draw()
        #pyxel.text(17, 192, "セキュリティ風呂", 0, self.font)
        #pyxel.text(140, 193, "色風呂", 0, self.font)
        pyxel.text(12, 12, "もどる", 6, self.font)
        pyxel.text(95, 12, f"セキュリティ：{self.chara_data.security}", 3, self.font)

        #セキュリティ風呂ボタン
        if self.security_btn:
            pyxel.text(70, 170, "セキュリティが100まで上がった", 0, self.font)
        #色風呂ボタン
        if self.color_btn:
            self.chooseBathBomb()
        #風呂キャンボタン
        if self.bath_cancel:
            pyxel.text(70, 180, "今日はもうおふろに入った", 0, self.font)
        

    def chooseBathBomb(self):
        self.showPopup = True
        pyxel.rect(66, 100, 97, 65, 7)
        self.rp.draw()
        self.rm.draw()
        self.gp.draw()
        self.gm.draw()
        self.bp.draw()
        self.bm.draw()
        pyxel.text(90, 101, "入浴剤を選ぶ", 1, self.font)
        pyxel.text(103, 157, "とじる", 1, self.font)
        pyxel.text(92, 126, f"{self.game_data.BathBombRp}", 0, self.font)
        pyxel.text(92, 150, f"{self.game_data.BathBombRm}", 0, self.font)
        pyxel.text(123, 126, f"{self.game_data.BathBombGp}", 0, self.font)
        pyxel.text(123, 150, f"{self.game_data.BathBombGm}", 0, self.font)
        pyxel.text(154, 126, f"{self.game_data.BathBombBp}", 0, self.font)
        pyxel.text(154, 150, f"{self.game_data.BathBombBm}", 0, self.font)
        


        
        

        