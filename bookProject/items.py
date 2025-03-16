import scrapy
from itemloaders.processors import TakeFirst, MapCompose, Join
import re

def clean_price(value):
    """Elimina el símbolo de moneda y convierte el precio a float"""
    value = re.sub(r"[^\d.]", "", value)  # Elimina todo excepto números y punto decimal
    try:
        return float(value)  # Convierte a número decimal
    except ValueError:
        return 0.0  # Si no se puede convertir, devuelve 0.0

def clean_stock(value):
    """Convierte la disponibilidad en 'Sí' o 'No'"""
    value = value.strip()  # Elimina espacios y saltos de línea
    return "Sí" if "In stock" in value else "No"

def clean_stars(value):
    """Convierte la clase de rating en número de estrellas"""
    stars_mapping = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    for key in stars_mapping:
        if key in value:
            return stars_mapping[key]
    return 0  # Si no se encuentra, devuelve 0

class BookItem(scrapy.Item):
    title = scrapy.Field(
        output_processor=TakeFirst()  # Toma solo el primer valor
    )
    price = scrapy.Field(
        input_processor=MapCompose(clean_price),  # Aplica la función de limpieza
        output_processor=TakeFirst()
    )
    stock = scrapy.Field(
        input_processor=MapCompose(str.strip, clean_stock),  # Limpia espacios y convierte a Sí/No
        output_processor=TakeFirst()
    )
    stars = scrapy.Field(
        input_processor=MapCompose(clean_stars),  # Convierte la clase a número de estrellas
        output_processor=TakeFirst()
    )
    category = scrapy.Field(
        output_processor=TakeFirst()  # Toma el nombre de la categoría sin modificarlo
    )
