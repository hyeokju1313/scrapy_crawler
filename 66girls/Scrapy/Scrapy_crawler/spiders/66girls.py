import scrapy
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
from Scrapy_crawler.items import UrlItem

class UrlSpider(scrapy.Spider):
    name = "UrlCrawler"
    allowed_domains = ["66girls.co.kr"]
    start_urls = ['https://66girls.co.kr/product/list.html?cate_no=70']
    
    def parse(self, response):
        contents = response.xpath('//*[@class="xans-record-"]/div')
        items = []
        for content in contents:
            item = UrlItem()
            try:
                item['source'] = '66girls-Top'
                item['title'] = content.xpath('div[2]/strong/a/span[2]/text()').extract()[0]
                item['url'] = content.xpath('div[1]/div/a/@href').extract()[0]
                item['thumb'] = content.xpath('div[1]/div/a/img/@src').extract()[0]
            except IndexError:
                item['title'] = 'no'
                item['url'] = 'no'
                item['thumb'] = 'no'
            # print(item['title'])
            # print(item['url'])
            # print(item['thumb'])
            items.append(item)
        return items
