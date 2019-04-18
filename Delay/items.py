# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DelayItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    routerName = scrapy.Field()
    fingerprint = scrapy.Field()
    contact = scrapy.Field()
    ip = scrapy.Field()
    onionRouterPort = scrapy.Field()
    directoryServerPort = scrapy.Field()
    countryCode = scrapy.Field()
    platform = scrapy.Field()

    pass
