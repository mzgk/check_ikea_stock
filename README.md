# IKEAの在庫確認スクリプト
- IKEAの在庫管理のURLから取得したXMLをパースして、次回入荷日などの情報を出力する
- Python 3.7.3

## 使い方
- 複合商品（天板＋脚のような机）は、次回入荷日が返却されない -> APIの仕様？
- その場合は、個別（天板のみ等）で検索
```bash
$ ikea.py 商品コード
```

## 動機
- 家のデスクをもう少し大きくしたくて、BEKANT(120x80)を買おう！
- TokyoBay店頭で確認したら在庫がなかった...
- 店員さんに聞いたら次回入荷日を教えてくれた
- 帰ってから試しにサイトで在庫確認したら、次回入荷日はなく「再入荷は未定です...」
- APIがあるはず
- ちょうどQiitaでIKEAの在庫情報をRubyで取得する記事がtwitterで流れてきた
  - https://qiita.com/sasasoni/items/b8223453542c90689b84
- Pythonで作ってみるか

## 概要
### パッケージ
- requests
  - HTTPクライアント。指定したURLにアクセスし、HTML/XMLデータを取得する
- BeautifulSoup4
  - HTML/XMLを解析するパッケージ

### 処理
- 実行時の引数で入力した商品コードを取得する
- requests.get()で在庫確認APIを叩いて結果（XML）を取得
- BeautifulSoupでXMLを解析する
- 店舗、在庫、次回入荷日を出力する


## IKEA-API
### 在庫管理URL
- https://www.ikea.com/jp/ja/catalog/availability/商品コード8桁/

### XML要素
- 店舗コード
  - `<localStore buCode="447" timeZoneOffsetInMillis="32400000">`
  - "447" => "TokyoBay"
  - "448" => "港北"
  - "887" => "新三郷"
  - "486" => "神戸"
  - "392" => "仙台"
  - "509" => "長久手"
  - "496" => "鶴浜"
  - "189" => "福岡新宮"
  - "359" => "立川"
- 次回入荷日 ※在庫がある場合は要素なし
  - `<restockDate>2019-05-09</restockDate>`
- 在庫数
  - `<availableStock>0</availableStock>`
- 列 ※天板＆脚のような組み合わせ商品番号の場合は、パーツに応じて存在
  - `<box>14</box>`
- 棚 ※天板＆脚のような組み合わせ商品番号の場合は、パーツに応じて存在
  - `<shelf>29</shelf>`
