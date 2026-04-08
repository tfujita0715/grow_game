import pyxel
#画面の基底クラス共通の機能、初期化

class BaseScreen:
    def __init__(self,game_data, chara_data):
        self.game_data = game_data, chara_data
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

    def update_common(self):
         #SPACEキーで表示/非表示を切り替え
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.show_popup = not self.show_popup
    

    def draw_common(self):
            #背景・メイン画面の描画
            pyxel.cls(0)
            pyxel.text(10, 10, "Press SPACE to toggle popup", 7)
            pyxel.circ(80, 60, 20, 11) # メイン画面のキャラ代わり

            #ポップアップの描画（フラグがTrueの時だけ実行）
            if self.show_popup:
                self.draw_popup()

    def draw_popup(self):
        #ポップアップの枠組み（塗りつぶし四角形）
        pyxel.rect(35, 35, 92, 52, 7)  #外枠（白）
        pyxel.rect(36, 36, 90, 50, 1)  #中身（紺）
        
        # テキストの表示
        pyxel.text(50, 50, "INFORMATION", 10)
        pyxel.text(45, 65, "This is a popup!", 7)
        pyxel.text(45, 75, "[SPACE] to close", 13)
