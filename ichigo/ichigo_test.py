from ichigo.ichigo import いちご


class TestIchigo:
    def test_いちごの文字列表現を取得できる_あまおうSサイズ(self):
        ichigo = いちご("あまおう", "S")

        assert str(ichigo) == "あまおう: S"

    def test_いちごの文字列表現を取得できる_とちおとめMサイズ(self):
        ichigo = いちご("とちおとめ", "M")

        assert str(ichigo) == "とちおとめ: M"

    def test_いちごの文字列表現を取得できる_もういっこLサイズ(self):
        ichigo = いちご("もういっこ", "L")

        assert str(ichigo) == "もういっこ: L"
