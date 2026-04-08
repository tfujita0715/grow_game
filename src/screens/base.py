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

    def update(self):
         #SPACEキーで表示/非表示を切り替え
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.show_popup = not self.show_popup
    

    def draw(self):
            #背景・メイン画面の描画
            #pyxel.text(10, 10, "Press SPACE to toggle popup", 7)
            #左上の四角ボタンの描画
            pyxel.rect(9, 9, 16, 16, 13)#全体の四角
            pyxel.rect(12, 12, 10, 2, 7)
            pyxel.rect(12, 16, 10, 2, 7)
            pyxel.rect(12, 20, 10, 2, 7)


    def draw(self):
        pyxel.cls(2)
        pyxel.text(90, 40, "SETTING", 7)
        
        #背景・メイン画面の描画
        pyxel.text(10, 10, "Press SPACE to toggle popup", 7)

        #ポップアップの描画（フラグがTrueの時だけ実行）
        if self.show_popup:
            self.draw_popup()

    def draw_popup(self):
        #ポップアップの枠組み（塗りつぶし四角形）
        pyxel.rect(50, 10, 177, 71, 7)  #外枠（白）
        pyxel.rect(51, 11, 175, 69, 1)  #中身（紺）
        
        # テキストの表示
        pyxel.text(54, 12, "menu", 10)
        #pyxel.text(45, 65, "This is a popup!", 7)
        #pyxel.text(45, 75, "[SPACE] to close", 13)

        #各ボタンの配置
        pyxel.rect(60, 20, 30, 20, 7)
        pyxel.text(62, 27, "setting" , 0)
        pyxel.rect(102, 20, 30, 20, 7)
        pyxel.rect(144, 20, 30, 20, 7)
        pyxel.rect(186, 20, 30, 20, 7)
        pyxel.rect(60, 50, 30, 20, 7)
        pyxel.rect(102, 50, 30, 20, 7)
        pyxel.rect(144, 50, 30, 20, 7)
        pyxel.rect(186, 50, 30, 20, 7)

