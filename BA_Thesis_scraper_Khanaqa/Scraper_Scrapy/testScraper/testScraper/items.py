# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TestscraperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass

def serialize_price(value):
    return f'$ {str(value)}'

class BookItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    upc = scrapy.Field()
    product_type = scrapy.Field()
    price_excl_tax = scrapy.Field() #serializer = serialize_price, use this instead of pipelines for small data
    price_incl_tax = scrapy.Field()
    tax = scrapy.Field()
    availability = scrapy.Field()
    num_reviews = scrapy.Field()
    stars = scrapy.Field()
    category = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()


class TweetItem(scrapy.Item):
    url = scrapy.Field()
    author = scrapy.Field()


class DuckDuckGoResultItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()


class BingResultItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()


class CveResultItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    description = scrapy.Field()

class YCombinatorNewsItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    rank = scrapy.Field()