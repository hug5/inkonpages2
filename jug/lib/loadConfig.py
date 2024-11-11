from jug.lib.logger import logger

from flask import request

from jug.lib.fLib import F
from jug.lib.gLib import G

def loadConfig_toml():

    try:

        config_toml = F.load_file("config.toml")


        G.sys["remote_ip"] = request.environ['REMOTE_ADDR']

        G.site["baseUrl"] = config_toml["site"]["baseUrl"]
        G.site["name"] = config_toml["site"]["name"]
        G.site["tagline"] = config_toml["site"]["tagline"]
        G.site["logo_title"] = config_toml["site"]["logo_title"]
        G.site["description"] = config_toml["site"]["description"]
        G.site["keywords"] = config_toml["site"]["keywords"]
        G.site["secret_key"] = config_toml["site"]["secret_key"]

        G.site["time_zone"] = config_toml["site"]["time_zone"]
        G.site["time_zone_name"] = config_toml["site"]["time_zone_name"]
        G.site["time_zone_mail"] = config_toml["site"]["time_zone_mail"]
        G.site["time_zone_mail_name"] = config_toml["site"]["time_zone_mail_name"]
        # G.site["book_url"] = config_toml["site"]["book_url"]


        G.contact["email"] = config_toml["contact"]["email"]
        G.contact["email_name"] = config_toml["contact"]["email_name"]
        G.contact["bounce_email"] = config_toml["contact"]["bounce_email"]
        G.contact["contact_us_subject"] = config_toml["contact"]["contact_us_subject"]


        G.db["un"] = config_toml["db"]["un"]
        G.db["pw"] = config_toml["db"]["pw"]
        G.db["host"] = config_toml["db"]["host"]
        G.db["port"] = config_toml["db"]["port"]
        G.db["database"] = config_toml["db"]["database"]

        G.api["mail.smtp"] = config_toml["api"]["mail.smtp"]
        G.api["mail.port"] = config_toml["api"]["mail.port"]
        G.api["mail.username"] = config_toml["api"]["mail.username"]
        G.api["mail.password"] = config_toml["api"]["mail.password"]


    except Exception as e:
        logger.exception(f"setConfig_toml Error: {e}")
    finally:
        pass
