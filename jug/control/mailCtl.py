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
        from_name = data.get("name")
        from_email = data.get("email")
        from_msg = data.get("msg").replace("\n", "<br>")

        # from_name = parse.unquote_plus(data.get("name"))
        # from_email = parse.unquote_plus(data.get("email"))
        # from_msg = parse.unquote_plus(data.get("msg"))

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

        sender_ip = "838423423"
        timestamp = F.getDateTime()
        # timezone = "America/LA"
        timezone = F.get_timezone()

        html_body = f"Sender Name: {from_name} <br>Sender Email: {from_email} <br>Sender IP: {sender_ip} <br>Timestamp: {timestamp}, {timezone} <br>Message: {from_msg}"

        # msg.html =f"<!DOCTYPE HTML><html lang='eng'><head><meta charset='UTF-8'></head><body> {html_body} </body></html>"
        msg.html =f"<html lang='en'><body> {html_body} </body></html>"


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

        # Batch sending
        # with mail.connect() as conn:
        #     for user in users:
        #         msg = Message(
        #             subject=f"hello, {user.name}",
        #             body="...",
        #             recipients=[user.email],
        #         )
        #         conn.send(msg)



        #------------------------------------------------------------
        # $arr =  F::json("config-admin", "mail_settings");

        # $arr["subject"] = "Contact Message: " . "$from_name/$from_email";

        # // from and to are same; sending to ourselves
        # $arr["from_email"] = [
        #     "address" => $to_email,
        #     "name"    => "Contact Page/" . $to_email_name,
        #     "bounce"  => $bounce_email
        # ];

        # $arr["to_email"] = ["address" => [$to_email => $to_email_name]];


        # $userIp     = G::$oIP;
        # $timestamp  = date("D, M j, Y, g:ia", time());
        # $timeZone   = F::json("config", "timeZoneName");


        # $body =
        #     "<!DOCTYPE HTML><html><body style=\"font-size:15px;\">" .
        #         "Sender Name: $from_name" .
        #         "<br>Sender Email: $from_email" .
        #         "<br>Sender IP: $userIp" .
        #         "<br>Timestamp: $timestamp, $timeZone" .
        #         "<br><a href=\"http://en.utrace.de/?query=$userIp\">IP Lookup - utrace</a>" .
        #         "<br><a href=\"http://whatismyipaddress.com/ip/$userIp\">IP Lookup - What's my IP</a>" .
        #         "<br><br>. . . . . . . . . . . . . . . . . . . . . .<br><br>" .
        #         nl2br($msg1) .
        #     "</body></html>";


        # $arr["body"] = ["message" => $body];

        # // get back # email sent; if zero, then error
        # $result = $this->callMailRouter($arr);

        # echo $result ? "ok" : "bad";

