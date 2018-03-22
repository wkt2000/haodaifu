# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WenmanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    hospital_phone = scrapy.Field()
    hospital_address = scrapy.Field()
    hospital_intro = scrapy.Field()
    hospital_level = scrapy.Field()
    hospital_name = scrapy.Field()
    hospital_type = scrapy.Field()

