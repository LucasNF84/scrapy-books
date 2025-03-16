import scrapy
from itemloaders.processors import TakeFirst, MapCompose, Join
import re

def clean_price(price_str):
    """Elimina el símbolo £ y convierte el precio a float"""
    if price_str:
        print(f"Antes de limpiar: {price_str}")  # 🚨 Depuración: Ver qué llega antes de limpiar
        price_str = price_str.replace("£", "").strip()  # Elimina el símbolo de moneda
        try:
            clean_value = float(price_str)  # Convierte a número decimal
            print(f"Después de limpiar: {clean_value}")  # 🚨 Ver si realmente se limpia
            return clean_value
        except ValueError:
            return 0.0  # Si hay error, devuelve 0.0
    return 0.0  # Si el valor es None o vacío, devuelve 0.0

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
        input_processor=MapCompose(clean_price),  # Aplica la limpieza
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
