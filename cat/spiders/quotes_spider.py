# -*- coding: utf-8 -*-
import scrapy

# scrapy runspider quotes_spider.py
# scrapy crawl quotes --nolog -o quotes.json


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]
    custom_settings = {
        'LOG_LEVEL' : 'ERROR',
        'LOG_FILE' : 'hello.log'
    }

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.xpath('span/small/text()').extract_first(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
