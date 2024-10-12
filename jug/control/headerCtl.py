from flask import render_template
                  # request


class HeaderCtl():

    def __init__(self):
        self.html = None
        pass

    def getHtml(self):
        return self.html


    def doHeader(self, cfDict):

        self.html = render_template(
            "headerHtml.jinja",
            cfDict = cfDict
            # base_url = base_url,
            # bestseller_url = bestseller_url,
            # contact_url = contact_url
        )


    def start(self, cfDict):
        self.doHeader(cfDict)

