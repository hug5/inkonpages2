from jug.lib.logger import logger

# from flask import redirect, request, jsonify, session
#, make_response
from jug.lib.fLib import F
from jug.lib.gLib import G
from flask_mail import Mail, Message


class MailCtl():
    """ // 2024-11-10
        This is the flask-mail implementation of mail;
        However, not suing because it fails dkim on long messages;
        Note: Remember that using flask-mail requires that you pass
        the flask object or self.jug in;
    """

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
        from_msg = F.hesc(F.unquote(data.get("msg"))).replace("\n", "<br> ")
          # Add extra space with <br> to prevent possible split of that word!

        # from_msg1 = F.hesc(F.unquote(data.get("msg")))
        # from_msg2 = from_msg1.replace("\n", "br2222")
        # from_msg = from_msg2.replace("br2222", "\n<br> ")


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


        mail = Mail(self.jug)
        # mail = Mail()
        # mail.init_app(self.jug)


        msg = Message(
          subject = G.contact["contact_us_subject"],
          sender = (G.contact["email_name"], G.contact["email"]),
          recipients = [ G.contact["email"] ]
        )

        # flask_mail.Message(
          #   subject='',
          #   recipients=None,
          #   body=None,
          #   sender=None,
          #   cc=None,
          #   bcc=None,
          #   reply_to=None,
          #   date=None,
          #   charset=None,
          #   extra_headers=None,
          #   mail_options=None,
          #   rcpt_options=None
          # )

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

        style = "<style>p{margin:2px 0 4px 0;}#info{width:fit-content;padding-bottom:15px;border-bottom:1px solid #CACACA;}.shade{background-color:#E1E1E1;border:1px solid #C2C2C2;padding:0 7px 0 7px;margin-left:5px;border-radius:5px;}#message1{margin-top:20px;}</style>"
        # extra_headers take a dictionary:
        head = f"<head><meta http-equiv='content-type' content='text/html; charset=UTF-8'> {style}</head>"
        # doctype = "<!DOCTYPE HTML>"

        msg.extra_headers = {
          'X-Engine': 'hypersonic',
          # email already has message-ID and date; creates duplicate;
          # and double date causes rejection by email providers;
          # 'Message-ID' : F.get_uuid("email"),
            # Flask inserts its own message ID
            # <173129931671.13507.3147714171779463197@digbase.dev>
            # Can't seem to change it;
          # 'Date' : F.getDateTime("email")
        }

        html_body = F.stripJinja( f"<div id='info'>\
          <p>Sender Name: {from_name}</p>\
          <p>Sender Email: {from_email}</p>\
          <p>Sender IP: {sender_ip} \
            <span class='shade'><a href='{ip_lookup_iplocation}'>iplocation</a></span>\
            <span class='shade'><a href='{ip_lookup_what_is}'>whatismyipaddress</a></span>\
            <span class='shade'><a href='{ip_lookup_keycdn}'>keycdn</a></span>\
            <span class='shade'><a href='{ip_lookup_utrace}'>utrace</a></span></p>\
          <p>Timestamp: {timestamp} [{timezone}]</p></div>\
          <div id='message1'>{from_msg}</div>" )

        # msg.html = f"{doctype}<html lang='en'>\n{head}\n<body>\n{html_body}\n</body>\n</html>"
        # msg.html = f"<html>\n{head}\n<body>\n{html_body}\n</body>\n</html>"
        msg.html = f"<html>{head}<body>{html_body}</body></html>"


        try:
            mail.send(msg)
        except Exception as e:
            logger.debug(f'email send fail: {e}')
            return "bad"

        return "ok"


# // 2024-11-10 Sun 20:44
# At any rate, the problem with flask-mail is that dkim fails with long message bodies!
# Use a few paragraphs and it fails;
# not sure if it's usuble;
# But the problem with smtplib is that it always sends anything more than trivial as base64!!
# It will not send as 7 or 8bit, which is what most emails for encoding;
