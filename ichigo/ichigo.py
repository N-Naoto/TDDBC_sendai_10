from __future__ import annotations


class いちご:
    def __init__(self, 品種: str, サイズ: str) -> None:
        self.品種 = 品種
        self.サイズ = サイズ

    def __str__(self) -> str:
        return f"{self.品種}: {self.サイズ}"

    @classmethod
    def create_from_weight(cls, 品種: str, 重さ: int) -> いちご:
        if 25 <= 重さ:
            return いちご(品種, "LL")

        if 20 <= 重さ < 25:
            return いちご(品種, "L")
