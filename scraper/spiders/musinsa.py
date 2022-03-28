import scrapy
from ..items import MusinsaItem


class MusinsaSpider(scrapy.Spider):
    name = 'musinsa'
    allowed_domains = ['www.musinsa.com']
    start_urls = [
        'https://www.musinsa.com/ranking/best',
        'https://www.musinsa.com/ranking/brand',
    ]
    category = ('001', '002', '003', '004', '005', '006', '007', '008', '009')

    def start_requests(self):
        for url in self.start_urls:
            print(url)
            for code in self.category:
                yield scrapy.Request(url + f'?mainCategory={code}', callback=self.parse)

    def parse(self, response):
        print('test {}'.format(response.url))
        print(len(response.xpath('//form[@id="goodsRankForm"]//li[@class="li_box"]')))

        items = response.xpath('//form[@id="goodsRankForm"]//li[@class="li_box"]')
        for item in items:
            musinsa_item = MusinsaItem()
            musinsa_item['name'] = item.xpath('.//p[@class="item_title"]/a/text()').get()

            yield musinsa_item
