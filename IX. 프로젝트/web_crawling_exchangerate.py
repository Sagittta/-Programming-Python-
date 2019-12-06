from bs4 import BeautifulSoup
from urllib.request import urlopen
import json

if __name__ == '__main__':
    # https://finance.naver.com/marketindex/?tabSel=exchange
    # iframe 안으로 들어감
    with urlopen("https://finance.naver.com/marketindex/exchangeList.nhn") as response:
        soup = BeautifulSoup(response, "lxml")
    # print(soup)

    countries = soup.find_all("td", attrs={"class": "tit"})
    exchange_wons = soup.find_all("td", attrs={"class": "sale"})

    a = []
    b = []
    count = 1
    for country in countries:
        country = country.find("a").text
        country = country.split()
        country = country[0] + " " + country[1]
        # print(count, "나라 : ", country)
        a.append(country)
        count += 1

    for exchange_won in exchange_wons:
        exchange_won = exchange_won.text
        # print(exchange_won, "won")
        b.append(exchange_won)

    for i in range(10):
        print(a[i], ":", b[i], "원")
