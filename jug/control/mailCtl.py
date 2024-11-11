from jug.lib.logger import logger

# from flask import redirect, request, jsonify, session
#, make_response
from jug.lib.fLib import F
from jug.lib.gLib import G
# from flask_mail import Mail, Message

import smtplib
from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.utils import formatdate
from email import encoders
import random

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
        from_msg = F.hesc(F.unquote(data.get("msg"))).replace("\n", "<br> ")
          # Add extra space with <br> to prevent possible split of that word!


        # Configuration
        port = G.api["mail.port"]
        smtp_server = G.api["mail.smtp"]
        login = G.api["mail.username"]
        password = G.api["mail.password"]

        sender_email = G.contact["email"]
        receiver_email = G.contact["email"]
        # receiver_email = "yooliganz@yahoo.com"

        # # self.jug.config['MAIL_SERVER']       = 'mail.paperdrift.com'
        # self.jug.config['MAIL_USE_TLS']        = True
        # self.jug.config['MAIL_USE_SSL']        = False
        # self.jug.config['MAIL_DEFAULT_SENDER'] = G.contact["email"]


        subject = "Contact Us //inkonpages.com"
        # html = from_msg


        # message = MIMEMultipart()
        # message["From"] = sender_email
        # message["To"] = receiver_email
        # message["Subject"] = subject


        #--------------------------------
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
        style = ''
        # extra_headers take a dictionary:
        head = f"<head><meta http-equiv='content-type' content='text/html; charset=UTF-8'> {style}</head>"
        # doctype = "<!DOCTYPE HTML>"


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


        msg_html = f"<html>{head}<body>{html_body}</body></html>"


        # Attach the HTML part
        # msg.attach(MIMEText(msg_html, "html"))
        # msg = MIMEText(msg_html, "html", "utf-8")
        # msg = MIMEText(msg_html, 'plain', 'us-ascii')
        # msg = MIMEText(msg_html, 'plain', 'utf-8)

        msg = MIMEText(msg_html, 'html', 'utf-8')
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject
        msg['Message-ID'] = F.get_uuid("email")
        msg['Date'] = F.getDateTime("email")
          # Returns a date string as per RFC 2822, e.g.:
          # Fri, 09 Nov 2001 01:08:47 -0000
          # Example: 'Fri, 10 Nov 2024 16:30:00 -0800'

        msg.add_header('X-engine', 'hypersonic')


        # message['Content-Transfer-Encoding'] = '8bit'
        # message.add_header('Content-Transfer-Encoding', '8bit')
        # message.add_header('Content-Type', 'text/html; charset=UTF-8')

        try:
          # Send the email
          with smtplib.SMTP(smtp_server, port) as server:
              server.starttls()
              server.login(login, password)
              server.sendmail(sender_email, receiver_email, message.as_string())

        except Exception as e:
            logger.debug(f'email send fail: {e}')
            return "bad"

        return "ok"

# ----------------------------------------------------------------
#
# Notes:
#
# msg.attach(MIMEText(text, 'plain'))
# msg.attach(MIMEText(html, 'html'))
# msg.add_header('Content-Transfer-Encoding', 'quoted-printable')  # or 'base64'
# msg.add_header('Content-Transfer-Encoding', '8bit')  # Set encoding to 8bit
# message.add_header('Content-Transfer-Encoding', '7bit')
# message.add_header('Content-Type', 'text/plain; charset=UTF-8')
# encoders.encode_7or8bit(message)

