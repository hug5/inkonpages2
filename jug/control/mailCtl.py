from jug.lib.logger import logger

# from flask import redirect, request, jsonify, session
#, make_response
from jug.lib.fLib import F
from jug.lib.gLib import G
from flask_mail import Mail, Message


class MailCtl():

    def __init__(self, jug):
        self.jug = jug
        pass


    # public
    def do_contact_us(self, data):

        # logger.info(f"---mailCtl data: {data}")
        # from_name = data.get("name")
        # from_email = data.get("email")
        # from_msg = data.get("msg").replace("\n", "<br>")

        from_name = F.hesc(F.unquote(data.get("name")))
        from_email = F.hesc(F.unquote(data.get("email")))
        from_msg = F.hesc(F.unquote(data.get("msg"))).replace("\n", "<br>")

        # from_name = "jane"
        # from_email = "jane@mark.com"
        # from_msg = "hello, my message"


        # self.jug.config['MAIL_SERVER']       = 'mail.paperdrift.com'
        self.jug.config['MAIL_SERVER']         = G.api["mail.smtp"]
        self.jug.config['MAIL_PORT']           = G.api["mail.port"]
        self.jug.config['MAIL_USE_TLS']        = True
        self.jug.config['MAIL_USE_SSL']        = False
        self.jug.config['MAIL_USERNAME']       = G.api["mail.username"]
        self.jug.config['MAIL_PASSWORD']       = G.api["mail.password"]
        self.jug.config['MAIL_DEFAULT_SENDER'] = G.contact["email"]

        # self.jug.config['MAIL_DEBUG: bool'] = app.debug
        # self.jug.config['MAIL_MAX_EMAILS'] = : int | None = None
        # self.jug.config['MAIL_SUPPRESS_SEND'] = : bool = app.testing
          # If the setting TESTING is set to True, emails will be suppressed.
          # Calling Message.send() will not result in any messages being actually sent.
        # self.jug.config['MAIL_ASCII_ATTACHMENTS'] = : bool = False
        # flask_mail.Message(subject='', recipients=None, body=None, sender=None, cc=None, bcc=None, reply_to=None, date=None, charset=None, extra_headers=None, mail_options=None, rcpt_options=None)



        mail = Mail(self.jug)
        # mail = Mail()
        # mail.init_app(self.jug)


        msg = Message(
          subject="Contact Us //inkonpages.com",
          sender=(G.contact["email_name"], G.contact["email"]),
          recipients=[ G.contact["email"] ]
        )

        # msg.recipients = ['hello@inkonpages.com']
        # msg.body =

        sender_ip = G.sys["remote_ip"]
        timestamp = F.getDateTime()
        # timezone = "America/LA"
        timezone = F.get_timezone()

        # https://whatismyipaddress.com/ip/{sender_ip}
        # json: https://api.iplocation.net/?ip=84.239.5.12
        # https://www.ip2location.com/demo/84.239.5.12
        ip_lookup_iplocation = f"https://www.iplocation.net/ip-lookup/{sender_ip}"
        ip_lookup_what_is = f"https://whatismyipaddress.com/ip/{sender_ip}"
        ip_lookup_utrace = f"http://en.utrace.de/?query={sender_ip}"
        ip_lookup_keycdn = f"https://tools.keycdn.com/geo?host={sender_ip}"

        head = "<head><meta http-equiv='content-type' content='text/html; charset=UTF-8'></head>"

        html_body = f"Sender Name: {from_name}<br>\
        Sender Email: {from_email}<br>\
        Sender IP: sender_ip | Lookup:\
        <a href='{ip_lookup_iplocation}'>iplocation</a>, \
        <a href='{ip_lookup_what_is}'>whatismyipaddress</a>, \
        <a href='{ip_lookup_keycdn}'>keycdn</a>, \
        <a href='{ip_lookup_utrace}'>utrace</a><br>\
        Timestamp: {timestamp} [{timezone}]<br>\
        <br>\
        <u>Message:</u><br>\
        {from_msg}"

        # msg.body = f"<html>{head}<body> {html_body} </body></html>"
          # Non-html mail


        # msg.html =f"<!DOCTYPE HTML><html lang='eng'><head><meta charset='UTF-8'></head><body> {html_body} </body></html>"
        # msg.html = f"<html lang='en'><body> {html_body} </body></html>"
        # msg.html = f"<html>{head}<body> {html_body} </body></html>"
        msg.html = html_body

        ###
          # msg = Message(
          #   subject="Contact Us //inkonpages.com",
          #   sender=("hello ౾inkonpages", "hello@inkonpages.com"),
          #   recipients=['hello@inkonpages.com'],
          #   body='This is a test email sent from Flask-Mail!'
          # )

          # msg.recipients = ["you@example.com"]
          # msg.add_recipient("somebodyelse@example.com")
          # msg.body = "testing"
          # msg.html = "<b>testing</b>"
          # msg.html = """
          # <html>
          #     <body>
          #         <p>Here is an embedded image:</p>
          #         <img src="cid:image1">
          #     </body>
          # </html>
          # """

          # # attachments:
          # with app.open_resource("image.png") as fp:
          #      msg.attach("image.png", "image/png", fp.read())
            # Open a resource file relative to root_path for reading.
            # For example, if the file schema.sql is next to the file app.py where the Flask app is defined, it can be opened with above;
          # Can also open the file with python's native open:
          # with open("invoice.pdf", "rb") as fp:
          #   msg.attach("invoice.pdf", "application/pdf", fp.read())


        try:
            mail.send(msg)
        except Exception as e:
            logger.debug(f'email send fail: {e}')
            return "bad"

        return "ok"

        ###
          # Batch sending
          # with mail.connect() as conn:
          #     for user in users:
          #         msg = Message(
          #             subject=f"hello, {user.name}",
          #             body="...",
          #             recipients=[user.email],
          #         )
          #         conn.send(msg)


