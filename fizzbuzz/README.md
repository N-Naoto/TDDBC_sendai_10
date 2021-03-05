# FizzBuzz TDD
## TODO

- [x] 今日の目標を確認する
    - Python版でFizzBuzzのTDDを進められたらOK
    - のこりは1人でもいける！ ってところまでいきたい
- [x] FizzBuzz問題の確認 と 最初の TODO整理
- MEMO: 抽象度 / 具象度(具体度) , HighLevel / LowLevel

- [ ] 整数を文字列に変換していく
    - [x] 3 で割り切れる場合は「Fizz」と変換する ← こうなっててほしい
        - [x] ex: 3 -> 'Fizz' ← 具体例
        - [x] ex: 6 -> 'Fizz'
    - [ ] 5 で割り切れる場合は「Buzz」と変換する
        - [x] ex: 5 -> 'Buzz' ← 具体例
    - [ ] 15 で割り切れる場合は「FizzBuzz」と変換する

- [ ] 1から100まで、数字を出力する。
    - [ ] 1 -> '1'
    - [ ] 2 -> '2'

- [ ] 数字を出力する

## あとで調べられた嬉しい(けど、いまは調べてもいいやつ)

- [x] ターミナルで Control+L するとスッキリして捗る
- [ ] pytestのclassの名前の先頭がTestで始まらないと実行できない？
- [ ] コミットのタイミングやコミットメッセージってどうするのがいいんだろう？

## 環境構築手順

```
$ python -m venv venv

# PowerShellの場合
$ .\venv\Scripts\Activate.ps1
```

```
$ pip install pytest pytest-watch
```

```
$ pip freeze > requirements.txt
```

