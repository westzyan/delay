# -*- coding: utf-8 -*-
import scrapy
from Delay.items import DelayItem
import re

class DealySpider(scrapy.Spider):
    name = 'delay'
    allowed_domains = ['torstatus.blutmagie.de']
    start_urls = ['http://torstatus.blutmagie.de']
    i = 0
    def parse(self, response):
        PATTERN_URLS = "FP=(.*?)'"
        pattern_urls = re.compile(PATTERN_URLS)
        print(response.text)
        for partUrl in pattern_urls.findall(response.text):
            yield scrapy.Request('http://torstatus.blutmagie.de/router_detail.php?FP='+partUrl, callback=self.parseUrl)

    def parseUrl(self, response):
        item = DelayItem()
        delayInfo = response.xpath("//td[@class='TRSB']/text()").extract()
        print(delayInfo)
        item['routerName'] = delayInfo[0]
        item['fingerprint'] = delayInfo[1]
        item['contact'] = delayInfo[2]
        item['ip'] = delayInfo[3]
        item['onionRouterPort'] = delayInfo[5]
        item['directoryServerPort'] = delayInfo[6]
        item['countryCode'] = delayInfo[7]
        item['platform'] = delayInfo[8]
        yield item

