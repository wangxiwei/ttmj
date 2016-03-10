# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ttmeijvItem(scrapy.Item):
    num = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    status = scrapy.Field()
    update_date = scrapy.Field()
    return_date = scrapy.Field()
    pass
