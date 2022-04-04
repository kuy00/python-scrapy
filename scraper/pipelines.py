# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from models.modelImporter import ModelImporter
from database.config import db


class ScraperPipeline:
    def process_item(self, item, spider):
        if isinstance(item, dict):
            return self.process_multiple_item(item, spider)
        else:
            model_name = getattr(item, '__model__')
            model = ModelImporter.get_model(model_name)
            model.create(item.__dict__)
            return item

    def process_multiple_item(self, item, spider):
        parent_model = ''

        try:
            db.begin_transaction()

            for key in item:
                target_item = item[key]

                if parent_model != '':
                    parent_model.product().create(target_item.__dict__)
                else:
                    model_name = getattr(target_item, '__model__')
                    model = ModelImporter.get_model(model_name)
                    parent_model = model.create(target_item.__dict__)

            db.commit()
            return item
        except Exception as e:
            db.rollback()

