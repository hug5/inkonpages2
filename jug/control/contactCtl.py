# import logging
# logger = logging.getLogger(__name__)

# from jug.lib.logger import logger, root
from jug.lib.logger import logger
from flask import render_template
# from jug.lib.f import F
# import random
from jug.lib.gLib import G



class ContactCtl():

    def __init__(self):
        self.config = {}
        self.html = None

    def getHtml(self):
        return self.html

    def getConfig(self):
        # Called by router to set page title;
        return self.config

    def doConfig(self):

        # A tuple ternary operator;
        # If there is a tagline, then combine name with tagline; otherwise, just stie name;
        # self.config = (
        #     {'site_title' : f"{G.site['name']}"},
        #     {'site_title' : f"{G.site['name']} | {G.site['tagline']}"}) \
        #     [ G.site['tagline'] != "" ]

        self.config = {
            'site_title' : f"Contact | {G.site['name']}",
            'site_keywords' : "contact us, email, " + G.site["keywords"],
        }


    def checkUrl(self):

        # print(url)

        logger.info('---checkUrl')
        # logger.info(f'---Beginning state self.redirect variable: {self.redirect}')

        req_uri = G.sys["req_uri"]
        logger.info(f"---REQUEST_URI: {req_uri}")
        url_list = req_uri.split("/")

        # logger.info(f"---Flask path: {url}")
        logger.info(f"---REQUEST_URL: {url_list}")
          # ['', 'contact', '']
          # ['', 'contact', 'xxx']
        logger.info(f"---REQUEST_URL len: {len(url_list)}")


        # if url_list[3] != '':

        # Home: ['', '']
        # Home: ['', '?asdf']
        # some path: ['', 'san%20diego', '?']
        # url1 = url_list[1]

        # Was trying to catch any suffix beginning with #, but can't seem to do it;
        # There doesn't seem to be a way to grab that value or its existence;
        # parsed_url = parse.urlparse(req_url)
        # fragment = parsed_url[5]
        # logger.info(f'***url_fragment: {parsed_url}')
        ##:: ParseResult(scheme='https', netloc='station.paperdrift.com', path='/first second/third fourth/', params='', query='hello=goodbye&ciao=buenes', fragmenurlurlt='marker')


                # url_list_len = len(url_list)
                # logger.info(f'***checkUrl: {url_list} : {url_list_len}')

                # # We're at home page
                # if url_list_len == 2 and url_list[1] != '':
                #     # r_url = "/"
                #     r_url = G.site["baseUrl"]
                #     logger.info(f'***checkUrl, badurl: "{r_url}"')
                #     self.redirect = [True, r_url]

                # # If like this: ['', 'san%20diego', 'asdf', ''], or more;
                # # Then too many paths; redirect to index 1
                # if url_list_len >= 4:
                #     url = url_list[1]
                #     r_url = self.cleanUrl(url)
                #     logger.info(f'***checkUrl, badurl: "{r_url}"')
                #     self.redirect = [True, r_url]

                # # if like this: ['', 'san%20diego', '?',]
                # # Then check index 1 and 2
                # if url_list_len == 3:
                #     if url_list[2] != '':
                #         url = url_list[1]
                #         r_url = self.cleanUrl(url)
                #         logger.info(f'***checkUrl, badurl: "{r_url}"')
                #         self.redirect = [True, r_url]

                #     else:
                #         r_url = self.cleanUrl(url_list[1])
                #         url = f'/{url_list[1]}/'
                #         if r_url != url:
                #             logger.info(f'***checkUrl, badurl: "{r_url}"')
                #             self.redirect = [True, r_url]

                # #/favicon.ico


                # logger.info(f'End. state self.redirect: {self.redirect}')

                # # self.redirect = [False, '']



    def doContact(self):
        logger.info('---doContact')

        self.checkUrl()
        self.doConfig()
        self.html = render_template(
            "contactHtml.jinja",
        )

