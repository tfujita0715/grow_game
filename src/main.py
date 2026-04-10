import os
import sys
import pyxel

from screens.screenManager import ScreenManager
from data import GameData
from data import CharacterData
from data import SettingData
class App:
    def __init__(self):
        #initは1回のみ。サイズも固定する。
        #他で初期化するとクラッシュします
        pyxel.init(256, 256, title="grow Game",quit_key = pyxel.KEY_NONE)#esc無効化
        pyxel.mouse(True)
        
        self.game_data = GameData()
        self.chara_data = CharacterData()
        #画面遷移をインスタンス化
        self.scmanager = ScreenManager(self.game_data,self.chara_data)

        
        pyxel.run(self.update, self.draw)

    def update(self):
        self.scmanager.update()


    def draw(self):
        pyxel.cls(0)
        self.scmanager.draw()


def main():
    print("Game Started!")

    #exeビルド時のおまじないらしい
    if getattr(sys, 'frozen', False):
        os.chdir(sys._MEIPASS)

    App()

if __name__ == "__main__":
    main()
    