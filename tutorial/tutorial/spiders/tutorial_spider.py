import scrapy


class tutorialSpider(scrapy.Spider):

    name = "toutiao"
    allowed_domains = ["toutiao.com"]
    start_urls = [
        "https://www.toutiao.com/a6588436119296147981/",
        "https://www.toutiao.com/a6588903898507903492/"
    ]

    def parse(self, response):

        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)

        for sel in response.xpath('//ul/li'):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('text()').extract()
            print(title, link, desc)