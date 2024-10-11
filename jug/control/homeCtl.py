# import logging
# logger = logging.getLogger(__name__)

from jug.lib.logger import logger
from flask import render_template
# from jug.lib.f import F
# import random
# from jug.lib.g import G


class HomeCtl():

    def __init__(self):
        self.config = {}
        pass

    def getConfig(self):
        return self.config

    def doConfig(self):

        # self.config = {
        #     'site_title' : f"{G.site['name']} | {G.site['tagline']}"
        # }
        pass

    def doHome(self):

        # self.doConfig()

        return render_template(
            "homeHtml.jinja",
        )


    def doStart(self):
        return self.doHome()

