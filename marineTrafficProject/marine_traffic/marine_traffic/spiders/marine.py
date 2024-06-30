import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MarineSpider(CrawlSpider):
    name = "marine"
    start_urls = ["https://www.marinetraffic.com/maritime-companies/directory/page:1/location:Bangladesh/per_page:50/"]

    rules = (Rule(LinkExtractor(restrict_xpaths='//h2[@class="no-margin font-150"]/a'), callback="parse_item", follow=True),)
    

    def parse_item(self, response):
        title = response.xpath('//td[@colspan="2"]/text()').get()
        email = response.xpath('//span/a[@rel="nofollow"]/text()').get()
        yield {
            'title': title,
            'email': email,
            'url': response.url,
        }