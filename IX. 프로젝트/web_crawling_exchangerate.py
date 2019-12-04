from bs4 import BeautifulSoup
from urllib.request import urlopen
import json

if __name__ == '__main__':
    with urlopen("https://finance.naver.com/marketindex/?tabSel=exchange") as response:
        soup = BeautifulSoup(response, "lxml")
    # print(soup)

    countries = soup.find_all("h3", attrs={"class": "h_lst"})
    exchange_wons = soup.find_all("span", attrs={"class": "value"})

    a = []
    b = []
    count = 1
    for country in countries:
        country = country.find("span").text
        # print(count, "나라 : ", country)
        a.append(country)
        count += 1

    for exchange_won in exchange_wons:
        exchange_won = exchange_won.text
        # print(exchange_won, "won")
        b.append(exchange_won)

    for i in range(10):
        print(a[i], ":", b[i])

url_dict = {
    '미국 USD': 'https://finance.naver.com/marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_USDKRW',
    '유럽연합 EUR': 'https://finance.naver.com/marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_EURKRW',
    '일본 JPY (100엔)': 'https://finance.naver.com/marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_JPYKRW',
    '중국 CNY': 'https://finance.naver.com/marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_CNYKRW',
    '홍콩 HKD': 'https://finance.naver.com/marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_HKDKRW',
    '대만 TWD': 'https://finance.naver.com/marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_TWDKRW',
    '영국 GBP': 'https://finance.naver.com/marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_GBPKRW',
    '오만 OMR': 'https://finance.naver.com/marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_OMRKRW',
    '캐나다 CAD': 'https://finance.naver.com/marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_CADKRW',
    '스위스 CHF': 'https://finance.naver.com/marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_CHFKRW'
}
