import scrapy
from ..items.ranking import Ranking


class MusinsaSpider(scrapy.Spider):
    name = 'musinsa'
    allowed_domains = ['www.musinsa.com']
    start_urls = [
        'https://www.musinsa.com/ranking/best',
        'https://www.musinsa.com/ranking/brand',
    ]
    category = ('004',)

    def start_requests(self):
        for url in self.start_urls:
            for code in self.category:
                print(code)
                yield scrapy.Request(url + f'?mainCategory={code}', callback=self.parse)

    def parse(self, response):
        print('test {}'.format(response.url))
        print(len(response.xpath('//form[@id="goodsRankForm"]//li[@class="li_box"]')))

        items = response.xpath('//form[@id="goodsRankForm"]//li[@class="li_box"]')
        for item in items:
            ranking = Ranking()
            ranking['brand'] = item.xpath('.//p[@class="item_title"]/a/text()').get()
            ranking['name'] = item.xpath('.//p[@class="list_info"]/a/@title').get()
            yield ranking
