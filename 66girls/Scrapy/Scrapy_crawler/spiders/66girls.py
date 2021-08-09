import scrapy
from Scrapy_crawler.items import UrlItem

class UrlSpider(scrapy.Spider):
    name = "UrlCrawler"
    allowed_domains = ["66girls.co.kr"]
    start_urls = ['https://66girls.co.kr/product/list.html?cate_no=70']
    
    def parse(self, response):
        contents = response.xpath('//*[@class="xans-record-"]/div')
        for content in contents:
            item = UrlItem()
            item['source'] = '66girls-Top'
            item['title'] = content.xpath('div[2]/strong/a/span[2]/text()').extract()
            item['url'] = content.xpath('div[1]/div/a/@href').extract()
            item['thumb'] = content.xpath('div[1]/div/a/img/@src').extract()
            # print(item['title'])
            # print(item['url'])
            # print(item['thumb'])
        yield item
