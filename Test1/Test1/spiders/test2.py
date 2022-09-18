import scrapy


class Test2Spider(scrapy.Spider):
    name = 'test2'
    allowed_domains = ['domion.info']
    start_urls = ['http://domion.info/']

    def parse(self, response):
        pass
