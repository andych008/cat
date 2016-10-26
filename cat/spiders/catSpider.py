# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CatspiderSpider(CrawlSpider):
    name = 'catSpider'
    allowed_domains = ['www.maomilingyang.com']
    start_urls = ['http://www.maomilingyang.com/AdoptList.asp']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # i = {}
        # #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # #i['name'] = response.xpath('//div[@id="name"]').extract()
        # #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i

        item = CatItem()

        datas = response.css('p.ind_tit a::attr(alt)')
        item['address'] = datas.re('^【.*领养】')
        item['desc'] = datas.extract()

        return item
