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

    def test_サイズではなく重さを直接与えていちごを作成できる_25gはLLサイズ(self):
        ichigo = いちご.create_from_weight("あまおう", 25)

        assert str(ichigo) == "あまおう: LL"

    def test_サイズではなく重さを直接与えていちごを作成できる_20gはLサイズ(self):
        # MEMO: メソッド名は and品種 も必要なのでは？
        ichigo = いちご.create_from_weight("あまおう", 20)

        assert str(ichigo) == "あまおう: L"
