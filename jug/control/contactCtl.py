# import logging
# logger = logging.getLogger(__name__)

# from jug.lib.logger import logger, root
from jug.lib.logger import logger
from flask import render_template
# from jug.lib.f import F
# import random
from jug.lib.gLib import G
from jug.lib.fLib import F



class ContactCtl():

    def __init__(self):
        self.config = {}
        self.html = ''

    def getHtml(self):
        return self.html

    def getConfig(self):
        # Called by router to set page title;
        return self.config

    def doConfig(self):

        self.config = {
            'site_title' : f"Contact | {G.site['name']}",
            'site_keywords' : "contact us, email, " + G.site["keywords"],
        }


    def checkUrl(self):

        logger.info('---checkUrl')
        uri_list = F.getUriList()
          # ['', 'contact', '']
          # ['', 'contact', 'xxx']

        logger.info(f"---REQUEST_URL: {uri_list}")

        # Currently, the url should only be /contact/
        # Anything else is wrong;
        if len(uri_list) > 3 or uri_list[2] != '':
            # G.sys["error"] = "redirect"
            # G.sys["redirect"] = "/" + uri_list[1] + "/"
            F.abort("redirect", "/" + uri_list[1] + "/")
            return False


    def doContact(self):
        logger.info('---doContact')

        if self.checkUrl() is False: return
        # if self.checkUrl() is not False:
        self.doConfig()
        self.html = render_template(
            "contactHtml.jinja",
            email = G.contact.get("email"),
            email_name = G.contact.get("email_name")
        )

