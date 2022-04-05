from .base import Base
from orator.orm import has_one
from .product import Product


class Category(Base):
    __table__ = 'category'
    __guarded__ = []
    __timestamps__ = False

    @has_one
    def product(self):
        return Product
