import pyxel
from .base import Popup

class RoomScreen(Popup):
    def __init__(self, game_data, chara_data):
        super().__init__(game_data, chara_data)
        self.chara_data = chara_data
        self.game_data = game_data

        # プログラムの場所を基準に assets フォルダ内のファイルを指定
        #path = os.path.join(os.path.dirname(__file__),"..", "assets", "room.pyxres")
        #pyxel.load(path)
        #print(path)
        #pyxel.load(r"assets\room.pyxres")
        #pyxel.load("C:/pyxel/grow2/grow_game/assets/room.pyxres")
        


        #アニメーション用の変数
        self.is_animating = False  #アニメーション中かどうかのフラグ
        self.anim_timer = 0        #アニメーションの進行度（フレーム数）
        self.old_day = 0           #変わる前の日数
    def update(self):
        #アニメーション中の処理（操作ロック）
        if self.is_animating:
            self.anim_timer += 1
            #60フレーム（約2秒）経ったらアニメーション終了
            if self.anim_timer >= 60:
                self.is_animating = False
            
            #（操作不可）
            return
        
        #親クラスupdateを呼び出し、SPACEキーやクリック有効、必ず最後じゃないと一番上に表示されない
        #こっちは最初に
        super().update()
        #ポップアップが開いていない時だけ操作を可能
        if not self.show_popup:
            
            #Qキーでの終了
            if pyxel.btnp(pyxel.KEY_Q):
                self.nextturn()
            
            #Wキーでターン消費（テスト用）
            if pyxel.btnp(pyxel.KEY_W):
                if self.chara_data.turn > 0:
                    self.chara_data.turn -= 1

            #マウスでの「一日を終わる」ボタンクリック判定
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                if 180 <= pyxel.mouse_x <= 245 and 230 <= pyxel.mouse_y <= 245:
                    self.nextturn()


    def nextturn(self):
        self.is_animating = True
        self.anim_timer = 0
        self.old_day = self.chara_data.day
        #次の日
        self.chara_data.day += 1
        self.chara_data.turn = 3

    def draw(self):
        #アニメーション専用画面
        if self.is_animating:
            pyxel.cls(0)
            
            if self.anim_timer < 20:
                #古い日付だけ表示
                pyxel.text(100, 120, f"DAY {self.old_day}", 7)
            elif self.anim_timer < 40:
                #変化を表示
                pyxel.text(100, 120, f"DAY {self.old_day} -> {self.chara_data.day}", 10) # 色を黄色(10)に
            else:
                #新しい日付だけ表示
                pyxel.text(100, 120, f"DAY {self.chara_data.day}", 7)
            return
        pyxel.cls(0)

        pyxel.rect(180, 230, 65, 15, 5) # 色は5（濃い青）
        pyxel.text(194, 235, "END DAY", 7) # テキストは白

        pyxel.text(80, 120, "room", 7) 
        
        pyxel.text(10, 30, f"DAY: {self.chara_data.day}", 7)
        pyxel.text(10, 40, f"HP: {self.chara_data.HP}", 8)

        pyxel.text(10, 50, f"MONEY: {self.game_data.money}", 10)

        pyxel.text(10, 60, f"TAIL:{self.chara_data.tail:.1f}", 7)
        pyxel.text(10, 70, f"SIZE:{self.chara_data.size:.1f}", 7)
        pyxel.text(10, 80, f"IQ:{self.chara_data.IQ:.1f}", 7)
        pyxel.text(10, 90, f"HP:{self.chara_data.HP}", 7)
                
        #親クラスのdrawを呼び出して、メニューボタンやポップアップ
        super().draw()