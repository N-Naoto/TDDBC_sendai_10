class いちご:
    def __init__(self, 品種: str, サイズ: str) -> None:
        self.品種 = 品種
        self.サイズ = サイズ

    def __str__(self) -> str:
        return self.品種 + ': ' + self.サイズ
