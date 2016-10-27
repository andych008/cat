# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor

from scrapy.spiders import CrawlSpider, Rule


class AdoptlistSpider(CrawlSpider):
    name = 'adoptList'
    # allowed_domains = ['www.maomilingyang.com']
    # start_urls = ['http://www.maomilingyang.com/AdoptList.asp?Page=0']

    allowed_domains = []
    start_urls = ['http://127.0.0.1:9000/static/AdoptList.html']

    rules = (
        Rule(LinkExtractor(allow=r'/static/Adopt/.+\.html'),
             callback='parse_item', follow=True),
    )

    # rules = (
    #     Rule(LinkExtractor(allow=r'/AdoptList\.asp'),
    #          callback='parse_item', follow=False),
    # )

    def parse_item(self, response):
        print('*******************')
        # filename = response.url.split("/")[-1]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)

        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] =
        # response.xpath('//div[@id="description"]').extract()

        for data in response.css('p span'):
            print('-----------------')

            lst = data.css('::text').extract()
            # filter4lst = filter(lambda x: x.strip() != '', lst)
            lst = [x for x in lst if x.strip() != '']
            print(len(lst))
            lenth = len(lst)

            if lenth == 8:
                lst = lst[1::2]
                for data in lst:
                    print(data)
            elif lenth == 12:
                print("主人+猫喵。。。。。")
                for data in lst:
                    print(data)
            elif lenth == 6:
                print("主人。。。。。")
                for data in lst:
                    print(data)
