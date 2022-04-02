# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from models.modelImporter import ModelImporter


class ScraperPipeline:
    def process_item(self, item, spider):
        model_name = getattr(item, '__model__')
        model = ModelImporter.get_model(model_name)
        model.create(item.__dict__)
        return item
