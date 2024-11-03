# from jug.lib.logger import logger, root
from jug.lib.logger import logger
from flask import render_template
from jug.lib.gLib import G
from jug.lib.fLib import F

from jug.dbo.dbc import Dbc

# try:
#     from jug.dbo.dbc import Dbc
# except Exception as e:
#     logger.info(f"XXX error: {e}")


class RankCtl():

    def __init__(self):
        self.config = {}
        self.html = ''

        self.url_page = ''  # what url are we at?

    def getHtml(self):
        return self.html

    def getConfig(self):
        # Called by router to set page title;
        return self.config

    def doConfig(self):

        self.config = {
            'site_title' : f"Rank | {G.site['name']}",
            'site_keywords' : "rank, " + G.site["keywords"],
        }


    def checkUrl(self):

        logger.info('---checkUrl')
        uri_list = F.getUriList()

        logger.info(f"---REQUEST_URL: {uri_list}")

        # /rank/bestseller/fiction/
        #  0     1         2           3        4        5
        # ['', 'rank', 'bestseller', 'fiction', '']
        # ['', 'rank', 'bestseller', 'fiction', 'asdf', ''']
        # ['', 'rank', 'bestseller', 'nonfiction', '']
        # ['', 'rank', 'alltime', '']

        G.sys["error"] = "redirect"

        # if uri_list[2] == 'bestseller' or len(uri_list) > 3:

        if uri_list[2] != "bestseller" and uri_list[2] != "alltime":
            logger.info("---check 0")
            G.sys["redirect"] = f"/{uri_list[1]}/bestseller/fiction/"
            return False

        elif uri_list[2] == 'bestseller' and \
         (uri_list[3] == 'fiction' or uri_list[3] == 'nonfiction') and \
         (len(uri_list) > 5 or uri_list[4] != ''):
            logger.info("---check 1")

            G.sys["redirect"] = f"/{uri_list[1]}/{uri_list[2]}/{uri_list[3]}/"
            return False

        elif uri_list[2] == 'alltime' and (len(uri_list) > 4 or uri_list[3] != ''):
            logger.info("---check 2")
            G.sys["redirect"] = f"/{uri_list[1]}/{uri_list[2]}/"
            return False

        elif uri_list[2] == "bestseller" and (uri_list[3] != "fiction" and uri_list[3] != "nonfiction"):
            logger.info("---check 3")
            G.sys["redirect"] = f"/{uri_list[1]}/{uri_list[2]}/fiction/"
            return False

        # url is okay
        G.sys["error"] = ""

        if uri_list[2] == "bestseller":
            # bestseller page
            self.url_page = "bestseller"
        else:
            self.url_page = uri_list[3]
            # fiction or nonfiction page

    # def getDb(self):

    #     try:
    #         dbo = Dbc()
    #         dbo.doConnect()

    #         # query  = "SELECT ARTICLENO, HEADLINE, BLURB FROM ARTICLES"
    #         query  = "SELECT HEADLINE FROM ARTICLES WHERE STATUS='N' AND TAGS='paperdrift'"

    #         # get back cursor
    #         curs = dbo.doQuery(query)
    #         # logger.info(f"curs: {curs}")  # this gives me a binary value;

    #         result_list = []

    #         # If single field, do this way:
    #         for row in curs:
    #             result_list.append(row[0])

    #         logger.info(f"db_result: {result_list}")


    #         db_result = result_list[ random.randrange( len(result_list) ) ]
    #         logger.info(f"db_result: {db_result}")

    #     except Exception as e:
    #         # print(f"Error committing transaction: {e}")
    #         # return [["bad db connection", e]]
    #         logger.info(f"exception: {e}")

    #     finally:
    #         dbo.doDisconnect()
    #         pass

    #     # logger.info('return result')
    #     return [db_result]
    #         # return as list, not string; will combine with other news list later;

    def getBSListDb(self, category):

        logger.info("---begin getBSListDb")

        dbo = Dbc()
        dbo.doConnect()

        query  = f"SELECT * FROM IPBRANK WHERE CATEGORY = '{category}' ORDER BY DATETIME DESC, RANK ASC LIMIT 100"

        #$result = dbo::doQuery($query);
        #if (!$result) return false;

        try:
            curs = dbo.doQuery(query)

            result_list = []

            for row in curs:
                result_list.append(row[1])  # date
                # result_list.append(row)

            logger.info(f"db_result: {result_list}")

            '''
            # db_result: [
            (52104, datetime.datetime(2021, 8, 3, 6, 0, 7), 'fiction', 1, 'The Last Thing He Told Me', ' Laura Dave', 'https://www.amazon.com/dp/B08LDY1MKW/', 'https://m.media-amazon.com/images/I/81BdMSuI5ZS.jpg'),
            (52105, datetime.datetime(2021, 8, 3, 6, 0, 7), 'fiction', 2, 'Black Ice', 'Brad Thor', 'https://www.amazon.com/ dp/B08LDWSKZT/', 'https://m.media-amazon.com/images/I/81JFwwMELdL.jpg'),
            (52106, datetime.datetime(2021, 8, 3, 6, 0, 7), 'fiction', 3, 'The Paper Palace', 'Miranda Cowley Heller', 'https://www.amazon.com/dp/B08R96D5FF/', ' https://m.media-amazon.com/images/I/81XXxS1L4iS.jpg'),
            (52107, datetime.datetime(2021, 8, 3, 6, 0, 7), 'fiction ', 4, 'The Cellist', 'Daniel Silva', 'https://www.amazon.com/dp/B08L3NB7FL/', 'https://m.media-amazon.com/image s/I/71LfMuoD+7S.jpg'),
            (52108, datetime.datetime(2021, 8, 3, 6, 0, 7), 'fiction', 5, 'False Witness', 'Karin Sl aughter', 'https://www.amazon.com/dp/B09239CX27/', 'https://m.media-amazon.com/images/I/81-fM8bLdNS.jpg'),
            (521 09, datetime.datetime(2021, 8, 3, 6, 0, 7), 'fiction', 6, 'People We Meet On Vacation', 'Emily Henry', 'https:/ /www.amazon.com/dp/B08FZNYQJC/', 'https://m.media-amazon.com/images/I/81yUZUVyOcS.jpg'),
            '''

        except Exception as e:
            # print(f"Error committing transaction: {e}")
            logger.info(f"XXXXXXX db exception: {e}")

        finally:
            dbo.doDisconnect()
            pass

        # logger.info('return result')
        # return result_list


        # $row = $result->fetch_assoc();
        # $datetime = $row["DATETIME"]; //stop fetching when date doesn't match this one;
        # $arr[] = $row;

        # // throw result into array
        # while ( $row = $result->fetch_assoc() ) {
        #     $date = $row["DATETIME"];
        #     if ($date !== $datetime) break; //if date time doesn't match, then stop
        #     $arr[] = $row;
        # }

        # //reverse the order so that bestsellers are listed first;
        # //$arr = array_reverse($arr);
        # return $arr;



    def doRank(self):
        logger.info('---doRank')
        if self.checkUrl() is False: return
        logger.info("---check OKay")

        self.getBSListDb("fiction")

        self.html = render_template(
            "rankHtml.jinja",
        )
        self.doConfig()


# https://inkonpages.com/rank/bestseller/fiction/
  # IP Bestsellers for FICTION | Nov 1, 2024, Friday | Inkonpages Press
# https://inkonpages.com/rank/bestseller/nonfiction/
  # IP Bestsellers for NONFICTION | Nov 1, 2024, Friday | Inkonpages Press
# https://inkonpages.com/rank/alltime/
  # Most Popular Books of ALL TIME | Nov 1, 2024, Friday | Inkonpages Press