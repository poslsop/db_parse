# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UniportItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    guideto_target_id = scrapy.Field()
    drugbank_target_id = scrapy.Field()
