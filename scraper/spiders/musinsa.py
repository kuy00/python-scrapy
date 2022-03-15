import scrapy


class MusinsaSpider(scrapy.Spider):
    name = 'musinsa'
    allowed_domains = ['www.musinsa.com']
    start_urls = ['http://www.musinsa.com/']

    def parse(self, response):
        pass
