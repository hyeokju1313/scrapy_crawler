BOT_NAME = 'Scrapy_crawler'

SPIDER_MODULES = ['Scrapy_crawler.spiders']
NEWSPIDER_MODULE = 'Scrapy_crawler.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {'Scrapy_crawler.pipelines.CsvPipeline': 300, }

FEED_EXPORT_FIELDS=["source", "title", "url", "thumb"]

DUPEFILTER_CLASS = 'scrapy.dupefilters.BaseDupeFilter'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,
}

DOWNLOAD_DELAY = 5
