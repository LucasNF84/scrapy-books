from bookProject.items import BookItem
import scrapy

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        categories = response.css("div.side_categories ul li a::attr(href)").getall()
        for category_url in categories:
            full_category_url = response.urljoin(category_url)
            yield response.follow(full_category_url, callback=self.parse_category)

    def parse_category(self, response):
        category_name = response.css("div.page-header h1::text").get().strip()

        for book in response.css("article.product_pod"):
            stock_text = book.css("p.availability::text").get(default="").strip()
            stars_class = book.css("p.star-rating::attr(class)").get(default="")
            

            yield {
                "title": book.css("h3 a::attr(title)").get(),
                "price": book.css("p.price_color::text").get(),
                "stock": "Sí" if "In stock" in stock_text else "No",
                "stars": self.extract_stars(stars_class),  # Llamamos a la función de conversión de estrellas
                "category": category_name,
            }

    def extract_stars(self, stars_class):
        """Convierte la clase de estrellas en número"""
        stars_mapping = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
        for key in stars_mapping:
            if key in stars_class:
                return stars_mapping[key]
        return 0  # Si no se encuentra, devuelve 0