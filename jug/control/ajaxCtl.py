from jug.lib.logger import logger
# from flask import render_template
# from jug.lib.f import F
# from jug.lib.weather_api import Weather_api
# from jug.lib.gLib import G
# import random
# import random



class AjaxCtl:

    # def __init__(self, jug, request_data):
    def __init__(self, request_data):

        # logger.info('LocationCtl __init__')
        # self.url = url.rstrip('/').capitalize()

        # self.jug = jug

        logger.info('--- Ajax init')

        self.action = request_data['action']

        logger.info(f'--- {self.action}')

        self.data = request_data
        self.result = {}
        logger.info(f'--- {self.data}')

    def getResult(self):
        return self.result


    # def get_Britannica_Location(self, location):
    #     news_scrapeO = News_Scrape()
    #     news_scrapeO.get_britannica(location)
    #     scrape_result = news_scrapeO.getResult()

    #     # if not json_result:

    #     imageUrl = "https://cdn.britannica.com/37/245037-050-79129D52/world-map-continents-oceans.jpg?w=300&h=1000"
    #     url = "https://www.britannica.com/Geography-Travel"
    #     descriptionList = [
    #         f'{location} is a shadowy settlement in an undisclosed location. Not much is known except that the mayor ran off with the barmaid and left his wife and seven children in penury destitution. But all was not lost as word arrived she was sole heir to the Snickers estate. Soon she was flowing in chocolate and romantic suitors as far as the cocoa eye can see.',
    #         f'{location} is a tropical haven in the Pacific. It enjoys year round sun, upscale tourists three months out of the calendar year, and tons of seafood sold by the bucket. According to local lore, Poseidon and Amphitrite used {location} as a summer palace and made giant sand chateaus on the beach with fixtures and indoor plumbing that can still be seen today.',
    #         f'{location} was established as a fortification in 1392 in the steppes of Siberia. Although the fort proved unsuccessful, its inhabitants survived half a dozen seasons on a diet of sheep, turnip and rye. While discipline and comraderie was strong among the young warriors, fighting broke out when a woman arrived and began to spread gossip and rumors. It would seem that there\'s more than one way to conquer a fort.',
    #         f'{location} was originally founded as a debtor penal colony in forested hills in the high mountains. Men were put to work chopping trees and women labored long hours collecting local vegetation. Carpenters produced barrels, tables and chairs. And women compressed fruits and vegetables into wine and green libations. Soon exports boomed and profits flowed to the industrial colony, freeing all men and women from their debts.'
    #     ]
    #     # Randomly choose 1
    #     description = descriptionList[random.randrange(0, len(descriptionList))]

    #     # In case any values are missing, replace with fiction:
    #     json_result = {}
    #     json_result["title"] = scrape_result.get("title", location)  # City
    #     json_result["url"] = scrape_result.get("url", url)
    #     json_result["description"] = scrape_result.get("description", description)
    #     json_result["imageUrl"] = scrape_result.get("imageUrl", imageUrl)

    #     json_result["status"] = "ok"

    #     self.result = json_result


    def do_contact_us(self):
        from jug.control.mailCtl import MailCtl

        logger.info("---doing contact_us")


        # mail = MailCtl(self.jug)
        mail = MailCtl()
        result = mail.do_contact_us(self.data)

        logger.info(f'--- mail contact_us result: {result}')

        json_result = {}
        json_result["status"] = result
        self.result = json_result


    def get_rank(self):

        def get_rankDb(category):
            from jug.dbo.rankDb import RankDb
            # Get news item from Yahoo News with request
            rankDb = RankDb()
            if category == "alltime":
                rankDb.getAlltimeRankDb()
            else:
                rankDb.getBSListDb(category)
            return rankDb.get_db_result()


        def do_rankBookCell(db_result):
            from jug.control.rankCtl import RankCtl
            Rank = RankCtl()
            Rank.do_rankBookCell(db_result)
            return Rank.getHtml()

        def do_json(rankBookCell):
            json_result = {}
            json_result["status"] = "ok"
            # json_result["rank_result"] = db_result
            json_result["rank_result"] = rankBookCell
            # json_result["rank_result"] = "<h2>hello</h2><p>bye</p>"
            self.result = json_result


        db_result = get_rankDb(self.data['category'])
        rankBookCell = do_rankBookCell(db_result)
        do_json(rankBookCell)


    def doAjax(self):

        if self.action == "get_rank":
            self.get_rank()

            # if some problem:
                # self.result = {
                #     "status" : "bad",
                #     "error_message" : "No location."
                # }
        elif self.action == "contact_us":
            self.do_contact_us()
