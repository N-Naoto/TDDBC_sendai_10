from ichigo.ichigo import Ichigo


class TestIchigo:
    def test_いちごの文字列表現を取得できる_あまおうSサイズ(self):
        ichigo = Ichigo("あまおう", "S")

        assert str(ichigo) == "あまおう: S"
