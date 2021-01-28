import scrapy


class BookspiderSpider(scrapy.Spider):
    name = 'bookspider'

    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        for book in response.css('ol.row li article.product_pod'):
            yield {
                'title': book.css('h3 a::attr(title)').get(),
                'price': book.css('div.product_price p::text').get(),
                'rating': book.css('p::attr(class)').re_first('star-rating (.*)'),
                'link': "https://books.toscrape.com/" + book.css('div.image_container a::attr(href)').get()

            }
        next_page = response.css("div ul.pager li.next a::attr(href)").get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
