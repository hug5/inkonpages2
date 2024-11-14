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

    def do_scrape_bestseller_Db(self, scrape_list):
        from jug.dbo.rankDb import RankDb

        rankDb = RankDb()
        rankDb.postBestSellerScrape(scrape_list)


    def do_scrape_bestseller(self):

        from jug.lib.scrape import Scrape

        scrape_obj = Scrape()
        scrape_obj.doScrape()
        scrape_list = scrape_obj.getResult()

        # Do database post
        # result = self.do_scrape_bestseller(scrape_list)

        # self.result = scrape_list

        logger.info(f'---bestseller scrape: {scrape_list}')
        # Return json
        # self.result = {"result":"ok"}
        self.result = {"result":f"{scrape_list}"}


    def doRest(self):

        logger.info('---doRest')

        if self.url == "scrape-bestseller":
            logger.info('---scrape-bestseller')
            self.do_scrape_bestseller()

        else:
            logger.info(f'---ELSE bestseller scrape: {self.url}')
            # self.result = ""


