# from flask import Flask
# from flask import flask
# import html
# from flask import redirect
# from markupsafe import Markup, escape
from jug.lib.logger import logger

import random
import os
from pathlib import Path
from jug.lib.gLib import G
from urllib import parse

# from markupsafe import escape
import html
import uuid


class F():

    @staticmethod
    def abort(type, url=''):

        G.sys["abort"] = {
            "type" : type,    # redirect, 404
            "redirect" : url  # redirect url
        }

        # G.sys["abort"]["type"] = type
        # G.sys["abort"]["redirect"] = url
          # This syntax doesn't work

        # G.sys = {
        #     "abort" : {
        #         "type" : type,    # redirect, 404
        #         "redirect" : url  # redirect url
        #     }
        # }

    @staticmethod
    def get_uuid(utype=''):
        unique_uuid = str(uuid.uuid4())

        # If used for email, then include site name,
        # And formatted for use in email ID:
        if utype == "email":
            domain = G.site["name"].replace(" ", "-")
            return f"<{unique_uuid}@{domain}>"

        # Otherwise, just return the unique uuid string:
        return unique_uuid



    @staticmethod
    def unquote(str):
       return parse.unquote_plus(str)

    @staticmethod
    def getUriList():
    # return the page url
        req_uri = G.sys["req_uri"]
        return req_uri.split("/")


    @staticmethod
    def get_timezone():
        # Get server's time zone
        # Get timezone info from /etc/timezone file
        # eg: America/Los_Angeles

        try:
            with open('/etc/timezone', 'r') as file:
                timezone = file.read().strip()
                # Gets whole file
            return timezone
        except FileNotFoundError:
            return "/etc/timezone file not found."
        except Exception as e:
            return f"An error occurred: {e}"


    @staticmethod
    def getDateTime(format=""):

        # For email use:
        # Returns a date string as per RFC 2822, e.g.:
        # Fri, 09 Nov 2001 01:08:47 -0000
        if format == "email":
            from email.utils import formatdate
            return formatdate(localtime=True)


        from datetime import datetime
        now = datetime.now()

        # Tuesday, Nov. 12, 2024
        if format == "long1":
            return now.strftime("%A, %b. %d, %Y")

        # 2024-11-23 16:13, Mon (24hr  + dayofweek)
        if format == "24h":
            return now.strftime("%Y-%m-%d %H:%M, %a")

        # 2024-11-23 04:13 PM, Mon (12hr + dayofweek)
        if format == "12h":
            return now.strftime("%Y-%m-%d %I:%M %p, %a")

        # Default format:
        # 2024-11-23 16:13:16
        return now.strftime("%Y-%m-%d %H:%M:%S")


        # https://www.programiz.com/python-programming/datetime/strftime
        # return dt_string

        # If you want to convert a given date to another kind of date:
        # x = datetime.strptime("2024-11-23 16:13", "%Y-%m-%d %H:%M")
        # Then run x strftime:
        # dt_string = x.strftime("%Y-%m-%d %I:%M %p, %a")



    @staticmethod
    def load_config_toml():
        import tomli

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
    def load_file(file):
        # Generic load file
        import tomli
        import pathlib
        # Load a toml file

        try:
            # if file has no path, then assume it's a
            # conf file in the conf folder
            if file.find("/") < 0:
                file = f"jug/conf/{file}"

            # check if file exists;
            file_path = Path(file)
            if not Path(file_path).is_file():
                raise FileNotFoundError(f"File Not Found: {file_path}.")

            open_file = {}
            # get file extension
            file_extension = pathlib.Path(file_path).suffix
            if file_extension == ".toml":
                with file_path.open(mode='rb') as file_toml:
                    open_file = tomli.load(file_toml)
            else:
                pass

            return open_file

        except FileNotFoundError as e:
            logger.exception(f"{file} Load Error: {e}")
        except Exception as e:
            logger.exception(f"load_file Error: {e}")
        finally:
            pass

        # if error, return empty dict
        return {}

        # import pathlib
        # # function to return the file extension
        # file_extension = pathlib.Path('my_file.txt').suffix
        # print("File Extension: ", file_extension)

        # import pathlib
        # print(pathlib.Path('yourPath.example').suffix) # '.example'
        # print(pathlib.Path("hello/foo.bar.tar.gz").suffixes) # ['.bar', '.tar', '.gz']
        # print(pathlib.Path('/foo/bar.txt').stem) # 'bar'


        # >>> import os
        # >>> filename, file_extension = os.path.splitext('/path/to/somefile.ext')
        # >>> filename
        # '/path/to/somefile'
        # >>> file_extension
        # '.ext'



    @staticmethod
    def uwsgi_log(msg):
        # Write to the uwsgi log;
        # Can use, but not used anymore since using the logger module;
        # To use, do:
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

        # # Using markupsafe module
        # # result = flask.escape(str)
        #   # Not work
        # # result = html.escape(str)
        #   # Works
        # return escape(str)
        #   # Works

        # Using html module
        return html.escape(str)

        # Note: STrange behavior; with the markupsafe module, it seems to escape
        # characters that it shouldn't, ie, AFTER the escape was done;
        # It's like a ghost escaping in the FUTURE.


    @staticmethod
    def cd():
        import os
        cwd = os.getcwd()
        print(cwd)

