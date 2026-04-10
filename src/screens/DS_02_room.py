import pyxel
import random
from .base import Popup

class RoomScreen(Popup):
    def __init__(self, game_data, chara_data):
        super().__init__(game_data, chara_data)
        self.chara_data = chara_data
        self.game_data = game_data
        self.font = pyxel.Font("misaki_gothic.bdf")

        self.chara_data.size = self.chara_data.size + 3.2
        self.daily_report = [] #ダメージや感染ログを保持
        # プログラムの場所を基準に assets フォルダ内のファイルを指定
        #path = os.path.join(os.path.dirname(__file__),"..", "..", "assets", "room.pyxres")
        #pyxel.load(path)
        #print(path)
        pyxel.load("assets/room.pyxres")
        
        if self.game_data.is_first_play:
            self.game_data.money += 10000
            self.game_data.is_first_play = False

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

            #マウスでの一日を終わるボタンクリック判定
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                if 180 <= pyxel.mouse_x <= 245 and 230 <= pyxel.mouse_y <= 245:
                    self.nextturn()


    def nextturn(self):
        self.chara_data.day += 1

        self.game_data.unko += 3
        self.is_animating = True
        self.anim_timer = 0
        self.old_day = self.chara_data.day

        self.daily_report = []

        # 1. 既に罹患している病気からのダメージ処理
        for disease in self.chara_data.diseases:
            atk = self.chara_data.DISEASE_MASTER[disease]["atk"]
            self.chara_data.HP -= atk
            self.daily_report.append(f"VIRUS DMG: -{atk} ({disease})")

        # 2. 新しい病気にかかる判定（例: 20%の確率で罹患）
        infection_rate = 0.20
        if random.random() < infection_rate:
            # まだかかっていない病気をリストアップ
            possible_diseases = [d for d in self.chara_data.DISEASE_MASTER.keys() if d not in self.chara_data.diseases]
            
            if possible_diseases:
                # ランダムで1つ選んでリストに追加
                new_disease = random.choice(possible_diseases)
                self.chara_data.diseases.append(new_disease)
                self.daily_report.append(f"WARNING: Infected with [{new_disease}]")

        # HPが0以下にならないようにする（将来的にここでゲームオーバー判定も可能）
        if self.chara_data.HP < 0:
            self.chara_data.HP = 0

        #次の日
        self.chara_data.day += 1
        self.chara_data.turn = 3

    def draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, 256, 256) 

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
            #ダメージや感染のレポートを表示
            for i, log in enumerate(self.daily_report):
                color = 8 if "DMG" in log or "WARNING" in log else 7
                pyxel.text(60, 130 + (i * 15), log, color)
            return

        pyxel.rect(180, 230, 65, 15, 5) #色は5（濃い青）
        pyxel.text(194, 235, "END DAY", 7) #テキストは白
        #pyxel.bltm(0, 0, 0, 0, 0, 256, 256)

        pyxel.text(80, 120, "room", 7) 
        
        pyxel.text(10, 30, f"DAY: {self.chara_data.day}", 7)
        pyxel.text(10, 40, f"HP: {self.chara_data.HP}", 8)

        pyxel.text(10, 50, f"MONEY: {self.game_data.money}", 10)

        index = int(self.chara_data.size)
        pyxel.text(10, 60, f"TAIL:{self.chara_data.tail:.1f}", 7)
        pyxel.text(10, 70, f"SIZE:{self.chara_data.outsidesize[index]}", 7)
        pyxel.text(10, 80, f"IQ:{self.chara_data.IQ:.1f}", 7)
        pyxel.text(10, 90, f"HP:{self.chara_data.HP}", 7)

        #病気中なら警告を出す
        if self.chara_data.diseases:
            pyxel.text(10, 100, "STATUS: SICK!", 8,self.font)
                
        #親クラスのdrawを呼び出して、メニューボタンやポップアップ
        super().draw()
