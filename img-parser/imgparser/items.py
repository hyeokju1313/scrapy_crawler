import scrapy

class ImgItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()
    pass
