from scrapy.pipelines.files import FilesPipeline


BOT_NAME = 'imgparser'

SPIDER_MODULES = ['imgparser.spiders']
NEWSPIDER_MODULE = 'imgparser.spiders'

ROBOTSTXT_OBEY = True

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,
}
FILES_STORE = 'downloads'

DEFAULT_FILES_URLS_FIELD = 'file_urls'
DEFAULT_FILES_RESULT_FIELD = 'files'

ITEM_PIPELINES = {
    'imgparser.pipelines.ImgPipeline': 100,
}

DOWNLOAD_DELAY = 3

CONCURRENT_REQUESTS = 1
