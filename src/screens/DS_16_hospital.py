import pyxel
from .base import BaseScreen

class HospitalScreen(BaseScreen):
    def __init__(self, game_data, chara_data):
        super().__init__(game_data, chara_data)
        self.next_screen = None
        self.medicine_cost = 100
        self.font = pyxel.Font("misaki_gothic.bdf")
        self.page = "top"

    def update(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            mx, my = pyxel.mouse_x, pyxel.mouse_y
            
            #戻るボタン
            if 10 <= mx <= 50 and 230 <= my <= 245:
                if self.page == "pharmacy":
                    self.page = "result"
                elif self.page == "result":
                    self.page = "top"
                else:
                    self.next_screen = "back"
                return

            #トップ画面
            if self.page == "top":
                #診察する
                if 80 <= mx <= 160 and 100 <= my <= 125:
                    self.page = "result" #診断結果画面へ移行

            #診断結果画面
            elif self.page == "result":
                #病気がある場合のみ、薬を購入ボタンを押せるようにする
                if self.chara_data.diseases:
                    if 80 <= mx <= 160 and 190 <= my <= 215:
                        self.page = "pharmacy" #薬購入画面へ移行

            #薬購入画面
            elif self.page == "pharmacy":
                for i, disease in enumerate(self.chara_data.diseases):
                    btn_y = 70 + i * 25
                    if 150 <= mx <= 210 and btn_y <= my <= btn_y + 15:
                        #お金が足りているか
                        if self.game_data.money >= self.medicine_cost:
                            self.game_data.money -= self.medicine_cost
                            self.chara_data.diseases.remove(disease) 
                            break 

    def draw(self):

        pyxel.text(10, 10, "病院", 7, self.font) 
        pyxel.text(10, 25, f"MONEY: {self.game_data.money} G", 10)

        #トップ画面
        if self.page == "top":
            pyxel.text(10, 45, "受付", 7, self.font)
            
            # 診察ボタン
            pyxel.rect(80, 100, 80, 25, 5)
            pyxel.text(100, 109, "診察する", 7, self.font)

        #診断結果画面
        elif self.page == "result":
            pyxel.text(10, 45, "診断結果", 7, self.font)

            if not self.chara_data.diseases:
                pyxel.text(20, 70, "ステータス: 健康", 11, self.font)
                pyxel.text(20, 85, "病気にはかかっていません。", 13, self.font)
            else:
                pyxel.text(20, 60, "以下のウイルスが検出されました:", 8, self.font)
                for i, disease in enumerate(self.chara_data.diseases):
                    y = 75 + i * 15
                    pyxel.text(20, y, f"・{disease}", 8, self.font) # 病名だけリスト表示

                # 薬を購入ボタン
                pyxel.rect(80, 190, 80, 25, 5)
                pyxel.text(95, 199, "薬を購入", 7, self.font)

        #薬購入画面の描画
        elif self.page == "pharmacy":
            pyxel.text(10, 45, "処方箋 (薬の購入)", 7, self.font)

            if not self.chara_data.diseases:
                pyxel.text(20, 70, "治療が必要な病気はありません。", 13, self.font)
            else:
                for i, disease in enumerate(self.chara_data.diseases):
                    y = 70 + i * 25
                    d_info = self.chara_data.DISEASE_MASTER[disease]
                    atk = d_info["atk"]
                    drug_name = d_info["drug"] if d_info["drug"] else "汎用ワクチン"

                    # 病名と薬の情報を表示
                    pyxel.text(20, y, f"病気:{disease}", 8, self.font) 
                    pyxel.text(20, y + 10, f"薬:{drug_name}", 7, self.font)

                    # BUYボタンの描画
                    pyxel.rect(150, y, 60, 15, 5)
                    text_color = 7 if self.game_data.money >= self.medicine_cost else 13
                    pyxel.text(152, y + 4, f"BUY({self.medicine_cost}G)", text_color)

        #戻るボタン
        pyxel.rect(10, 230, 40, 15, 5)
        pyxel.text(18, 235, "BACK", 7)