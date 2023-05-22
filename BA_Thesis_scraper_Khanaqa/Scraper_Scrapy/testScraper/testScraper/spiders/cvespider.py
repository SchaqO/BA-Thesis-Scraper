import scrapy
from testScraper.items import CveResultItem

class CVESpider(scrapy.Spider):
    name = 'cvespider'
    allowed_domains = ['cvedetails.com.com']
    start_urls = ['https://www.cvedetails.com/google-search-results.php?q=google+assistant'] #new code

    custom_settings = {
        'FEEDS': {
            'data/cve.csv': {
                'format': 'csv',
                'overwrite': True,
            }
        }
    }

    ''' 
    def start_requests(self):
        query = getattr(self, 'query', '')  # Default query is an empty string
        start_url = f'https://www.cvedetails.com/google-search-results.php?q={query}'
        yield scrapy.Request(start_url, self.parse)
    '''

    def parse(self, response):
        # Extract information from the response here
        search_results = response.css('div.gsc-webResult.gsc-result')
        
        # Process the extracted data as needed
        # Example:
        for result in search_results:
            item = CveResultItem()
            item['title'] = result.css('div.gs-title a.gs-title::text').get()
            item['url'] = result.css('div.gs-bidi-start-align.gs-visibleUrl-long span.gs-visibleUrl-long::text').get()
            item['description'] = result.css('div.gs-bidi-start-align.gs-snippet span.gs-snippet::text').get()
            yield item
            print(item + "test")
        
        
        # Follow links to next pages if available
        next_page_url = response.css('div.gsc-cursor-page.gsc-cursor-current-page + div.gsc-cursor-page a::attr(href)').get()
        if next_page_url:
            yield response.follow(next_page_url, callback=self.parse)

            