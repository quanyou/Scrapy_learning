# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

# create a Scrapy project by order code : scrapy startproject tutorial

# Item 是保存爬到的数据的容器； 编辑tutorial目录中的items.py文件

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()

