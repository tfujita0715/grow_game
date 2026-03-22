#状態は辞書型で保存

#キャラクターの情報はここで管理すること。ファイルを使ってデータを保存する場合はjsonを使ってください。

class SettingData:
    def __init__(self):
        self.volume = 5


class CharacterData:
    def __init__(self):
        self.day = 1         #現在の日付
        self.HP = 100        #体力
        self.maxHP = 100     #最大HP
        self.gene = None     #遺伝子
        self.RGB = None      
        self.tail = 0        #尻尾
        self.size = 0        #大きさ
        self.IQ = 0          #賢さ
        #病気
        self.security = 0    #セキュリティ
        self.diseases = []   #病気リスト

        #病気データ定義
        self.DISEASE_MASTER = {
            "ぬるぽ":{
                "atk": 5, 
                "recovery": 100, 
                "drug": "ｶﾞｯ",
            },
            "Syntax Error":{
                "atk": 15,
                "recovery": 80, 
                "drug": "", 
            },
            "トロイの木馬":{
                "atk": 20, 
                "recovery": 10, 
                "drug": "", 
            },
            "SQLインジェクション":{
                "atk": 15,
                "recovery": 70,
                "drug": "",
            },
            "0xc00000d":{
                "atk": 30,
                "recovery": 0,
                "fatal": 100,
                "drug": "余命",
            },
            "404 not found": {
                "atk": 15,
                "recovery": 50,
                "drug": "",
            },
            "#N/A": {
                "atk": 10,
                "recovery": 90,
                "drug": "f",
            }
        }



class GameData:
    def __init__(self):
        self.money = 0
        self.hungerLevel    #空腹度
        self.unko           #キャッシュ（うんち）
        self.lifespan       #寿命



