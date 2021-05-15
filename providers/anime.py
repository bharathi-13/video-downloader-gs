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

        self.ep_link = ep_link

        url = requests.get(self.ep_link).text
        soup = bs(url, 'lxml')

        ep_list_scr = soup.find('div', class_="listing listing8515 full").h3
        
        ep_name =  str(ep_list_scr.text).strip('\n')

        ep_link_scr  = str(ep_list_scr).split('"')
        ep_link = ep_link_scr[3]

        ep_id_scr = ep_link[3].split('id')


        
        print(ep_id_scr)

        

if __name__ == "__main__":
    bleach = anime("full metal", website="kissanime")

    bleach.list_all_ep(ep_link='https://kissanime.com.ru/Anime/fullmetal-alchemist-dub.25384/')

    # anime.list_all_ep(ep_link='https://kissanime.com.ru/Anime/fullmetal-alchemist-dub.25384/')
