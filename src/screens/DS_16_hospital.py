import pyxel
from .base import Popup

class HospitalScreen(Popup):
    def __init__(self, game_data):
        super().__init__(game_data)
        self.menu_index = 0
        self.message = "病院へようこそ"
        self.sub_mode = "TOP" 

    def update(self):
        if self.sub_mode == "TOP":
            if pyxel.btnp(pyxel.KEY_UP): self.menu_index = (self.menu_index - 1) % 4
            if pyxel.btnp(pyxel.KEY_DOWN): self.menu_index = (self.menu_index + 1) % 4
            
            if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_RETURN):
                if self.menu_index == 0: self.sub_mode = "EXAM"
                elif self.menu_index == 1: self.sub_mode = "TREAT"
                elif self.menu_index == 2: self.message = "遺伝子検査中..."
                elif self.menu_index == 3: self.next_screen = "main"

        elif self.sub_mode == "EXAM":
            if pyxel.btnp(pyxel.KEY_B): self.sub_mode = "TOP"
            
        elif self.sub_mode == "TREAT":
            if pyxel.btnp(pyxel.KEY_B): self.sub_mode = "TOP"
            if pyxel.btnp(pyxel.KEY_SPACE) and self.game_data.active_diseases:
                cured = self.game_data.active_diseases.pop(0)
                self.game_data.next_turn() 
                self.sub_mode = "TOP"

    def draw(self):
        pyxel.cls(0)
        pyxel.text(10, 10, "--- 病院 ---", 12)
        pyxel.text(10, 25, self.message, 7)
        
        if self.sub_mode == "TOP":
            menus = ["1. 検査 (病気にかかっているか確認)", "2. 治療 (薬を飲んで治す)", "3. 遺伝子検査 (自分と相手の遺伝子)", "4. 戻る"]
            for i, m in enumerate(menus):
                color = 10 if i == self.menu_index else 7
                pyxel.text(20, 50 + i * 10, m, color)

        elif self.sub_mode == "EXAM":
            pyxel.text(10, 50, "【 検査結果 】", 14)
            if not self.game_data.active_diseases:
                pyxel.text(20, 70, "健康です：異常なし", 11)
            else:
                for i, d in enumerate(self.game_data.active_diseases):
                    pyxel.text(20, 70 + i * 10, f"{d}: 陽性 (True)", 8)
            pyxel.text(10, 140, "[B] 戻る", 6)

        elif self.sub_mode == "TREAT":
            pyxel.text(10, 50, "【 治療室 】", 14)
            if not self.game_data.active_diseases:
                pyxel.text(20, 70, "治療が必要な病気はありません。", 7)
            else:
                d = self.game_data.active_diseases[0]
                drug = self.game_data.DISEASE_MASTER[d]["drug"]
                pyxel.text(20, 70, f"現在の病気: {d}", 7)
                pyxel.text(20, 80, f"処方される薬: {drug}", 10)
                pyxel.text(20, 100, "スペースキーで薬を飲む", 13)
                pyxel.text(20, 110, "※1ターン消費します", 6)
            pyxel.text(10, 140, "[B] 戻る", 6)