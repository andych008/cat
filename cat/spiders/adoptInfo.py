# -*- coding: utf-8 -*-
import scrapy

from cat.items import AdoptItem


class AdoptinfoSpider(scrapy.Spider):
    name = 'adoptInfo'
    # allowed_domains = ['www.maomilingyang.com']
    # start_urls = ['http://www.maomilingyang.com/AdoptList.asp']
    
    allowed_domains = ['127.0.0.1:9000']
    start_urls = ['http://127.0.0.1:9000/static/AdoptList.html']

    def parse(self, response):

        item = AdoptItem()

        datas = response.css('p.ind_tit a::attr(alt)')
        # print(datas.re('^【.*领养】'))

        item['address'] = [i[1:i.rindex('领养】')] for i in datas.re('^【.*领养】')]
        # item['address'] = [i.replace('【','').replace('领养】','') for i in datas.re('^【.*领养】')]
        item['desc'] = datas.extract()
        item['href'] = response.css('p.ind_tit a::attr(href)').extract()
        print(item)
