from urllib.request import urlopen
from bs4 import BeautifulSoup

if __name__ == '__main__':
    with urlopen("https://movie.daum.net/boxoffice/yearly") as response:
        soup = BeautifulSoup(response, "lxml")

    # print(soup)
    movie_titles = soup.find_all("a", attrs={"class": "link_g"})
    n = 1
    print("Daum Movie Box Office")
    for movie_title in movie_titles[2:]:
        print(n, movie_title.text)
        n += 1

    with urlopen("https://search.naver.com/search.naver?where=nexearch&query=%eb%b0%95%ec%8a%a4%ec%98%a4%ed%94%bc%ec%8a%a4%ec%88%9c%ec%9c%84") as response:
        soup = BeautifulSoup(response, "lxml")

    # print(soup)
    movie_titles_naver = soup.find_all("strong", attrs={"class": "_text"})
    n = 1
    print("Naver Movie Box Office")
    for movie_title_naver in movie_titles_naver[:10]:
        print(n, movie_title_naver.text)
        n += 1
