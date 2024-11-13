from jug.lib.logger import logger
# from flask import render_template
# from jug.lib.f import F
# from jug.lib.weather_api import Weather_api
# from jug.lib.gLib import G
# import random
# import random

# Maybe revisit this in future:
# https://flask-restful.readthedocs.io/en/latest/index.html


class RestCtl:

    def __init__(self, url):
        self.url = url
        self.result = {"result":"?"}


    def getResult(self):
        return self.result


    def scrape_bestseller(self):

        from jug.lib.scrape import Scrape

        scrape_obj = Scrape()
        scrape_obj.doScrape()
        scrape_list = scrape_obj.getResult()

        logger.info(f'---bestseller scrape: {scrape_list}')
        self.result = {"result":"ok"}


    def doRest(self):

        logger.info('---doRest')

        if self.url == "scrape-bestseller":
            logger.info('---scrape-bestseller')
            self.scrape_bestseller()

        else:
            logger.info(f'---ELSE bestseller scrape: {self.url}')
            # self.result = ""


