import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from GlassesShop.spiders.products import ProductsSpider

process=CrawlerProcess(settings=get_project_settings())
process.crawl(ProductsSpider)
process.start()
