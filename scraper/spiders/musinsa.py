import scrapy


class MusinsaSpider(scrapy.Spider):
    name = 'musinsa'
    allowed_domains = ['www.musinsa.com']
    start_urls = [
        'https://www.musinsa.com/ranking/brand',
        'https://www.musinsa.com/ranking/best',
        'https://www.musinsa.com/ranking/keyword',
    ]

    def __init__(self, category=None):
        self.category = category

    def start_requests(self):
        for url in self.start_urls:
            print(url)
            yield scrapy.Request(url + f'/mainCategory={self.category}', callback=self.parse)

    def parse(self, response):
        self.logger.info('test')
