import pyxel
from .base import BaseScreen

class NameInputScreen(BaseScreen):
    def __init__(self, game_data):
        super().__init__(game_data)
        self.input_text = ""
        #Pyxelで入力可能な文字
        self.valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    def update(self):
        #1文字ずつ入力を受け付けるs
        for char in self.valid_chars:
            if pyxel.btnp(getattr(pyxel, f"KEY_{char.upper()}")):
                if len(self.input_text) < 10:
                    self.input_text += char

        if pyxel.btnp(pyxel.KEY_BACKSPACE) and len(self.input_text) > 0:
            self.input_text = self.input_text[:-1]

        #enterで確定&画面遷移
        if pyxel.btnp(pyxel.KEY_RETURN) and len(self.input_text) > 0:
            self.game_data.username = self.input_text
            self.game_data.save() #名前を保存
            self.next_screen = "story" #次はストーリー

    def draw(self):
        pyxel.cls(0)
        pyxel.text(70, 100, "name nyuuryoku:", 7)
        pyxel.text(70, 120, f"> {self.input_text}", 10)
        pyxel.text(70, 150, "PRESS ENTER", 6)