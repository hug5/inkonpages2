# import logging
# logger = logging.getLogger(__name__)

from jug.lib.logger import logger
from flask import render_template
# from jug.lib.f import F
# import random
from jug.lib.g import G


class HomeCtl():

    def __init__(self):
        self.config = {}
        self.html = None

    def getHtml(self):
        return self.html

    def getConfig(self):
        # Called by router to set page title;
        return self.config

    def doConfig(self):

        self.config = {
            # 'site_title' : f"{G.site['name']} | {G.site['tagline']}"
            'site_title' : f"{G.site['name']}"
        }

    def doHome(self):
        from datetime import date
        today = date.today().strftime("%A, %b. %d, %Y")
          # there datetime.datetime, datetime.date, datetime.time, datetime.timedelta, tzinfo;
          # datetime may be a combination of date/time;
          # date is just date;

        self.doConfig()

        self.html = render_template(
            "homeHtml.jinja",
            today = today,
        )

    def start(self):
        # return self.doHome()
        self.doHome()

