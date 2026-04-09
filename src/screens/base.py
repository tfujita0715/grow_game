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
        pyxel.text(35, 35, "メニュー", 10, self.font)
        #pyxel.text(45, 65, "This is a popup!", 7)
        #pyxel.text(45, 75, "[SPACE] to close", 13)

        #各ボタンの配置
        pyxel.rect(40, 50, 50, 50, 7)
        pyxel.rect(102, 50, 50, 50, 7)
        pyxel.rect(164, 50, 50, 50, 7)
        pyxel.rect(40, 110, 50, 50, 7)
        pyxel.rect(102, 110, 50, 50, 7)
        pyxel.rect(164, 110, 50, 50, 7)
        pyxel.rect(71, 170, 50, 50, 7)
        pyxel.rect(133, 170, 50, 50, 7)


        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if 39 < pyxel.mouse_x < 91 and 49 < pyxel.mouse_y < 101:
                self.next_screen = "room"

            elif 101 < pyxel.mouse_x < 153 and 49 < pyxel.mouse_y < 101:
                self.next_screen = "setting"



