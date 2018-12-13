import scrapy

class goodreadsSpider(scrapy.Spider):
	name = "goodreads_auth_text"

	def start_requests(self):
		url = 'http://www.goodreads.com/quotes?page=1'
		yield scrapy.Request(url = url, callback = self.parse)

	def parse(self, response):
		for quote in response.selector.xpath("//div[@class='quote']"):
			yield {
				'text': quote.xpath(".//div[@class='quoteText']/text()[1]").extract_first(),
				'author': quote.xpath(".//div[@class='quoteText']/child::span/text()").extract_first(),
				'tags': quote.xpath(".//div[starts-with(@class, 'greyText')]/a/text()").extract(),
			}