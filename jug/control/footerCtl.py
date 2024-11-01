from flask import render_template

class FooterCtl():

    def __init__(self):
        self.html = None
        pass

    def getHtml(self):
        return self.html

    def doFooter(self):

        self.html = render_template(
            "footerHtml.jinja",
        )


    def start(self, cfDict):
        self.doFooter(cfDict)