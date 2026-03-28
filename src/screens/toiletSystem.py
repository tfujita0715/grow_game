import random
import time

class ToiletSystem:
    def __init__(self):
        self.cache = 0              # 現在のキャッシュ量
        self.max_cache = 100       # 最大キャッシュ
        self.used_today = False    # 1日1回制限
        self.minutes = 0           # 経過時間

    # キャッシュの時間経過処理
    def update(self):
        self.minutes += 1

        # 30分ごとに1増加
        if self.minutes % 30 == 0:
            self.add_cache(1)

    # ゲームを1プレイするごとに10増える
    def add_cache_from_game(self):
        self.add_cache(10)

    # キャッシュ増加処理
    def add_cache(self, value):
        self.cache = min(self.max_cache, self.cache + value)

    # ゲームプレイ可能か
    def can_play(self):
        return self.cache < self.max_cache

    # 重い状態（制限用）
    def is_heavy(self):
        return self.cache >= 80

    # トイレ（キャッシュ削除）
    def clear_cache(self):
        if self.used_today:
            return "already"

        self.used_today = True

        r = random.random()

        # 失敗（20%）→余計にクリア
        if r < 0.2:
            self.cache = 0
            return "fail"

        # 大成功（20%）
        elif r > 0.8:
            self.cache = 0
            return "perfect"

        # 成功（60%）
        else:
            amount = random.choice([30, 50, 70])
            self.cache = max(0, self.cache - amount)
            return f"success_{amount}"

    # 日付リセット
    def reset_day(self):
        self.used_today = False

def use_toilet_with_message(toilet_system):
    result = toilet_system.clear_cache()

    # すでにトイレを使ってた場合
    if result == "already":
        print("今日はもうトイレできないよ！")
        return

    # トイレ中表示（2秒）
    print("トイレ中...")
    time.sleep(2)

    # 結果表示
    if result == "fail":
        print("トイレ失敗")
    elif result == "perfect":
        print("トイレ大成功")
    elif "success" in result:
        print("トイレ成功")