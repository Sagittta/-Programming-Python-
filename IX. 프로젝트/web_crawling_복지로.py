from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    url = "http://bokjiro.go.kr/welInfo/retrieveWelInfoBoxList.do"
    data = {"searchIntClId": "03", "pageUnit": "100"}
    with requests.get(url, data) as response:
        soup = BeautifulSoup(response.text, "lxml")
    # print(soup)

    # dts = soup.find_all("dt", attrs={"class": "tit"})
    # for dt in dts:
    #     title = dt.find("a")
    #     print(title.text)
    titles = soup.select("dt.tit > a")      # <dt class="tit"><a> text </a></dt>
    cnt = 1
    for title in titles:
        print(cnt, title.text)
        cnt += 1
