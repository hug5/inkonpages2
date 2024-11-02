# from flask import Flask
# from flask import flask
# import html
# from flask import redirect
# from markupsafe import Markup, escape
from jug.lib.logger import logger

from markupsafe import escape
import random
import os
import tomli
from pathlib import Path
from datetime import datetime
from jug.lib.gLib import G


class F():

    @staticmethod
    def getUriList():
    # return the page url
        req_uri = G.sys["req_uri"]
        return req_uri.split("/")

    @staticmethod
    def getDateTime(param="basic"):

        now = datetime.now()

        # 2024-11-23 16:13, Mon
        if param == "basic_dow":
            dt_string = now.strftime("%Y-%m-%d %H:%M, %a")

        # 2024-11-23 04:13 PM, Mon
        elif param == "basic2_dow":
            dt_string = now.strftime("%Y-%m-%d %I:%M %p, %a")

        # 2024-11-23 16:13
        else:
            # if param == "basic":
            # datetime object containing current date and time
            dt_string = now.strftime("%Y-%m-%d %H:%M")


        # https://www.programiz.com/python-programming/datetime/strftime
        return dt_string

        # If you want to convert a given date to another kind of date:
        # x = datetime.strptime("2024-11-23 16:13", "%Y-%m-%d %H:%M")
        # Then run x strftime:
        # dt_string = x.strftime("%Y-%m-%d %I:%M %p, %a")


    @staticmethod
    def load_config_toml():

        try:
            config_toml_path = Path("jug/conf/config.toml")
            if not Path(config_toml_path).is_file():
                raise FileNotFoundError(f"File Not Found: {config_toml_path}.")

            with config_toml_path.open(mode='rb') as file_toml:
                config_toml = tomli.load(file_toml)

            return config_toml

        except FileNotFoundError as e:
            logger.exception(f"config.toml Load Error: {e}")
        except Exception as e:
            logger.exception(f"load_config_toml: {e}")
        finally:
            pass

        return {}


    @staticmethod
    def uwsgi_log(msg):
        # To use, you'd do:
        # F.uwsgi_log("Call HomeDb")

        # log_path = os.getcwd() + "/etc/log/uwsgi.log"
        log_path = os.getcwd() + "/etc/log/debug.log"
        # os.system("echo " + msg + " >> " + log_path)
        os.system(f"echo '--- {msg}' >> {log_path}")


    # escape("<script>alert(document.cookie);</script>")
    # Markup(u'&lt;script&gt;alert(document.cookie);&lt;/script&gt;')

    @staticmethod
    def checkPathSlash(url):
        # checks that url ends in slash

        # url2 = url.rstrip('/')  # right-strip;
            # This always makes sure there's no final slash;
        url2 = url.rstrip('/') + "/"
            # This makes usre there is always a final slash;
        if url2 != url:
            # return redirect('/' + url2, code=301)
            # return redirect('/' + url2, code=301)
                # The / makes the redirect at the root; otherwise, will just append the url;
            # return "here"
            # 301 /url2   # Not sure what this is about; doesn't seem to work;
            # if there's a / at url, then redirect to non-slash url;

            # raise redirect_to('/' + url2)

            return '/' + url2
            # return True

        return True

        # There doesn't seem to be a way to redirect directly from here; have to do a return; very lame!

    @staticmethod
    def stripJinja(html):
        # html = html.replace('\n', '').replace('   ', '').replace('  ', '')
        # # return html.replace('    ', '')
        # return html

        return ' '.join(html.split())
        # return ' '.join(html.split()).replace('> <', '><')
        # Split the string by white spaces and put into a list; then join back using ' ' (space)
        # Supposed to at most leave 1 white space;
        # Not perfect though; see white space between '> <', for instance;
        # Also note that we can use replace to make > < to ><,
        # but this will alter the css layout sometimes; This is a quandary;
        # I have not seen any noticeable difference between stripping (as I do above),
        # And not stripping; so maybe that's a good baseline to start with;

    @staticmethod
    def hesc(str):
        # result = flask.escape(str)
          # Not work
        # result = html.escape(str)
          # Works
        result = escape(str)
          # Works
        # return str
        return result

    @staticmethod
    def cd():
        import os
        cwd = os.getcwd()
        print(cwd)

