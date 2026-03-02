import pyxel

class MatchMaking:
    def update(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            #遺伝子検査ボタン
            if 97 < pyxel.mouse_x < 160 and 130 < pyxel.mouse_y < 157:
                pyxel.text(10, 60, "HELLO!", 0)
            #結婚ボタン
            elif 97 < pyxel.mouse_x < 160 and 160 < pyxel.mouse_y < 186:
                #TODO繁殖にいく
                pass
                

    def draw(self):
        pyxel.load("matchmaking2.pyxres")
        pyxel.blt(0, 0, 0, 0, 0, 255, 255, 0)
        pyxel.text(97, 130, "遺伝子検査", 0)
        pyxel.text(97, 160, "結婚", 0)
        #TODOキャラ画のサイズ確認てか作る