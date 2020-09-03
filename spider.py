# -*- coding: utf-8 -*-
import scrapy
import sys
import json
from items import FinalItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.item import Item

class ToScrapeSpiderXPath(CrawlSpider):
    name = 'toscrape-xpath'
    start_urls = [
        'https://www.dynamiteclothing.com/ca/d/sale/clearance/?lang=en_CA',
    ]

    rules = (Rule(LinkExtractor(), callback='parse_url', follow=False), )

    # def dataItem():
    # 	data = {}
    # 	return data 


    # def parse_url(self, response):
	   #  sel = Selector(response)
	   #  items = sel.select('//div[@class="final-sale callout"]')
	   #  data = {}
	   #  for item in items:
	   #      #data = DataItem()
	   #      data['item'] = item.xpath("//h1[contains(@class, 'product-name')]/text()").extract_first()
	   #      #allData.append(data)
	   #  sys.stdout.write(data)
	   #  yield data

    # def parse_url(self, response):
    #     items = FinalItem()
    #     for quote in response.xpath('//div[@class="final-sale callout"]'):
    #         name =  quote.xpath("//h1[contains(@class, 'product-name')]/text()").extract_first()
    #         number = quote.xpath('//div[@class="container product-detail product-wrapper"]/@data-pid').extract_first()
    #         items['name'] = name
    #         items['number'] = number
    #     yield items

    def parse_url(self, response): 
        for quote in response.xpath('//div[@class="final-sale callout"]'):
            yield {
                'item': quote.xpath("//h1[contains(@class, 'product-name')]/text()").extract_first(),
                'number': quote.xpath('//div[@class="container product-detail product-wrapper"]/@data-pid').extract_first()
            }


