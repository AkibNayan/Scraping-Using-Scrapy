import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BpropertySpider(CrawlSpider):
    name = "bproperty"
    start_urls = ["https://www.bproperty.com/en/dhaka/properties-for-rent/"]

    rules = (Rule(LinkExtractor(restrict_xpaths='//li[@aria-label="Listing"]/article/div[1]/a'), callback="parse_item", follow=True),)

    def parse_item(self, response):
        yield {
            'title': response.xpath('//h1[@class="fcca24e0 fontCompensation"]/text()').get(),
            'area': response.xpath('//span[@class="fc2d1086"]/span/text()').get(),
            'bed': response.xpath('//span[@aria-label="Beds"]/span[@class="fc2d1086"]/text()').get(),
            'bath': response.xpath('//span[@aria-label="Baths"]/span[@class="fc2d1086"]/text()').get(),
            'type': response.xpath('//span[@aria-label="Type"]/text()').get(),
            'url': response.url
        }
        
