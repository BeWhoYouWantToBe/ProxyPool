# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule 
from ProxyPool.items  import ProxypoolItem


class ProxyspiderSpider(CrawlSpider):
    name = 'proxyspider'
    allowed_domains = ['mimiip.com']
    start_urls = [
        'http://www.mimiip.com/gngao/'
    ]

    rules = (
        Rule(LinkExtractor(allow=r'/gngao/[0-9]+$'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = ProxypoolItem() 
        i['ip'] = response.xpath('//tr/td[1]/text()').extract()
        i['port'] = response.xpath('//tr/td[2]/text()').extract()
        i['protocol'] = response.xpath('//tr/td[5]/text()').extract()
        i['location'] = response.xpath('//tr/td[3]/a[1]/text()').extract()

#        from scrapy.shell import inspect_response
#        inspect_response(response,self)

        return i
