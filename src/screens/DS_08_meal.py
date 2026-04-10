import pyxel
from .base import Popup
#pyxel.load("assets/meal.pysres")

class meal(Popup):
    def __init__(self, game_data,chara_data):
        super().__init__(game_data,chara_data)
        self.chara_data = chara_data
        self.game_data = game_data
        self.font = pyxel.Font("misaki_gothic.bdf")
        
        

    def update(self):
        #ごはんの入力受け取り
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if 16 < pyxel.mouse_x < 79 and 24 < pyxel.mouse_y < 55:
                self.choose(self.game_data.items["Byte Bites"], self.game_data.ByteBites)
            
            elif 96 < pyxel.mouse_x < 159 and 24 < pyxel.mouse_y < 55:
                self.choose(self.game_data.items["Cookie"], self.game_data.Cookie)
            
            elif 176 < pyxel.mouse_x < 239 and 24 < pyxel.mouse_y < 55:
                self.choose(self.game_data.items["Wi-Fiバームクーヘン"], self.game_data.Wifi)

            elif 16 < pyxel.mouse_x < 79 and 72 < pyxel.mouse_y < 103:
                self.choose(self.game_data.items["SSDサンド"], self.game_data.SSD)

            elif 96 < pyxel.mouse_x < 159 and 72 < pyxel.mouse_y < 103:
                self.choose(self.game_data.items["Raspberry Pi"], self.game_data.Pi)

            elif 176 < pyxel.mouse_x < 239 and 72 < pyxel.mouse_y < 103:
                self.choose(self.game_data.items["NullNullNatto"], self.game_data.Natto)

    
    def draw(self):
        #ごはんの選択肢の描画
        #pyxel.bltm(0, 0, 0, 0, 0, 255, 255)
        pyxel.rect(72, 216, 111, 23, 7)
        pyxel.text(70, 225, "「ごはん」をえらんでください", 10)
        pyxel.rect(16, 24, 63, 31, 9)
        pyxel.rect(96, 24, 63, 31, 9)
        pyxel.rect(176, 24, 63, 31, 9)
        pyxel.rect(16, 72, 63, 31, 9)
        pyxel.rect(96, 72, 63, 31, 9)
        pyxel.rect(176, 72, 63, 31, 9)

        text_color = 0

        #上段のアイテム
        pyxel.text(20, 36, "Byte Bites", 0,self.font)
        pyxel.text(110, 36, "Cookie",0, self.font)
        
        #Wi-Fiバームクーヘンは長いので2行に分ける
        pyxel.text(180, 28, "Wi-Fi",0, self.font)
        pyxel.text(180, 38, "バームクーヘン",0,self.font)

        #下段のアイテム
        pyxel.text(25, 84, "SSDサンド",0,self.font)
        
        #ラズベリーパイ2行
        pyxel.text(100, 76, "Raspberry",0,self.font)
        pyxel.text(115, 86, "Pi",0,self.font)
        
        #納豆2行
        pyxel.text(184, 76, "NullNull",0,self.font)
        pyxel.text(190, 86, "Natto",0,self.font)

        byte_price = self.game_data.items["Byte Bites"]["price"]
        pyxel.text(10, 10, f"PRICE: {byte_price}G", 7)

        self.chara_data.HP += food["hp"]
        self.chara_data.tail += food["tail"]
        self.chara_data.size += food["size"]
        self.chara_data.IQ += food["iq"]
        

            
    def choose(self, food, have):
        if have > 0:
            pyxel.text(100, 110, food, 10, self.font)
            pyxel.text(100, 120, "をたべますか？", 10, self.font)
            pyxel.text(110, 130, "Yes / No", 10)
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                if 120 < pyxel.mouse_x < 130 and 150 < pyxel.mouse_y < 155:

                    pyxel.text(120, 120, "もぐもぐ・・・")
                    #HPとかの回復の描画

                    
        elif have <= 0:
            have == 0
            pyxel.text(120, 120, "ショップでごはんをかってね", 10)




