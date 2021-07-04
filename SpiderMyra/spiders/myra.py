import scrapy


class MyraSpider(scrapy.Spider):
    name = 'myra'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        pass
