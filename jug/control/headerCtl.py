from flask import render_template

class HeaderCtl():

    def __init__(self):
        pass


    def doStart(self):

        return render_template(
            "headerHtml.jinja",
        )
