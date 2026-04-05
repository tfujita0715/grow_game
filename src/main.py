import pyxel
from screens.screenManager import ScreenManager

class App:
    def __init__(self):
        #initは1回のみ。サイズも固定する。
        #他で初期化するとクラッシュします
        pyxel.init(256, 256, title="grow Game",quit_key = pyxel.KEY_NONE)#esc無効化
        pyxel.mouse(True)
        
        #画面遷移をインスタンス化
        self.scmanager = ScreenManager()
        self.scmanager = ScreenManager()
        
        pyxel.run(self.update, self.draw)

    def update(self):
        self.scmanager.update()
        #sample画面遷移 これはspace
        #if pyxel.btnp(pyxel.KEY_SPACE):
            #self.screen = Screen01() 

    def draw(self):
        pyxel.cls(0)
        self.scmanager.draw()

def main():
    print("Game Started!")
    App()

if __name__ == "__main__":
    main()
    