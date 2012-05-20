from scrapy.spider import BaseSpider
from scrapy.http import Request

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

from wiki_crawler.items import WikiItem

class WikiSpider(BaseSpider):
  name = "wiki"
  #allowed_domains = ["simple.wikipedia.org"]
  start_urls = [
    "http://simple.wikipedia.org/wiki/Main_Page"
  ]
  link_extractor = SgmlLinkExtractor(allow=['simple\.wikipedia\.org/wiki/\w+$'])
  '''
  rules = [
    Rule(
      link_extractor,
      'parse_link',
      follow=True
    )
  ]
  '''
  page_counter = 0

  def get_page_name(self, url):
    return url.split("/")[-1]

  def parse(self, response):
    self.page_counter += 1
    ctx = HtmlXPathSelector(response)
    title = ctx.select('//title').extract()
    page_name = self.get_page_name(response.url)
    print self.page_counter, "page:", page_name
    open("pages/%s"%page_name, 'wb').write(response.body)
    links = self.link_extractor.extract_links(response)
    print "links:", page_name, (" ".join([self.get_page_name(a.url) for a in links]))
    for link in links:
      yield Request(link.url, callback=self.parse)
