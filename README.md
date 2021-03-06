# TDDBC Sendai X


## お題まとめ
- [はじめに](https://hackmd.io/opUU1f8lTh6VwDsyZoIy6A))
- [お題1](https://hackmd.io/@135yshr/rkxjun1mO)
- [お題2](https://hackmd.io/@135yshr/rkD0_3Jmd)

## 気になること とか あとで調べられた嬉しい(けど、いまは調べなくてもいいやって判断したやつ)
- [ ] クラスの書き方が怪しい
- [ ] エラー文読み慣れてない
- [ ] classmethodとはなんですか？

## TODO
- [x] strawberryのスペルがむずいので、ichigoにした！

### お題1: いちごの文字列表現を取得できる
- [x] いちごの文字列表現を取得できる
    - [x] 品種: あまおう, サイズ: S => 'あまおう: S'
    - [x] 品種: とちおとめ, サイズ: M => 'とちおとめ: M'
    - [x] 品種: もういっこ, サイズ: L => 'もういっこ: L'
    - [x] テストコードが似通っていて、重複なのかな？ 気になる
        - [x] 通称: パラメタライズドテスト
    - [x] テストの件数と範囲はどうしよう？ ← ぶっちゃけ LL とか、 全組み合わせはやらなくてよさそう。意味がないというか、テストをやった嬉しさが増えない。

### お題2: 重さからのいちご作成
- [ ] サイズではなく、重さを直接与えて、いちごを作成する。
    - [x] 25g以上 → LL
        - [ ] 上限: ん？ 上限ってないのか？ お題には書いてないなあ。
        - [x] 下限: (あまおう、25) -> LLサイズのあまおう → str((あまおう、25)) == 'あまおう: LL'
    - [x] 20g以上24g以下 → L
        - [x] 上限: (あまおう, 24) → L
        - [x] 下限: (あまおう, 20) → L 
    - [x] 10g以上19g以下 → M
        - [x] 上限: (あまおう, 19) → M
        - [x] 下限: (あまおう, 10) → M 
    - [x] 1g以上9g以下 → S
        - [x] 下限: (あまおう, 1) → S
        - [x] 上限: (あまおう, 9) → S 
    - [ ] COMMENT: テストケースが あまおう だけなので、あまおうだけ重さから作れちゃうと勘違いしちゃうんじゃね？
        - [x] 「もういっこ」のケースを追加する
    - [ ] あとで
        - [ ] 1g のいちごって現実にありえるのか？
        - [ ] 例外系のテストはあとまわし！
            - [ ] いちごの重さは 0g以下 とか 文字列はどうするとか
        - [ ] 区分オブジェクト(Enum)にする
            - [ ] 品種クラス
            - [ ] サイズクラス
        

### お題1の整理
品種 と サイズ を与えて、 いちご をclassで作成する。
その文字列表現を取得する。

- 文字列表現の例
    - `あまおう: S`
    - `とちおとめ: M` 
    - `もういっこ: L`
- 品種とサイズの情報
    - 品種は、 `あまおう` `とちおとめ` `もういっこ` の3種類
    - いちごのサイズは `S` `M` `L` `LL` の4種類


### お題2の整理
サイズではなく、重さを直接与えて、いちごを作成する。

- 25g以上 → LL
- 20g以上25g未満 → L
- 10g以上20g未満 → M
- 1g以上10g未満 → S

例えば、 重さが 8g の あまおうの場合は、 あまおう: S という文字列表現になります。

- ただし、
    - いちごの重さは 1g以上とし 0g以下は対象としない。 ← テストしなくていいのか？ 
