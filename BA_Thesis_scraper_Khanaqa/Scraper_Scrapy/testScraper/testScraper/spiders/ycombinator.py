import scrapy

class YcombinatorSpider(scrapy.Spider):
    name = "ycombinator"
    allowed_domains = ['news.ycombinator.com']
    start_urls = ['http://news.ycombinator.com/']

    custom_settings = {
        'FEEDS': {
            'data/ycombinator.csv': {
                'format': 'csv',
                'overwrite': True,
            }
        }
    }

    
    def parse(self, response):
        articles = response.css('tr.athing')
        for article in articles:
            yield {
                "URL": article.css(".titleline a::attr(href)").get(),
                "title": article.css(".titleline a::text").get(),
                "rank": article.css(".rank::text").get().replace(".", "")
        }


        next_page_url = response.css('.morelink::attr(href)').get()
        if next_page_url is not None:
            yield response.follow(next_page_url, callback=self.parse)