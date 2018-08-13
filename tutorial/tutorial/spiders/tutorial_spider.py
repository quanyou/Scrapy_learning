import scrapy

class tutorialSpider(scrapy.Spider):

    name = "toutiao"
    allowed_domains = ["toutiao.com"]
    start_urls = [
        "https://www.toutiao.com/a6588436119296147981/",
        "https://www.toutiao.com/a6588903898507903492/"
    ]

    def parse(self, response):

        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)