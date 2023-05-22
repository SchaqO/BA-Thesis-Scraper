import scrapy
from testScraper.items import DuckDuckGoResultItem


class DuckDuckGoSpider(scrapy.Spider):
    name = 'duckduckgospider'
    allowed_domains = ['duckduckgo.com']

    custom_settings = {
        'FEEDS': {
            'data/duckduckgo.csv': {
                'format': 'csv',
                'overwrite': True,
            }
        }
    }

    def start_requests(self):
        query = getattr(self, 'query', 'alexa')  # Default query is "alexa"
        start_url = f'https://duckduckgo.com/html/?q={query}'
        yield scrapy.Request(start_url, self.parse)

    def parse(self, response):
        results = response.css('.result')
        
        for result in results:
            item = DuckDuckGoResultItem()
            item['title'] = result.css('.result__title a::text').get()
            item['url'] = result.css('.result__url::text').get()
            yield item

        # Extract the URL of the next page of search results
        next_page = response.css('.nav-link.nextbtn::attr(href)').get()

        if next_page:
            yield response.follow(next_page, callback=self.parse)