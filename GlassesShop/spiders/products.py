# -*- coding: utf-8 -*-
import scrapy


class ProductsSpider(scrapy.Spider):
    name = 'products'
    allowed_domains = ['glassesshop.com']
    start_urls = ['https://glassesshop.com/bestsellers/']

    def parse(self, response):
        products=response.xpath("//div[@class='col-sm-6 col-md-4 m-p-product']")
        for product in products:
            product_name=product.xpath(".//a[@class='pull-left']/text()").get()
            product_url=product.xpath(".//a[@class='pull-left']/@href").get()
            product_image=product.xpath(".//img[@class='default-image-front']/@src").get()
            product_price=product.xpath(".//span[@class='pull-right']/text()").get()

            yield{
                'product_name':product_name,
                'product_url':product_url,
                'product_image':product_image,
                'product_price':product_price
            }

        next_page=response.xpath("//a[@rel='next']/@href").get()
        if next_page:
            yield scrapy.Request(url=next_page,callback=self.parse)
