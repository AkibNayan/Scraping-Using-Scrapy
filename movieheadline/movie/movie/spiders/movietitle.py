import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class MovietitleSpider(CrawlSpider):
    name = "movietitle"
    start_urls = ["https://subslikescript.com/movies_letter-Z?page=1"]

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//ul[@class="scripts-list"]/a'), callback="parse_item", follow=True),
        Rule(LinkExtractor(restrict_xpaths='(//a[@rel="next"])[1]'), callback="parse_item", follow=True),
    )

    def parse_item(self, response):
        article= response.xpath('//article[@class="main-article"]')
        yield {
            "Title": article.xpath('./h1/text()').get(),
            'Plot': article.xpath('./p/text()').get()
        }
