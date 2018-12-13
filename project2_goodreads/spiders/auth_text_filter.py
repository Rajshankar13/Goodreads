import scrapy
from scrapy.loader import ItemLoader
from project2_goodreads.items import QuoteItem

class goodreadsSpider(scrapy.Spider):
	name = "goodreads_auth_text_filter"

	def start_requests(self):
		url = 'http://www.goodreads.com/quotes?page=1'
		yield scrapy.Request(url = url, callback = self.parse)

	def parse(self, response):
		for quote in response.selector.xpath("//div[@class='quote']"):
			loader = ItemLoader(item = QuoteItem(), selector = quote, response = response)
			loader.add_xpath('text', ".//div[@class='quoteText']/text()[1]")
			loader.add_xpath('author', ".//div[@class='quoteText']/child::span")
			loader.add_xpath('tags', ".//div[starts-with(@class, 'greyText')]/a")
			yield loader.load_item()