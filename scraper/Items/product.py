from dataclasses import dataclass


@dataclass
class Product:
    __model__ = 'Product'

    brand: str
    name: str

