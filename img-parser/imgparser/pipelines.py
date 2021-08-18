import os
from urllib.request import urlparse
 
from scrapy.pipelines.files import FilesPipeline
 
class ImgPipeline( FilesPipeline ):
    def file_path(self, request, response=None, info=None):
        return 'files/' + os.path.basename(urlparse(request.url).path)
