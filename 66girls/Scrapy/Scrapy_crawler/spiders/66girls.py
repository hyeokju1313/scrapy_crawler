import scrapy
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
from Scrapy_crawler.items import UrlItem

class UrlSpider(scrapy.Spider):
    name = "UrlCrawler"
    allowed_domains = ["66girls.co.kr"]
    
    def start_requests(self):
        for i in range(1, 8):
            yield scrapy.Request("https://66girls.co.kr/product/list.html?cate_no=70&page={0}".format(i), self.parse)
    
    def parse(self, response):
        contents = response.xpath('//*[@class="xans-record-"]/div')
        items = []
        for content in contents:
            item = UrlItem()
            item['source'] = '66girls-Top'
            try:
                item['title'] = content.xpath('div[2]/strong/a/span[2]/text()').extract()[0]
                item['url'] = content.xpath('div[1]/div/a/@href').extract()[0]
                item['thumb'] = content.xpath('div[1]/div/a/img/@src').extract()[0]
            except IndexError:
                pass
            
            items.append(item)
        return items
