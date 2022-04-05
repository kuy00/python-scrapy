from dataclasses import dataclass


@dataclass
class Product:
    brand: str
    name: str
    image: str
    product_page_url: str
    price: str
    rank: int
