from flask import render_template

class FooterCtl():

    def __init__(self):
        pass


    def doStart(self):

        return render_template(
            "footerHtml.jinja"
        )
