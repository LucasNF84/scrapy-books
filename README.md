# 📚 Scrapy Books Extraction

Este proyecto utiliza **Scrapy** para extraer información de libros desde [books.toscrape.com](https://books.toscrape.com). 
El scraper recorre todas las categorías de libros, extrae información relevante, la transforma y la almacena en un archivo JSON.

---

## 🚀 **Tecnologías utilizadas**
- **Python** 🐍
- **Scrapy** (framework de web scraping)
- **JSON** (almacenamiento de los datos)

---

## 📌 **Flujo del scraper**
El proceso consta de **tres fases principales**: **extracción, transformación y almacenamiento**.

### **1️⃣ Extracción de datos**
- Scrapy accede a la página principal de `books.toscrape.com`.
- Extrae todas las **categorías** de libros desde la barra lateral izquierda.
- Para cada categoría, navega por todas las páginas de la misma y extrae información de cada libro.

### **2️⃣ Transformación de datos**
Para cada libro, se procesan los siguientes campos:
| **Campo** | **Descripción** | **Transformación aplicada** |
|-----------|---------------|-----------------------------|
| `title` | Nombre del libro | Se extrae directamente del HTML. |
| `price` | Precio del libro | Se elimina el símbolo `£` y se convierte a `float`. |
| `stock` | Disponibilidad | Se convierte en `"Sí"` si está en stock, `"No"` si no. |
| `stars` | Calificación | Se transforma de `star-rating Five` a `5` (número de estrellas). |
| `category` | Categoría del libro | Se extrae desde la URL de la categoría. |

### **3️⃣ Almacenamiento de los datos**
Los datos extraídos y transformados se guardan en un archivo **JSON** llamado `libros_output.json`, en formato estructurado.

---

## ⚙ **Instalación y ejecución**
### 📌 **1. Clonar el repositorio**
```bash
git clone https://github.com/LucasNF84/scrapy-books.git
cd scrapy-books/bookProject
