from pymongo import MongoClient
from datetime import datetime
from itemadapter import ItemAdapter


class MongoPipeline:
    def __init__(self, **db):
        self.mongo_uri = db['mongo_uri']
        self.mongo_db = db['mongo_db']
        self.client = object
        self.db = object

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        spider_name = getattr(spider, 'name')
        collection_name = f'{spider_name}_{datetime.now().strftime("%y%m%d")}'
        category = ItemAdapter(item['category']).asdict()
        product = ItemAdapter(item['product']).asdict()

        self.db[collection_name].insert_one({
            'category': category,
            'product': product,
        })
        return item

    def close_spider(self, spider):
        self.client.close()
