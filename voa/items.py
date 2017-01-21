# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class VoaItem(scrapy.Item):
    vtitle = scrapy.Field();
    vlink = scrapy.Field();
    vdate = scrapy.Field();
    vtag = scrapy.Field();
    vcategory = scrapy.Field();
