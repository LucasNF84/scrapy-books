from bookProject.items import BookItem  # Importamos BookItem
from scrapy.loader import ItemLoader
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
            loader = ItemLoader(item=BookItem(), selector=book)  # 🚀 Ahora usamos ItemLoader

            loader.add_css("title", "h3 a::attr(title)")
            loader.add_css("price", "p.price_color::text")  # 🚨 Se aplica `clean_price()`
            loader.add_css("stock", "p.availability::text")
            loader.add_css("stars", "p.star-rating::attr(class)")  # 🚨 Se aplica `clean_stars()`
            loader.add_value("category", category_name)  # Se agrega manualmente

            yield loader.load_item()  # 🚀 Scrapy aplicará `clean_price()` y `clean_stars()`
