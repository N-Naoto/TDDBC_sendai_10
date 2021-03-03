from fizzbuzz import fizzbuzz_convert


class TestFizzBuzz:
    def test_3で割り切れる整数をFizzに変換する_3の場合(self):
        assert fizzbuzz_convert(3) == 'Fizz'

    def test_5で割り切れる整数をBuzzに変換する_5の場合(self):
        assert fizzbuzz_convert(5) == 'Buzz'

