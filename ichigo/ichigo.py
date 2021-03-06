from __future__ import annotations


class いちご:
    def __init__(self, 品種: str, サイズ: str) -> None:
        self.品種 = 品種
        self.サイズ = サイズ

    def __str__(self) -> str:
        return f"{self.品種}: {self.サイズ}"

    @classmethod
    def create_from_weight(cls, 品種: str, 重さ: int) -> いちご:
        # 嬉しい: 上限を抑えているので、順序変更に強い
        # 悲しい: 条件がかわると 2箇所 直さないといけない
        #        25g -> 30 になったら、2箇所
        if 25 <= 重さ:
            return いちご(品種, "LL")

        if 20 <= 重さ <= 24:
            return いちご(品種, "L")

        if 10 <= 重さ <= 19:
            return いちご(品種, "M")

        if 1 <= 重さ <= 9:
            return いちご(品種, "S")
