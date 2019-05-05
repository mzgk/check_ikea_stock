import requests
from bs4 import BeautifulSoup

AVAILABILITY_URL = 'https://www.ikea.com/jp/ja/iows/catalog/availability/'
STORE_NAME = {
    '447': 'TokyoBay',
    '448': '港北',
    '887': '新三郷',
    '486': '神戸',
    '392': '仙台',
    '509': '長久手',
    '496': '鶴浜',
    '189': '福岡新宮',
    '359': '立川'
}


def main(store_code: str):
    # 在庫確認APIを叩いて結果XMLを取得
    url = AVAILABILITY_URL + store_code
    r = requests.get(url)

    # BeautifulSoupでXMLを解析する
    soup = BeautifulSoup(r.content, 'xml')
    # print(soup.prettify())

    # XMLから店舗別の情報を抜き出す
    for store in soup.find_all('localStore'):
        # print(store.prettify())
        store_code = store['buCode']
        print('店舗: {}'.format(STORE_NAME[store_code]))
        print('在庫: {}'.format(store.availableStock.string))
        if store.restockDate:
            print('次回入荷: {}'.format(store.restockDate.string))
        print('----------')


if __name__ == '__main__':
    code = '70366289'
    main(code)
