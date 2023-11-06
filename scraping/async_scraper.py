import httpx
from parsel import Selector
import asyncio


class AsyncScraper:
    Headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
    }
    URL = 'https://www.scientificamerican.com/technology/?page={page}&source='
    LINK_E = '//div[@class="grid__col large-up-1 medium-1-2"]/article[@class="listing-wide"]/a/@href'
    PLUS_E = 'https://www.scientificamerican.com'

    async def async_generator(self, limit):
        for page in range(1, limit + 1):
            yield page

    async def get_url(self, client, url):
        response = await client.get(url)
        return response.text

    async def scrape_links(self, html):
        tree = Selector(text=html)
        links = tree.xpath(self.LINK_E).extract()
        return links

    async def parse_pages(self):
        links = []
        async with httpx.AsyncClient(headers=self.Headers) as client:
            async for page in self.async_generator(limit=2):
                html = await self.get_url(
                    client=client,
                    url=self.URL.format(page=page)
                )
                page_links = await self.scrape_links(html)
                links.extend(page_links)
        return links[:5]


if __name__ == "__main__":
    scraper = AsyncScraper()
    links = asyncio.run(scraper.parse_pages())
    for link in links:
        print(link)