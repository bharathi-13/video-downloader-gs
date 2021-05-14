import requests
from bs4 import BeautifulSoup as bs
import wget


""" https://www1.gogoanime.ai//search.html?keyword=bleach """

class anime:
    search_url_list = (
            'https://www1.gogoanime.ai//search.html?keyword=',
            'https://www.kissanime.com.ru/Search/?s='
    )

    def __init__(self, anime_name='none', url='none', _id='none', website='gogoanime', quality = None):
        self.url = url
        self._id = _id
        self.website = website
        self.anime_name = anime_name
        self.quality = quality
    

    def search_anime(self,):
        try:
            if self.website == 'gogoanime':
                search_url = self.search_url_list[0]+self.anime_name
                search_resulr_scr = requests.get(search_url).text
                self.soup = bs(search_resulr_scr, 'lxml')
                print(self.soup.prettify())

            if self.website == 'kissanime':
                search_url = self.search_url_list[1]+self.anime_name
                search_resulr_scr = requests.get(search_url).text
                self.soup = bs(search_resulr_scr, 'lxml')
                print(self.soup.prettify())
            else:
                print('please provide the website to do the search...')
        
        except:
            print('There is some problem with the website Domine. Please check and update the Domine...')



bleach = anime('bleach')

bleach.search_anime()
# print(bleach.website)




