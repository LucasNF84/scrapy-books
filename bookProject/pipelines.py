import json
import scrapy.exceptions

class JsonWriterPipeline:
    def open_spider(self, spider):
        """Abre el archivo JSON al iniciar el Spider"""
        self.file = open('libros_output.json', 'w', encoding="utf-8")
        self.file.write("[")
        self.first_item = True

    def close_spider(self, spider):
        """Cierra el archivo JSON al finalizar el Spider"""
        self.file.write("]")
        self.file.close()

    def process_item(self, item, spider):
        """Procesa cada item, valida y lo guarda en el JSON"""

        # Verificación: Si falta el título, descarta el ítem
        if not item.get("title"):
            raise scrapy.exceptions.DropItem(f"Faltan datos en el ítem: {item}")
        # 🚨 Depuración: Ver si el precio llega limpio al pipeline
        print(f"Precio recibido en pipeline: {item['price']}")

        # Si el precio no es válido, poner 0 en vez de descartarlo
        if item.get("price") is None:
            item["price"] = 0  # Asigna 0 en lugar de descartar

        # Si el stock está vacío, poner "Desconocido"
        if not item.get("stock"):
            item["stock"] = "Desconocido"

        # Guarda el ítem en JSON
        if not self.first_item:
            self.file.write(",\n")  # Agrega una coma entre elementos
        self.first_item = False

        line = json.dumps(dict(item), ensure_ascii=False, indent=4)
        self.file.write(line)

        return item  # Retorna el ítem para que Scrapy continúe procesando
