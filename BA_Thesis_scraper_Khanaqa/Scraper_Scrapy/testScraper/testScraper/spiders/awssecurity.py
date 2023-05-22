import scrapy


class AwssecuritySpider(scrapy.Spider):
    name = "awssecurity"
    start_urls = ['https://aws.amazon.com/security/security-bulletins/?card-body.sort-by=item.additionalFields.bulletinId&card-body.sort-order=desc&awsf.bulletins-flag=*all&awsf.bulletins-year=*all']

    custom_settings = {
        'FEEDS': {
            'data/awssecurity.csv': {
                'format': 'csv',
                'overwrite': True,
            }
        }
    }

    def parse(self, response):
        bulletins = response.css('.lb-content-item')

        for bulletin in bulletins:
            title = bulletin.css('h4 a::text').get()
            date = bulletin.css('.aws-bulletin-meta-date::text').get()
            description = bulletin.css('.aws-bulletin-desc::text').get()

            yield {
                'title': title.strip(),
                'date': date.strip(),
                'description': description.strip()
            }