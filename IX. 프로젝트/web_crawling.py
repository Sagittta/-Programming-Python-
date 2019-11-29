# File > Settings... > Project:... > Project interpreter > + > beautifulsoup4 > Install Package
# 터미널 > pip install bs4
# File > Settings... > Project:... > Project interpreter > + > lxml > Install Package
# 터미널 > pip install lxml

from bs4 import BeautifulSoup           #html 구조적으로 변환하자  alt+shift+enter
from urllib.request import urlopen      #url에 해당하는 html 가져오자

if __name__ == '__main__':
    # # urlopen 하자
    # data = urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=703852&weekday=tue")
    #
    # # BeautifulSoup 객체 생성하자
    # soup = BeautifulSoup(data, "lxml")
    # # print(soup)
    #
    # data.close()

    with urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=703852&weekday=tue") as data:
        soup = BeautifulSoup(data, "lxml")

    # 원하는 태그나 속성으로 찾자
    cartoon_titles = soup.find_all("td", attrs={"class": "title"})
    # print(cartoon_titles)
    for title in cartoon_titles[:]:
        t = title.find("a").text
        link = title.find("a").get("href")
        link = "https://comic.naver.com/" + link
        print(t)
        print(link)

    # 정보 가져오자
