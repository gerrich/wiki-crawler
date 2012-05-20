# Scrapy settings for wiki_crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'wiki_crawler'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['wiki_crawler.spiders']
NEWSPIDER_MODULE = 'wiki_crawler.spiders'
DEFAULT_ITEM_CLASS = 'wiki_crawler.items.WikiCrowlerItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

