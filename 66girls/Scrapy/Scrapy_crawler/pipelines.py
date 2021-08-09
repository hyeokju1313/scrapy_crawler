from __future__ import unicode_literals
from scrapy.exporters import CsvItemExporter
from itemadapter import ItemAdapter

class CsvPipeline(object):
    def __init__(self):
        self.file = open("url.csv", 'wb')
        self.exporter = CsvItemExporter(self.file, encoding='utf-8')
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
