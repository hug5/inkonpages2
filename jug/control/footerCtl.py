from flask import render_template

class FooterCtl():

    def __init__(self):
        self.html = None
        pass

    def getHtml(self):
        return self.html

    def doFooter(self, cfDict):

        self.html = render_template(
            "footerHtml.jinja",
            cfDict = cfDict
        )


    def start(self, cfDict):
        self.doFooter(cfDict)