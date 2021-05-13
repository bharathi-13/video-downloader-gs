import requests
from bs4 import BeautifulSoup as bs
import wget


class anime:
    def __init__(self, url, video_id, website):
        content = requests.get(url).text
        soup = bs(content, 'lxml')
        print(self.video_id)
    def pri(self):
        print(self.video_id)


