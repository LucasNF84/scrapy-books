import os
import psycopg2
import scrapy.exceptions
from dotenv import load_dotenv

# 🔹 Cargar variables del entorno
load_dotenv()

class PostgresPipeline:
    def open_spider(self, spider):
        """Se ejecuta cuando el spider inicia: Conecta a PostgreSQL"""
        
        # 🚨 Imprimir configuración para depuración
        print("🔹 Intentando conectar a PostgreSQL con:")
        print("Host:", os.getenv("POSTGRES_HOST"))
        print("DB:", os.getenv("POSTGRES_DB"))
        print("User:", os.getenv("POSTGRES_USER"))
        print("Password:", os.getenv("POSTGRES_PASSWORD"))  # 🚨 Ver si está vacío
        print("Port:", os.getenv("POSTGRES_PORT"))

        try:
            self.conn = psycopg2.connect(
                host=os.getenv("POSTGRES_HOST"),
                database=os.getenv("POSTGRES_DB"),
                user=os.getenv("POSTGRES_USER"),
                password=os.getenv("POSTGRES_PASSWORD"),
                port=os.getenv("POSTGRES_PORT"),
            )
            self.cursor = self.conn.cursor()
        except Exception as e:
            print("❌ Error de conexión a PostgreSQL:", e)
            raise scrapy.exceptions.DropItem(f"No se pudo conectar a PostgreSQL: {e}")

    def process_item(self, item, spider):
        """Guarda el libro en la base de datos, actualiza si ya existe"""
        try:
            print(f"🔄 Procesando: {item}")  # 🚨 Ver qué datos se están insertando
            
            self.cursor.execute("""
                INSERT INTO books (title, price, stock, stars, category)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (title) DO UPDATE 
                SET price = EXCLUDED.price,
                    stock = EXCLUDED.stock,
                    stars = EXCLUDED.stars,
                    category = EXCLUDED.category
            """, (item["title"], item["price"], item["stock"], item["stars"], item["category"]))

            self.conn.commit()  # 🔹 IMPORTANTE: Confirmar la transacción después de cada inserción
            print(f"✅ Guardado/Actualizado: {item['title']}")

        except Exception as e:
            print(f"❌ Error al guardar {item['title']}: {e}")
            self.conn.rollback()  # 🚨 IMPORTANTE: Revertir la transacción en caso de error

        return item

    def close_spider(self, spider):
        """Cierra la conexión cuando el Spider termina"""
        self.cursor.close()
        self.conn.close()
