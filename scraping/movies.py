from parsel import Selector
import requests


class movies:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'keep-alive'
    }
    URL = "https://rezka.ag/animation/"
    MOVIE_LINK_XPATH = '//div[@class="b-content__inline_item"]/@data-url'
    PLUS_URL = "https://rezka.ag/animation/"

    def parse_data(self):
        html = requests.get(url=self.URL, headers=self.headers).text
        tree = Selector(text=html)
        links = tree.xpath(self.MOVIE_LINK_XPATH).extract()
        for link in links:
            self.PLUS_URL + link

        return links[:5]


if __name__ == '__main__':
    scraper = movies()
    scraper.parse_data()
