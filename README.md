# 📚 Scrapy Books Extraction

This project uses **Scrapy** to extract book information from [books.toscrape.com](https://books.toscrape.com). 
The scraper navigates through all book categories, extracts relevant information, transforms it, and stores it in a **PostgreSQL** database.

---

## 🚀 Technologies Used

- **Python** 🐍
- **Scrapy** (web scraping framework)
- **PostgreSQL** (relational database)
- **Docker** (to run PostgreSQL in a container)
- **dotenv** (environment variable management)

---

## 📌 Scraper Workflow

The process consists of **three main phases**: **extraction, transformation, and storage**.

### **1️⃣ Data Extraction**

- Scrapy accesses the main page of `books.toscrape.com`.
- Extracts all **book categories** from the left sidebar.
- For each category, it navigates through all pages and extracts information from each book.

### **2️⃣ Data Transformation**

For each book, the following fields are processed:

| **Field**   | **Description**      | **Applied Transformation**                           |
|------------|--------------------|-----------------------------------------------------|
| `title`    | Book title         | Extracted directly from HTML.                      |
| `price`    | Book price         | Removes the `£` symbol and converts it to `float`. |
| `stock`    | Availability       | Converts to `"Yes"` if in stock, `"No"` otherwise.  |
| `stars`    | Rating            | Converts from `star-rating Five` to `5` (star count). |
| `category` | Book category     | Extracted from the category URL.                   |

### **3️⃣ Data Storage**

Extracted and transformed data is stored in a **PostgreSQL** database in the `books` table.

---

## ⚙ Installation and Setup

### 🔹 **1. Clone the Repository**

```bash
git clone https://github.com/LucasNF84/scrapy-books.git
cd scrapy-books/bookProject
```

### 🔹 **2. Create and Activate a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows
```

### 🔹 **3. Set Up PostgreSQL with Docker**

If PostgreSQL is not installed, you can run it using **Docker**:

```bash
docker run --name postgres-scrapy -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=your_password -e POSTGRES_DB=booksdb -p 5432:5432 -d postgres
```

### 🔹 **4. Create the Table in PostgreSQL**

If PostgreSQL is installed locally, manually create the database:

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

### 🔹 **5. Set Up Environment Variables (`.env`)**

Create a `.env` file in the project's root directory and add the following details:

```ini
POSTGRES_HOST=localhost
POSTGRES_DB=booksdb
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
POSTGRES_PORT=5432
```

Install **python-dotenv** to load these variables:

```bash
pip install python-dotenv
```

### 🔹 **6. Install Dependencies**

Run the following command to install all required libraries:

```bash
pip install -r requirements.txt
```

Ensure that `requirements.txt` includes:

```
scrapy
psycopg2
python-dotenv
```

### 🔹 **7. Run the Scraper**

Run the following command to start the scraping process and store the data in PostgreSQL:

```bash
scrapy crawl books
```

### 🔹 **8. Verify Data in PostgreSQL**

Connect to the database and verify that the data was inserted correctly:

```sql
SELECT * FROM books;
```

---

## 📊 Recent Changes

✔ Data is now stored in **PostgreSQL** instead of a JSON file.  
✔ **.env** is used to manage sensitive configurations.  
✔ A `books` table was created in PostgreSQL to store extracted data.  
✔ Data processing was improved using **ItemLoaders** in Scrapy.  
✔ Configuration for running PostgreSQL in **Docker** was added.  
✔ Detailed installation and setup instructions were included.  

---

🎯 **Now, Scrapy efficiently extracts and stores book data in PostgreSQL.** 🚀

