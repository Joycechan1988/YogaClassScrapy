__author__ = 'hchen11'

from scrapy.spider import Spider
from scrapy import log, Request

class ylSpider(Spider):
    name = 'yl'
    allowed_domains = ["http://3.util.sinaapp.com/yl/"]
    start_urls = ["http://3.util.sinaapp.com/yl/"]

    def make_requests_from_url(self, url):
        return Request(url, cookies={'saeut':'216.113.160.68.1427679656108478','PHPSESSID':'dc3a630f4ab64aa59681e17ebaff3a44'}, dont_filter=True)

    def parse(self, response):
        log.msg("start parse", level=log.INFO)
        log.msg(response.body)
        ##todo
        log.msg("end parse", level=log.INFO)


