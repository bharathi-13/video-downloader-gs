import requests
from bs4 import BeautifulSoup as bs
import wget


""" https://www1.gogoanime.ai//search.html?keyword=bleach """


class anime:
    search_url_list = (
        "https://www1.gogoanime.ai//search.html?keyword=",
        "https://www.kissanime.com.ru/Search/?s=",
    )

    kissanime_class_ele = (
        "item_movies_in_cat item_movies_in_cat_thumb", 
        "item_movies_in_cat item_movies_in_cat_thumb odd"
    )
    gogo_main_url = 'https://www1.gogoanime.ai/'


    def __init__(
        self,
        anime_name="none",
        url="none",
        _id="none",
        website="gogoanime",
        quality=None,
    ):
        self.url = url
        self._id = _id
        self.website = website
        self.anime_name = anime_name
        self.quality = quality

    def search_anime_scr(self, search_url):
        search_resulr_scr = requests.get(search_url).text
        self.soup = bs(search_resulr_scr, "lxml")

    def search_anime(self):
        try:
            if self.website == "gogoanime":
                search_url = self.search_url_list[0] + self.anime_name
                self.search_anime_scr(search_url=search_url)

                anime_scr = self.soup.find('ul', class_='items')

                for anime_name_scr in anime_scr.find_all('li'):

                    self.anime_name = str(anime_name_scr.find('p', class_='name').text)
                    anime_release = str(anime_name_scr.find('p', class_='released').text).strip('\n')
                    self.anime_release = anime_release.strip(' ')

                    anime_link_scr = str(anime_name_scr.find('a'))
                    part_of_the_link = anime_link_scr.split('"')[1]
                    self.anime_link = self.gogo_main_url+part_of_the_link

                    print(self.anime_name+'____   '+self.anime_release+' - '+self.anime_link,'\n')

            if self.website == "kissanime":
                search_url = self.search_url_list[1] + self.anime_name
                self.search_anime_scr(search_url=search_url)


                for anime_list_scr in self.soup.find_all("div", class_=self.kissanime_class_ele):

                    self.anime_name_link = anime_list_scr.find('div', class_='title_in_cat_container')
                    self.anime_name = str(self.anime_name_link.text).strip('\n')

                    self.anime_link_scr = str(self.anime_name_link.a).split('"')
                    self.anime_link = self.anime_link_scr[-2]

                    self.anime_status = str(anime_list_scr.find('div', class_='status_in_cat_container').text).strip('\n')


                    print(self.anime_name+'____   '+self.anime_status+' - '+self.anime_link,'\n')

        except:
            print(
                "There is some problem with the website Domine. Please check and update the Domine..."
            )


    def list_all_ep(self, ep_link='none'):

        self.ep_link_main = ep_link

        url = requests.get(self.ep_link_main).text
        soup = bs(url, 'lxml')

        if self.website == 'kissanime':

            for ep_list_all in soup.find_all('div', class_="listing listing8515 full"):

                for self.ep_list_scr in ep_list_all.find_all('h3'):
                
                    self.ep_name =  str(self.ep_list_scr.text).strip('\n')

                    ep_link_scr  = str(self.ep_list_scr).split('"')
                    self.ep_link = ep_link_scr[3]

                    ep_id_scr = self.ep_link.split('=')
                    self.ep_id = ep_id_scr[-1]

                    print(self.ep_name+'___'+self.ep_link+'  -  '+self.ep_id,'\n')
            

if __name__ == "__main__":
    bleach = anime("bleach", website="gogoanime")

    # bleach.list_all_ep(ep_link='https://kissanime.com.ru/Anime/fullmetal-alchemist-dub.25384/')

    bleach.search_anime()
