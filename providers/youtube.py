import requests
from bs4 import BeautifulSoup as bs 


class youtube:
    def __init__(self, url):
        self.url = url

    def source_code (self):
        url = requests.get(self.url)
        source = url.content
        source_code = bs(source, 'lxml')
        print(source_code.prettify())



video = youtube('https://www.youtube.com/watch?v=pLHt1hMVsDQ')

print(video.source_code())
