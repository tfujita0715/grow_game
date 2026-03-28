import pyxel

class MatchMaking:
    def __init__(self, item, characters):
        self.item = item
        self.characters = characters
        self.partner = None
        self.tester = None
        self.test_btn = False
        

    def update(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            #遺伝子検査ボタン
            if 97 < pyxel.mouse_x < 160 and 130 < pyxel.mouse_y < 157:
                self.test_btn = True
                self.tester = self.characters[0]
            #結婚ボタン
            elif 97 < pyxel.mouse_x < 160 and 160 < pyxel.mouse_y < 186:
                self.partner = self.characters[0]
                #TODO繁殖にいく
                #TODOdata.pyとやりとりして、結婚相手を登録する

    def draw(self):
        pyxel.load("matchmaking2.pyxres")
        pyxel.blt(0, 0, 0, 0, 0, 255, 255, 0)
        pyxel.text(97, 130, "遺伝子検査", 0)
        pyxel.text(97, 160, "結婚", 0)
        #TODOキャラ画のサイズ確認てか作る

        #検査ボタン押されたとき
        if self.test_btn == True:
            #TODOアイテムがあれが、遺伝子検査の結果を表示して、キット４→３（キットの数を表示）
            pass