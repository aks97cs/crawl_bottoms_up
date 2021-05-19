import scrapy


class ImageSpider(scrapy.Spider):

    name = 'image crawler'

    def start_requests(self):
        pass

    def parse(self, response, **kwargs):
        pass
