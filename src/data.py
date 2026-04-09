#状態は辞書型で保存

#キャラクターの情報はここで管理すること。ファイルを使ってデータを保存する場合はjsonを使ってください。

import json
import os

class GameData:
    def __init__(self):
        self.save_file = "save_data.json"
        #setting
        self.volume = 5
        self.username = ""
        #setting
        self.money = 0
        self.hungerLevel = 100   #空腹度
        self.unko   = 0        #キャッシュ（うんち）
        self.lifespan   = 100    #寿命

        self.items = {
            "Byte Bites" : {"price": 50, "tail": 0.5, "size": 0.5, "iq": 0.5, "hp": 0},
            "Cookie" : {"price": 80, "tail": 0.75, "size": 0.75, "iq": 0.75, "hp": 0},
            "Wi-Fiバームクーヘン" : {"price": 70, "tail": 1, "size": 0.1, "iq": 0.1, "hp": 0},
            "SSDサンド" : {"price": 70, "tail": 0.1, "size": 1, "iq": 0.1, "hp": 0},
            "Raspberry Pi" : {"price": 90, "tail": 0.1, "size": 0.1, "iq": 1, "hp": 0},
            "NullNullNatto" : {"price": 40, "tail": 0, "size": 0, "iq": 0, "hp": 10},
        }

        #起動時にデータを読み込む
        self.load()
    
    def save(self):
        #現在の状態をJSONに保存する
        data = {
            "volume": self.volume,
            "username": self.username
        }
        with open(self.save_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def load(self):
            #JSONから読込
            if os.path.exists(self.save_file):
                with open(self.save_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.volume = data.get("volume", 5)
                    self.username = data.get("username", "")

class SettingData:
    def __init__(self):
        self.volume = 5


class CharacterData:
    def __init__(self):
        self.turn = 3        #残りのターン数
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







