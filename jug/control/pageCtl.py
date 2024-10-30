from jug.lib.logger import logger
from flask import render_template
from jug.lib.fLib import F
from jug.control.headerCtl import HeaderCtl
from jug.control.footerCtl import FooterCtl
from jug.lib.gLib import G


class PageCtl():

    def __init__(self):

        self.article = ''
        self.header = ''
        self.footer = ''
        self.ascii_art = ''

        self.html = ''

    def getHtml(self):
        return self.html

    def doHeader(self):
        ob = HeaderCtl()
        ob.start()
        self.header = ob.getHtml()

    def doFooter(self):
        ob = FooterCtl()
        ob.start()
        self.footer = ob.getHtml()

    def doAscii_art(self):
        # self.ascii_art = render_template(
        #     "ascii_art.jinja"
        # )

        # Have to wrap with () to use multiple lines, it seems:

        self.ascii_art = ("<!-- \n" +
        "// [==]  👹 paperdrift  <o=o> //-->")


    def doCommon(self):
        # logger.info('DoCommon')
        self.doHeader()
        self.doFooter()
        self.doAscii_art()
        # pass

    def doHome(self):
        from jug.control.homeCtl import HomeCtl

        logger.info('DoHome')
        # F.uwsgi_log("doHome")
        self.doCommon()

        home_ob = HomeCtl()
        home_ob.doHome()


        self.article = home_ob.getHtml()
        site_title = home_ob.getConfig()["site_title"]

        site_keywords = G.site["keywords"]

        html = render_template(
            "pageHtml.jinja",
            title = site_title,
            header = self.header,
            article = self.article,
            footer = self.footer,
            site_keywords = site_keywords
        )

        logger.info(f'---type info: {type(html)}')

        self.html = F.stripJinja(html) + self.ascii_art


    def doLocationUrl(self, url):
        from jug.control.locationCtl import LocationCtl

        logger.info('DoLocationUrl')

        self.doCommon()

        location_ob = LocationCtl(url)
        # self.article = location_ob.start()
        location_ob.doLocation()
        self.article = location_ob.getHtml()
        site_title = location_ob.getConfig()["site_title"]

        site_keywords = G.site["keywords"]

        html = render_template(
            "pageHtml.jinja",
            title = site_title,
            header = self.header,
            article = self.article,
            footer = self.footer,
            site_keywords = site_keywords
        )

        self.html = F.stripJinja(html) + self.ascii_art
