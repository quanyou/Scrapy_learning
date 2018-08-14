import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor


# class tutorialSpider(scrapy.Spider):
#
#     name = "toutiao"
#     allowed_domains = ["toutiao.com"]
#     start_urls = [
#         "https://www.toutiao.com/a6588436119296147981/",
#         "https://www.toutiao.com/a6588903898507903492/"
#     ]
#
#     def parse(self, response):
#
#         # filename = response.url.split("/")[-2]
#         # with open(filename, 'wb') as f:
#         #     f.write(response.body)
#
#         for sel in response.xpath('//ul/li'):
#             title = sel.xpath('a/text()').extract()
#             link = sel.xpath('a/@href').extract()
#             desc = sel.xpath('text()').extract()
#             print(title, link, desc)



class MySpider(CrawlSpider):

    name = 'example.com'
    allowed_demains = ['example.com']
    start_urls = ['http://www.example.com']

    rules = (

        # 提取匹配 ‘category.php’ （但不匹配‘subsection.php’）的链接并跟进链接（没有callback意味着follow默认为True）
        Rule(LinkExtractor(allow=('category\.php', ), deny=('subsection\.php', ))),

        # 提取匹配‘item.php’ 的链接并使用spider的parse_item方法进行分析
        Rule(LinkExtractor(allow=('item\.php', )), callback='parse_item'),
    )