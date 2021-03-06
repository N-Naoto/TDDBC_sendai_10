import random

from typing import get_args
import pytest

from ichigo.ichigo import いちご


class TestIchigo:
    @pytest.mark.parametrize(
        "品種, サイズ, expected",
        (
            ("あまおう", "S", "あまおう: S"),
            ("とちおとめ", "M", "とちおとめ: M"),
            ("もういっこ", "L", "もういっこ: L"),
        ),
    )
    def test_いちごの文字列表現(self, 品種: str, サイズ: str, expected: str):
        ichigo = いちご(品種, サイズ)

        assert str(ichigo) == expected

    def test_サイズではなく重さを直接与えていちごを作成できる_25gはLLサイズ_下限(self):
        ichigo = いちご.create_from_weight("あまおう", 25)

        assert str(ichigo) == "あまおう: LL"

    def test_サイズではなく重さを直接与えていちごを作成できる_24gはLサイズ_上限(self):
        ichigo = いちご.create_from_weight("あまおう", 24)

        assert str(ichigo) == "あまおう: L"

    def test_サイズではなく重さを直接与えていちごを作成できる_20gはLサイズ_下限(self):
        # MEMO: メソッド名は and品種 も必要なのでは？
        ichigo = いちご.create_from_weight("あまおう", 20)

        assert str(ichigo) == "あまおう: L"

    def test_サイズではなく重さを直接与えていちごを作成できる_19gはMサイズ_上限(self):
        ichigo = いちご.create_from_weight("あまおう", 19)

        assert str(ichigo) == "あまおう: M"

    def test_サイズではなく重さを直接与えていちごを作成できる_10gはMサイズ_下限(self):
        ichigo = いちご.create_from_weight("あまおう", 10)

        assert str(ichigo) == "あまおう: M"

    def test_サイズではなく重さを直接与えていちごを作成できる_9gはMサイズ_上限(self):
        ichigo = いちご.create_from_weight("あまおう", 9)

        assert str(ichigo) == "あまおう: S"

    def test_サイズではなく重さを直接与えていちごを作成できる_1gはMサイズ_下限(self):
        ichigo = いちご.create_from_weight("もういっこ", 1)

        assert str(ichigo) == "もういっこ: S"

    def test_サイズではなく重さを直接与えていちごを作成できる_品種無関係版_9gはMサイズ_上限(self):
        # 品種が無関係ですよアピールするなら、これもあり？
        # このテスト1件があれば、よいかもしれない！(他のケースはベタ書きでいいかも！)
        # 困りポイント: REDのとき、「あれ？ どのパターンでREDになったん？」がわからん(ランダムがつらい問題)
        # ダメダメポイント: assert に ロジックがあるので、unittestになっていない！
        random_品種 = self._random_品種()
        ichigo = いちご.create_from_weight(random_品種, 9)

        assert str(ichigo) == f"{random_品種}: S"

    def _random_品種(self):
        return random.choice(["あまおう", "とちおとめ", "もういっこ"])
