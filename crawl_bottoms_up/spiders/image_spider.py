import scrapy
import json


class ImageSpider(scrapy.Spider):

    name = 'image_crawler'

    def start_requests(self):
        urls = [
            "https://unsplash.com/s/photos/dogs"
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):

        res = response.css("img::attr(src)").extract()

        # collector is the directory name should be available in root dir of the project

        with open('collector/out.json', 'wb') as f:
            f.write((json.dumps(res).encode()))
        # print(json.dumps(res))
