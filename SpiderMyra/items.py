# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpidermyraItem(scrapy.Item):
    texto = scrapy.Field()
    autor = scrapy.Field()
    tags = scrapy.Field()
