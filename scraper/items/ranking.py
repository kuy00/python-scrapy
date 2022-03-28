import scrapy


class Ranking(scrapy.Item):
    brand = scrapy.Field()
    name = scrapy.Field()
