from .base import Base


class Product(Base):
    __table__ = 'products'
    __guarded__ = []
    __timestamps__ = False
