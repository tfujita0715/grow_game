import pyxel

class Breed:#[ ]繁殖にするか結婚にするか
    def __init__(self, item, partner):
        self.item = item
        self.partner = partner
        self.get_married = False
        
    
    def update(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            #繁殖ボタン
            if 95 < pyxel.mouse_x < 167 and 123 < pyxel.mouse_y < 150:
                self.get_married = True
                #TODOクリックしたら部屋に戻る

            #選びなおすボタン
            elif 91 < pyxel.mouse_x < 172 and 230 < pyxel.mouse_y < 251:
                #TODOお見合いに戻る、data.pyのpartner情報を破棄
                pass

    def draw(self):
        pyxel.load("breed.pyxres")
        pyxel.blt(0, 0, 0, 0, 0, 255, 255, 0)
        pyxel.text(95, 123, "繁殖", 0)
        pyxel.text(91, 230, "選びなおす", 0)

        if self.get_married == True:
            #TODO子供の姿を描画、部屋に戻るボタン作るかも
            pass