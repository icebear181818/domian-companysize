# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class SearchItem(scrapy.Item):
    result=scrapy.Field()
    keyword = scrapy.Field()
    link=scrapy.Field()
    # siccode=scrapy.Field()
