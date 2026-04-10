import pyxel
from .base import Popup
#pyxel.load("assets/meal.pysres")

class meal(Popup):
    def __init__(self, game_data,chara_data):
        super().__init__(game_data,chara_data)
        self.chara_data = chara_data
        self.game_data = game_data
        
        

    def update(self):
        #ごはんの入力受け取り
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            if 16 < pyxel.mouse_x < 79 and 24 < pyxel.mouse_y < 55:
                self.choose(self.game_data.items["Byte Bites"], self.game_date.ByteBites)
            
            elif 96 < pyxel.mouse_x < 159 and 24 < pyxel.mouse_y < 55:
                self.choose(self.game_data.items["Cookie"], self.game_date.Cookie)
            
            elif 176 < pyxel.mouse_x < 239 and 24 < pyxel.mouse_y < 55:
                self.choose(self.game_data.items["Wi-Fiバームクーヘン"], self.game_date.Wifi)

            elif 16 < pyxel.mouse_x < 79 and 72 < pyxel.mouse_y < 103:
                self.choose(self.game_data.items["SSDサンド"], self.game_date.SSD)

            elif 96 < pyxel.mouse_x < 159 and 72 < pyxel.mouse_y < 103:
                self.choose(self.game_data.items["Raspberry Pi"], self.game_date.Pi)

            elif 176 < pyxel.mouse_x < 239 and 72 < pyxel.mouse_y < 103:
                self.choose(self.game_data.items["NullNullNatto"], self.game_date.Natto)

    
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

            
    def choose(self, food, have):
        if have > 0:
            pyxel.text(100, 110, food, 10, self.font)
            pyxel.text(100, 120, "をたべますか？", 10, self.font)
            pyxel.text(110, 130, "Yes / No", 10)
            #if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                #if 120 < pyxel.mouse_x < 130 and 150 < pyxel.mouse_y < 155:
            if pyxel.btnp(pyxel.KEY_Y):
                    pyxel.text(120, 120, "もぐもぐ・・・")
                    #HPとかの回復の描画
                
            elif pyxel.btnp(pyxel.KEY_N):
                pass
                    
        elif food <= 0:
            food == 0
            pyxel.text(120, 120, "ショップでごはんをかってね", 10)


