# -*- coding: utf-8 -*-

# Scrapy settings for myScrapy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'myScrapy'

SPIDER_MODULES = ['myScrapy.spiders']
NEWSPIDER_MODULE = 'myScrapy.spiders'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.cookies.CookiesMiddleware': 700
}

COOKIES_DEBUG = True

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'myScrapy (+http://www.yourdomain.com)'
