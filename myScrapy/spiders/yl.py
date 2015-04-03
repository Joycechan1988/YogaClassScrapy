__author__ = 'hchen11'

from scrapy.spider import Spider
from scrapy import log, Request


class ylSpider(Spider):
    name = 'yl'
    allowed_domains = ['*']
    start_urls = ["http://3.util.sinaapp.com/yl/"]
    day = ''

    def make_requests_from_url(self, url):
        return Request(url, cookies={'saeut':'216.113.160.68.1427679656108478','PHPSESSID':'87094be5a61f22448212a9bd3ecabad8'}, dont_filter=True)

    def parse(self, response):
        urllist = []
        for url in response.xpath('//a[@href]/@href').extract():
            if "day=2015" in url:
                urllist.append(url)
        url = urllist.pop(3)
        self.day = url[14:]
        url= "http://3.util.sinaapp.com/yl/"+url
        yield Request(url, cookies={'saeut':'216.113.160.68.1427679656108478','PHPSESSID':'87094be5a61f22448212a9bd3ecabad8'}, dont_filter=True, callback=self.parseurl)


    def parseurl(self, response):
        url = ajax_template.format()
        yield Request(url="http://112.124.111.116:8080/wx/appointment/list.action", dont_filter=True, callback=self.parseJS)

    def parseJS(self, response):
        log.msg(response.body)
