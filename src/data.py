#状態は辞書型で保存

#キャラクターの情報はここで管理すること。ファイルを使ってデータを保存する場合はjsonを使ってください。

class SettingData:
    def __init__(self):
        self.volume = 5


class CharacterData:
    def __init__(self):
        self.volume = 5
        self.day = 1         #現在の日付
        self.HP = 100        #体力
        self.maxHP = 100     #最大HP
        self.security = 0    #セキュリティ
        self.gene = None     #遺伝子
        self.RGB = None      
        self.tail = 0        #尻尾
        self.size = 0        #大きさ
        self.IQ = 0          #賢さ



class GameData:
    def __init__(self):
        self.money = 0
        self.hungerLevel    #空腹度
        self.unko           #キャッシュ（うんち）
        self.lifespan       #寿命

