# -*- coding: utf-8 -*-
import scrapy

from cat.items import AdoptItem


class AdoptinfoSpider(scrapy.Spider):
    name = 'adoptInfo'
    # allowed_domains = ['www.maomilingyang.com']
    # start_urls = ['http://www.maomilingyang.com/AdoptList.asp']

    allowed_domains = ['127.0.0.1:9000']
    start_urls = ['http://127.0.0.1:9000/static/AdoptList.html']

    def get_alt(self, response):
        data = response.css('::attr(alt)')
        text = data.re('^【.*领养】')[0]
        text2 = data.extract()[0]
        return (text[1:text.rindex('领养】')], text2[text2.rindex('_')+1:len(text2)-1])

    def parse(self, response):
        # print(type(response.css('p.ind_tit a::attr(alt)')))# SelectorList

        for data in response.css('p.ind_tit a'):

            item = AdoptItem()

            text = self.get_alt(data)

            item['address'] = text[0]
            item['name'] = text[1]
            item['href'] = data.css('::attr(href)').extract()[0]
            
            yield item

        # for data in response.css('p.ind_tit a::attr(href)'):

        #     item = AdoptItem()

        #     # item['address'] = [i[1:i.rindex('领养】')] for i in data.re('^【.*领养】')]
        #     text = data.re('^【.*领养】')[0]
        #     item['address'] = text[1:text.rindex('领养】')]
        #     item['desc'] = data.extract()
        #     #
