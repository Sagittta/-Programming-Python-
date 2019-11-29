# 다음웹툰 > 취향저격 그녀

from urllib.request import urlopen
import json

if __name__ == '__main__':
    with urlopen("http://webtoon.daum.net/data/pc/webtoon/view/favorite?timeStamp=1574736026313") as response:
        response_byte = response.read()
    response_json = json.loads(response_byte)
    # print(json.loads(response.read()))
    # print(response_json['data']['webtoon']['webtoonEpisodes'][11]['title'])  # data.webtoon.webtoonEpisodes[11].title
    cartoon_titles = response_json['data']['webtoon']['webtoonEpisodes']
    for item in cartoon_titles:
        title = item['title']
        print(title)
