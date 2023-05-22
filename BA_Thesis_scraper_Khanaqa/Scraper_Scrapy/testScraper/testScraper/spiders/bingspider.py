import scrapy
from testScraper.items import BingResultItem

class BingSpider(scrapy.Spider):
    name = 'bingspider'
    allowed_domains = ['bing.com']

    custom_settings = {
        'FEEDS': {
            'data/bing.csv': {
                'format': 'csv',
                'overwrite': True,
            }
        }
    }

    def start_requests(self):
        query = getattr(self, 'query', 'alexa')  # Default query is "alexa"
        start_url = f'https://www.bing.com/search?q={query}'
        yield scrapy.Request(start_url, self.parse)

    def parse(self, response):
        results = response.css('.b_algo')

        for result in results:
            item = BingResultItem()
            item['title'] = result.css('h2 a::text').get()
            item['url'] = result.css('h2 a::attr(href)').get()
            yield item

        next_page = response.css('.sb_pagN::attr(href)').get()

        if next_page:
            yield response.follow(next_page, callback=self.parse)