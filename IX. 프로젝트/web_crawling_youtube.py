from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    # url = "https://www.youtube.com/channel/UC005BPECU5QAR2JVItQOswg/videos"
    url = "https://www.youtube.com/feed/trending"
    # response = requests.get(url)
    # post 방식으로 request
    response = requests.post(url)
    soup = BeautifulSoup(response.text, "lxml")
    # print(soup)
    # 주로 a 태그, 주로 class 로 찾으면 쉬움
    youtube_titles = soup.find_all("a", attrs={"class": "yt-uix-tile-link"})
    for youtube_title in youtube_titles:
        print(youtube_title.text)
        # 속성값 가져오는 방법
        # print(youtube_title.get("href"))
        print("https://www.youtube.com/" + youtube_title["href"])
