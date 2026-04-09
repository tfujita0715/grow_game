import pyxel
#画面の基底クラス共通の機能、初期化

class BaseScreen:
    def __init__(self,game_data, chara_data):
        self.game_data = game_data
        self.chara_data = chara_data
        self.next_screen = None #Noneの場合は遷移なし
    def update(self):
        pass
    def draw(self):
        pass

    def get_next_screen(self):
        return self.next_screen

class Popup(BaseScreen):
    
    def __init__(self, game_data, chara_data):
        super().__init__(game_data, chara_data)
        self.number = False
        #切り替え用のフラグ
        self.show_popup = False
        self.font = pyxel.Font("misaki_gothic.bdf")


    def update(self):
         #SPACEキーで表示/非表示を切り替え
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.show_popup = not self.show_popup

        #if pyxel.btnp
            #if 59 < pyxel.mouse_x 
            #self.next_screen = "setting"
    

    def draw(self):
        #背景・メイン画面の描画
        #pyxel.text(10, 10, "Press SPACE to toggle popup", 7)
        #左上の四角ボタンの描画
        pyxel.rect(9, 9, 16, 16, 13)#全体の四角
        pyxel.rect(12, 12, 10, 2, 7)
        pyxel.rect(12, 16, 10, 2, 7)
        pyxel.rect(12, 20, 10, 2, 7)


        #ポップアップの描画（フラグがTrueの時だけ実行）
        if self.show_popup:
            self.draw_popup()

    def draw_popup(self):
        #ポップアップの枠組み（塗りつぶし四角形）
        pyxel.rect(27, 27, 202, 202, 7)  #外枠（白）
        pyxel.rect(28, 28, 200, 200, 1)  #中身（紺）
        
        # テキストの表示
        pyxel.text(35, 35, "メニュー", 7, self.font)
        #pyxel.text(45, 65, "This is a popup!", 7)
        #pyxel.text(45, 75, "[SPACE] to close", 13)

        #各ボタンの配置
        pyxel.rect(40, 50, 50, 50, 6)
        pyxel.text(53, 65, "へやに\n\nもどる", 7, self.font)
        pyxel.rect(102, 50, 50, 50, 13)
        pyxel.text(112, 72, "せってい", 7, self.font)
        pyxel.rect(164, 50, 50, 50, 10)
        pyxel.text(174, 72, "ショップ", 7, self.font)
        pyxel.rect(40, 110, 50, 50, 8)
        pyxel.text(45, 132, "びょういん", 7, self.font)
        pyxel.rect(102, 110, 50, 50, 3)
        pyxel.text(115, 132, "トイレ", 7, self.font)
        pyxel.rect(164, 110, 50, 50, 12)
        pyxel.text(177, 132, "おふろ", 7, self.font)
        pyxel.rect(71, 170, 50, 50, 9)
        pyxel.text(84, 192, "ごはん", 7, self.font)
        pyxel.rect(133, 170, 50, 50, 0)
        pyxel.text(140, 185, "じゅんび\n\nちゅう…", 7, self.font)


        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if 39 < pyxel.mouse_x < 91 and 49 < pyxel.mouse_y < 101:
                self.next_screen = "room"

            elif 101 < pyxel.mouse_x < 153 and 49 < pyxel.mouse_y < 101:
                self.next_screen = "setting"


        #if pyxel.btnp(pyxel.KEY_Q):
            #self.next_screen = "meal"

        elif pyxel.btnp(pyxel.KEY_W):
            self.next_screen = "shop"

        elif pyxel.btnp(pyxel.KEY_E):
            self.next_screen = "toilet"

        elif pyxel.btnp(pyxel.KEY_R):
            self.next_screen = "bath"






