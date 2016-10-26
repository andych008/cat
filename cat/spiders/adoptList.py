# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor

from scrapy.spiders import CrawlSpider, Rule


class AdoptlistSpider(CrawlSpider):
    name = 'adoptList'
    allowed_domains = ['www.maomilingyang.com']
    start_urls = ['http://www.maomilingyang.com/AdoptList.asp?Page=0']

    rules = (
        Rule(LinkExtractor(allow=r'/AdoptList\.asp\?'),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # filename = response.url.split("/")[-1]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        print(response.url.split("/")[-1])

        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
