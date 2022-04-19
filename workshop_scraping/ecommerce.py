# -*- coding: utf-8 -*-
import scrapy


class EcommerceSpider(scrapy.Spider):
    name = 'ecommerce'
    allowed_domains = ['webscraper.io/test-sites/e-commerce/static']
    start_urls = ['http://webscraper.io/test-sites/e-commerce/static/']

    def parse(self, response):
        pass
