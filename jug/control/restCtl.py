from jug.lib.logger import logger
# from flask import render_template
# from jug.lib.f import F
# from jug.lib.weather_api import Weather_api
# from jug.lib.gLib import G
# import random
# import random



class RestCtl:

    def __init__(self, url):
        self.url = url
        self.result = None


    def getResult(self):
        return self.result


    def spider_bestseller(self):

        from jug.lib.scrape import Scrape

        scrape_obj = Scrape()
        scrape_obj.doScrape()
        scrape_list = scrape_obj.getResult()

        logger.info(f'---bestseller scrape: {scrape_list}')
        self.result = "ok"


    def doRest(self):

        if self.url == "spider_bestseller":
            self.spider_bestseller()


