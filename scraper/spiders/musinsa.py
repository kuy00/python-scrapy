import scrapy
from scraper.Items import *


class MusinsaSpider(scrapy.Spider):
    name = 'musinsa'
    allowed_domains = ['www.musinsa.com']
    start_urls = [
        'https://www.musinsa.com/ranking/best',
    ]
    categories = {
        '001': '상의',
        '002': '아우터',
        '020': '원피스',
        '022': '스커트',
    }

    def start_requests(self):
        for url in self.start_urls:
            for key, value in self.categories.items():
                yield scrapy.Request(
                    url + f'?mainCategory={key}',
                    callback=self.parse,
                    cb_kwargs={
                       'item': {
                           'code': key,
                           'name': value,
                       }
                    },
                )

    def parse(self, response, item):
        print(f'parse url: {response.url}')

        items = response.xpath('//form[@id="goodsRankForm"]//li[@class="li_box"]')
        for key, value in enumerate(items):
            product_code = value.xpath('./@data-goods-no').get()
            price_node = value.xpath('.//p[@class="price"]/text()')
            if len(price_node) > 1:
                price = price_node[-1].get().strip()
            else:
                price = price_node.get().strip()

            category_item = category.Category(**item)
            product_item = product.Product(
                brand=value.xpath('.//p[@class="item_title"]/a/text()').get(),
                name=value.xpath('.//p[@class="list_info"]/a/@title').get(),
                image=value.xpath('.//div[@class="list_img"]/a/img/@src').get(),
                product_page_url=f'https://store.musinsa.com/app/goods/{product_code}',
                price=price,
                rank=key+1,
            )

            yield {
                'category': category_item,
                'product': product_item,
            }
