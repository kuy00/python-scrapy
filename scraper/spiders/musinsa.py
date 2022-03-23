import scrapy
from ..items import MusinsaItem


class MusinsaSpider(scrapy.Spider):
    name = 'musinsa'
    allowed_domains = ['www.musinsa.com']
    start_urls = [
        'https://www.musinsa.com/ranking/best',
        'https://www.musinsa.com/ranking/brand',
    ]

    def __init__(self, category=None):
        self.category = category

    def start_requests(self):
        for url in self.start_urls:
            print(url)
            yield scrapy.Request(url + f'?mainCategory={self.category}', callback=self.parse)

    def parse(self, response):
        print('test {}'.format(response.url))
        print(len(response.xpath('//form[@id="goodsRankForm"]//li[@class="li_box"]')))

        items = response.xpath('//form[@id="goodsRankForm"]//li[@class="li_box"]')
        for item in items:
            musinsa_item = MusinsaItem()
            musinsa_item['name'] = item.xpath('.//p[@class="item_title"]/a/text()').get()

            yield musinsa_item
