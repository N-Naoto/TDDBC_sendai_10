class Ichigo:
    def __init__(self, ichigo, size):
        self.ichigo = ichigo
        self.size = size

    def __str__(self) -> str:
        # str() を呼ぶと ここが実行される！ == 文字列表現
        return "わーい！"
