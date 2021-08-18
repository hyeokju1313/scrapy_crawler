import csv
import os
import sys
import scrapy
import import_csv as ics
from imgparser.items import ImgItem
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

start_urls = 'https://66girls.co.kr{}'
class ImgSpider(scrapy.Spider):
    name = "ImgCrawler"
    allowed_domains = ["66girls.co.kr"]

    def start_requests(self):
        tags = ics.get_list_csv('url.csv', 0, ignore_header=True)
        for tag in tags:
            yield scrapy.Request(start_urls.format(tag))
    def parse(self, response):
        contents = response.xpath('//*[@class="cont_detail"]')
        file_urls = []
        for content in contents:
            item = ImgItem()
            try:
                item['file_urls'] = content.xpath('img/@src').extract()
            except IndexError:
                pass
            file_urls.append(item)
        return file_urls
