import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SpiSpider(CrawlSpider):
    name = "spi"
    start_urls = ["https://www.marinetraffic.com/maritime-companies/directory/location:Bangladesh"]

    rules = (
        Rule(LinkExtractor(restrict_xpaths=('//h2[@class="no-margin font-150"]/a')), callback="parse_item", follow=False),
    )

    def parse_item(self, response):
        yield {
            'url': response.url,
        }