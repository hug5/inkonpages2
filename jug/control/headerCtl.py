from flask import render_template
# from jug.lib.gLib import G


class HeaderCtl():

    def __init__(self):
        self.html = None
        pass

    def getHtml(self):
        return self.html


    def doHeader(self):

        self.html = render_template(
            "headerHtml.jinja",
            # site = G.site
            # base_url = base_url,
            # bestseller_url = bestseller_url,
            # contact_url = contact_url
        )

