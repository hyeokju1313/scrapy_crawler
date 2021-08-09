import scrapy

class UrlItem(scrapy.Item):
    source = scrapy.Field() # 쇼핑몰
    title = scrapy.Field() # 상품명
    url = scrapy.Field() # 해당 상품 링크
    thumb = scrapy.Field() # 상품 썸네일
    pass
