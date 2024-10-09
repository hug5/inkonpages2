from flask import render_template

class HeaderCtl():

    def __init__(self):
        pass


    def doStart(self):

        # return ["headerHtml-0", "headerHtml-1"]

        # return "xxx"
        # return render_template(
        #     "headerHtml.jinja",
        #     # header = headerHtml
        #     # code=moon
        # )

        # return "XXXXXXXX"

        return render_template(
            "headerHtml.jinja",
        )
