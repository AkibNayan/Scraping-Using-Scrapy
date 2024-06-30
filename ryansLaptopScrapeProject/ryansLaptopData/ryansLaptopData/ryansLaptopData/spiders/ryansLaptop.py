import scrapy


class RyanslaptopSpider(scrapy.Spider):
    name = "ryansLaptop"
    start_urls = [
        "https://www.ryans.com/category/laptop-all-laptop?limit=100&sort=D&osp=1&st=0&page=1",
        ]

    def parse(self, response):
        cards = response.xpath(
            '//div[@class="cus-col-2 cus-col-3 cus-col-4 cus-col-5 category-single-product mb-2 context1"]')
        for card in cards:
            title = card.css("p.list-view-text > a::text").get()
            #print(title)
            price = card.css(
                "div.card-body > a.text-decoration-none::text").get()
            #print(price)
            yield{
                "title" : title,
                "price" : price
            }
            
        next_page = response.css("li.page-item > a[rel='next']::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

