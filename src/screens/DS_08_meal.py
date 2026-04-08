import pyxel
from .base import BaseScreen
pyxel.load("meal.pysres")

class meal(BaseScreen):
    def __init__(self, game_data,chara_data):
        super().__init__(game_data,chara_data)
        self.chara_data = chara_data
        self.game_data = game_data
        choice = False
        

    def update(self):
        #ごはんの入力受け取り
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            if 16 < pyxel.mouse_x < 79 and 24 < pyxel.mouse_y < 55:
                
                self.choose(ByteBites, "バイトバイツ")
            
            elif 96 < pyxel.mouse_x < 159 and 24 < pyxel.mouse_y < 55:
                self.game_data.items["Cookie"]
                self.choose(cookie, "Cookie")
            
            elif 176 < pyxel.mouse_x < 239 and 24 < pyxel.mouse_y < 55:
                self.choose(WiFi, "Wi-Fiバームクーヘン")

            elif 16 < pyxel.mouse_x < 79 and 72 < pyxel.mouse_y < 103:
                self.choose(SSD, "SSDサンド")

            elif 96 < pyxel.mouse_x < 159 and 72 < pyxel.mouse_y < 103:
                self.choose(Raspberry, "Raspberry Pi")

            elif 176 < pyxel.mouse_x < 239 and 72 < pyxel.mouse_y < 103:
                self.choose(Natto, "NullNullNatto")
    
    def draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, 255, 255)
        pyxel.rect(72, 216, 111, 23, 7)
        pyxel.text(90, 220, "ご飯を選んでください", 10)
        pyxel.rect(16, )
        

    def choose(self, food, name):
        while(self.choice == False):
            if food > 0:
                pyxel.text(120, 90, name, 10)
                pyxel.text(120, 120, "をたべますか？" 10)
                pyxel.text(120, 150, "Yes / No", 10)
        


            else:
                pyxel.text(120, 120, "ショップでごはんを購入してね", 10)

