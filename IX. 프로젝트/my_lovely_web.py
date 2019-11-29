# 배스킨라빈스 월간 아이스크림 순위
from urllib.request import urlopen
from bs4 import BeautifulSoup

if __name__ == '__main__':
    with urlopen("https://www.baskinrobbins.co.kr/menu/list.php?top=A") as response:
        soup = BeautifulSoup(response, "lxml")
    # print(soup)

    ice_creams_rank = soup.find_all("span", attrs={"class": "ice_name"})
    n = 1
    print("Monthly Ice Cream Rank")
    for ice_cream_rank in ice_creams_rank:
        print(n, ice_cream_rank.text)
        n += 1

    print("")
    ice_creams = soup.find_all("figcaption")
    n = 1
    print("Ice Cream Menu")
    for ice_cream in ice_creams:
        ice_cream = ice_cream.find("span")
        print(n, ice_cream.text)
        n += 1
