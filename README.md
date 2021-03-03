## TODO
- [ ] Python仮想環境設定
    - [ ] venv作成

```
python -m venv venv

.\venv\Scripts\Activate.ps1
```

```
pip install pytest pytest-watch
```

```
pip freeze > requirements.txt
```

pipenv
poetry


## TODO
- [x] 今日の目標を確認する
    - Python版でFizzBuzzのTDDを進められたらOK
    - のこりは1人でもいける！ ってところまでいきたい
- [x] FizzBuzz問題の確認 と 最初の TODO整理


抽象度 具象度(具体度)
HighLevel LowLevel

- [ ] 整数を文字列に変換していく
    - [ ] 3 で割り切れる場合は「Fizz」と変換する ← こうなっててほしい
        - [x] ex: 3 -> 'Fizz' ← 具体例
        - [ ] ex: 6 -> 'Fizz'
    - [ ] 5 で割り切れる場合は「Buzz」と変換する
    - [ ] 15 で割り切れる場合は「FizzBuzz」と変換する
    
- [ ] 1から100まで、数字を出力する。
    - [ ] 1 -> '1'
    - [ ] 2 -> '2'
    
- [ ] 数字を出力する

### あとで調べられた嬉しい(けど、いまは調べてもいいやつ)
- [x] ターミナルで Control+L するとスッキリして捗る
- [ ] pytestのclassの名前の先頭がTestで始まらないと実行できない？
- [ ] コミットのタイミングやコミットメッセージってどうするのがいいんだろう？