# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule 
from ProxyPool.items import ProxypoolItem


class YundailiSpiderSpider(CrawlSpider):
    name = 'yundaili_spider'
    allowed_domains = ['yun-daili.com']
    start_urls = ['http://www.yun-daili.com/?stype=1']

    rules = (
        Rule(LinkExtractor(allow=r'stype=1&page=[0-9]+$'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = ProxypoolItem() 
        i['ip'] = response.xpath('//td[@class="style1"]/text()').extract()
        i['port'] = response.xpath('//td[@class="style2"]/text()').extract()
        i['protocol'] = response.xpath('//td[@class="style4"]/text()').extract()
        i['location'] = response.xpath('//td[@class="style5"]/text()').extract()
        return i
