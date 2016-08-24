# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule 
from ProxyPool.items  import ProxypoolItem


class ProxyspiderSpider(CrawlSpider):
    name = 'proxyspider'
    allowed_domains = ['kuaidaili.com']
    start_urls = [
        'http://www.kuaidaili.com/free/outha/1/',
        'http://www.kuaidaili.com/free/inha/1/',
    ]

    rules = (
        Rule(LinkExtractor(allow=r'/free/(out|in)ha/[1-9]/$'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = ProxypoolItem() 
        i['ip'] = response.xpath('//td[@data-title="IP"]/text()').extract()
        i['port'] = response.xpath('//td[@data-title="PORT"]/text()').extract()
        i['protocol'] = response.xpath('//td[@data-title="类型"]/text()').extract()
        i['location'] = response.xpath('//td[@data-title="位置"]/text()').extract()

#        from scrapy.shell import inspect_response
#        inspect_response(response,self)

        return i
