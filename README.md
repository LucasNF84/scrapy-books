# 📚 Scrapy Books Extraction

Este proyecto utiliza **Scrapy** para extraer información de libros desde [books.toscrape.com](https://books.toscrape.com). 
El scraper recorre todas las categorías de libros, extrae información relevante, la transforma y la almacena en una base de datos **PostgreSQL**.

---

## 🚀 Tecnologías utilizadas
- **Python** 🐍
- **Scrapy** (framework de web scraping)
- **PostgreSQL** (base de datos relacional)
- **Docker** (para ejecutar PostgreSQL en un contenedor)
- **dotenv** (manejo de variables de entorno)

---

## 📌 Flujo del scraper
El proceso consta de **tres fases principales**: **extracción, transformación y almacenamiento**.

### **1️⃣ Extracción de datos**
- Scrapy accede a la página principal de `books.toscrape.com`.
- Extrae todas las **categorías** de libros desde la barra lateral izquierda.
- Para cada categoría, navega por todas las páginas de la misma y extrae información de cada libro.

### **2️⃣ Transformación de datos**
Para cada libro, se procesan los siguientes campos:

| **Campo**   | **Descripción**   | **Transformación aplicada** |
|------------|------------------|----------------------------|
| `title`    | Nombre del libro  | Se extrae directamente del HTML. |
| `price`    | Precio del libro  | Se elimina el símbolo `£` y se convierte a `float`. |
| `stock`    | Disponibilidad    | Se convierte en `"Sí"` si está en stock, `"No"` si no. |
| `stars`    | Calificación      | Se transforma de `star-rating Five` a `5` (número de estrellas). |
| `category` | Categoría del libro | Se extrae desde la URL de la categoría. |

### **3️⃣ Almacenamiento de los datos**
Los datos extraídos y transformados se guardan en una base de datos **PostgreSQL** en la tabla `books`.

---

## ⚙ Instalación y configuración

### 🔹 **1. Clonar el repositorio**
```bash
git clone https://github.com/LucasNF84/scrapy-books.git
cd scrapy-books/bookProject
```

### 🔹 **2. Crear y activar un entorno virtual**
```bash
python -m venv venv
source venv/bin/activate  # Para macOS/Linux
venv\Scripts\activate  # Para Windows
```

### 🔹 **3. Configurar PostgreSQL con Docker**
Si no tienes PostgreSQL instalado, puedes ejecutarlo en **Docker** con:
```bash
docker run --name postgres-scrapy -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=tu_contraseña -e POSTGRES_DB=booksdb -p 5432:5432 -d postgres
```

### 🔹 **4. Crear la tabla en PostgreSQL**
Si PostgreSQL está instalado localmente, crea la base de datos manualmente:
```sql
CREATE DATABASE booksdb;

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title TEXT,
    price NUMERIC,
    stock TEXT,
    stars INTEGER,
    category TEXT
);
```

### 🔹 **5. Configurar variables de entorno (`.env`)**
Crea un archivo `.env` en el directorio principal del proyecto y agrega los siguientes datos:
```ini
POSTGRES_HOST=localhost
POSTGRES_DB=booksdb
POSTGRES_USER=postgres
POSTGRES_PASSWORD=tu_contraseña
POSTGRES_PORT=5432
```
Para cargar estas variables en `settings.py`, instala **python-dotenv**:
```bash
pip install python-dotenv
```
Y agrega esto en `settings.py`:
```python
from dotenv import load_dotenv
import os

load_dotenv()

POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", 5432))
```

### 🔹 **6. Instalar dependencias**
Ejecuta el siguiente comando para instalar todas las librerías necesarias:
```bash
pip install -r requirements.txt
```
Asegúrate de que el archivo `requirements.txt` incluya:
```
scrapy
psycopg2
python-dotenv
```

### 🔹 **7. Ejecutar el scraper**
Ejecuta el siguiente comando para iniciar el scraping y almacenar los datos en PostgreSQL:
```bash
scrapy crawl books
```

### 🔹 **8. Verificar los datos en PostgreSQL**
Conéctate a la base de datos y verifica que los datos fueron insertados correctamente:
```sql
SELECT * FROM books;
```

---

## 📊 Resumen de cambios recientes
✔ Ahora los datos se almacenan en **PostgreSQL** en lugar de un archivo JSON.  
✔ Se agregó el uso de **.env** para manejar configuraciones sensibles.  
✔ Se creó una tabla `books` en PostgreSQL con los campos extraídos del scraping.  
✔ Se mejoró el procesamiento de datos usando **ItemLoaders** en Scrapy.  
✔ Se agregó configuración para ejecutar PostgreSQL en **Docker**.  
✔ Se incluyó la instalación y configuración detallada del entorno de desarrollo.  

---

🎯 **Ahora Scrapy guarda la información de los libros en PostgreSQL de manera estructurada y eficiente.** 🚀