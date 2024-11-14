from jug.lib.logger import logger

from flask import redirect, request, jsonify, session
                # , make_response, render_template

from jug.lib.fLib import F
from jug.lib.gLib import G

# from pathlib import Path
# import tomli
# import re
# from urllib import parse
from jug.control.pageCtl import PageCtl
from jug.lib import configLoad


class RouterCtl():

    def __init__(self, jug):
        self.jug = jug

        logger.info('==== Begin RouterCtl __init__ ===')


    def init_conf(self):

        logger.info('---init_conf')

        # init variables:

        self.response_obj = None
        # self.redirect = [False, '']
        # self.setConfig_toml()

        # load config toml file into G var
        configLoad.configLoad_toml()

        # This makes the session last as per PERMANENT_SESSION_LIFETIME
        session.permanent = True
        session["user"] = "Phoebe"  # Some misc user

        # session["location"] = ["los angeles", "fresno"]
        # session.pop('username', None)
        # if "user" in session:                         # user in session
        # user = session["user"]
        # session["user"] = user                      # init session


        # G.sys["debug"] = False
        # if self.jug.debug:
        #     logger.info('---RUNNING DEBUG MODE')
        #     G.sys["debug"] = True
        # I don't even know what debug mode does!!

    def getResponse_obj(self):
        return self.response_obj

    # def setConfig_toml(self):
        # try:
        #     # config_toml_path = Path("jug/conf/config.toml")
        #     # if not Path(config_toml_path).is_file():
        #     #     raise FileNotFoundError(f"File Not Found: {config_toml_path}.")

        #     # with config_toml_path.open(mode='rb') as file_toml:
        #     #     config_toml = tomli.load(file_toml)
        #     #     # If bad, should give FileNotFoundError

        #     # config_toml = F.load_config_toml()
        #     config_toml = F.load_file("config.toml")

        #     G.site["baseUrl"] = config_toml["site"]["baseUrl"]
        #     G.site["name"] = config_toml["site"]["name"]
        #     G.site["tagline"] = config_toml["site"]["tagline"]
        #     G.site["logo_title"] = config_toml["site"]["logo_title"]
        #     G.site["description"] = config_toml["site"]["description"]
        #     G.site["keywords"] = config_toml["site"]["keywords"]
        #     G.site["secret_key"] = config_toml["site"]["secret_key"]

        #     G.site["time_zone"] = config_toml["site"]["time_zone"]
        #     G.site["time_zone_name"] = config_toml["site"]["time_zone_name"]
        #     G.site["time_zone_mail"] = config_toml["site"]["time_zone_mail"]
        #     G.site["time_zone_mail_name"] = config_toml["site"]["time_zone_mail_name"]
        #     # G.site["book_url"] = config_toml["site"]["book_url"]


        #     G.contact["email"] = config_toml["contact"]["email"]
        #     G.contact["email_name"] = config_toml["contact"]["email_name"]
        #     G.contact["bounce_email"] = config_toml["contact"]["bounce_email"]

        #     G.db["un"] = config_toml["db"]["un"]
        #     G.db["pw"] = config_toml["db"]["pw"]
        #     G.db["host"] = config_toml["db"]["host"]
        #     G.db["port"] = config_toml["db"]["port"]
        #     G.db["database"] = config_toml["db"]["database"]

        #     G.api["mailgun.smtp"] = config_toml["api"]["mailgun.smtp"]
        #     G.api["mailgun.port"] = config_toml["api"]["mailgun.port"]
        #     G.api["mailgun.username"] = config_toml["api"]["mailgun.username"]
        #     G.api["mailgun.password"] = config_toml["api"]["mailgun.password"]


        # except Exception as e:
        #     logger.exception(f"setConfig_toml Error: {e}")
        # finally:
        #     pass




    # def cleanUrl(self, url):
        # url2 = parse.unquote_plus(url)
        # url3 = (url2.replace('[', '').replace(']', '').replace('{', '')
        #         .replace('}', '').replace('', '').replace('<', '').replace('>', '')
        #         .replace('?', '').replace('@', '').replace('*', '').replace('~', '')
        #         .replace('!', '').replace('#', '').replace('$', '').replace('%', '')
        #         .replace('^', '').replace('&', '').replace('(', '').replace(')', '')
        #         .replace(',', '').replace(';', '').replace('+', '').replace('.', ''))
        #         # Wrap with parenthesis to break up lines;

        # url4 = ' '.join(url3.split())

        # url5 = parse.quote_plus(url4, safe="/", encoding="utf-8", errors='replace')

        # # Return clean url with slashes
        # return f'/{url5}/'



    def doRequestUrl(self):
        # Assume this url:
        # https://station.paperdrift.com/something/?a=b

        rpath = request.url_root
        logger.info("---URL url_root: " + rpath)
        # root.info("---URL url_root: " + rpath)
          # https://station.paperdrift.com/

        rpath = request.base_url
        logger.info("---URL base_url: " + rpath)
        # root.info("---URL base_url: " + rpath)
            # https://station.paperdrift.com/something/

        rpath = request.url
        logger.info("---URL url: " + rpath)
        # root.info("---URL url: " + rpath)
          # https://station.paperdrift.com/something/?a=b

        rpath = request.full_path
        logger.info("---URL full_path: " + rpath)
        # root.info("---URL full_path: " + rpath)
          # /something/?a=b
          # /?   # will always have a ? on the index or other page ERRONESOUSLY;

        rpath = request.environ['PATH_INFO']
        logger.info("---URL PATH_INFO: " + rpath)
        # root.info("---URL PATH_INFO: " + rpath)
            # /something/

        rpath = request.environ['QUERY_STRING']
        logger.info("---URL QUERY_STRING: " + rpath)
        # root.info("---URL QUERY_STRING: " + rpath)
          # a=b

        # These below give me the same IP address
        # rpath = request.remote_addr
        rpath = request.environ['REMOTE_ADDR']
        logger.info("---Remote Address2: " + rpath)
        # root.info("---Remote Address2: " + rpath)
          # 84.239.5.141


        # This gives us the TRUE RAW uri; ? and // are always shown
        rpath = request.environ["REQUEST_URI"]
        G.sys["req_uri"] = rpath
        logger.info("---uri: " + rpath)
        # root.info("---uri: " + rpath)
          # /something/?a=b

        # print everything; check uwsgi_log
        # print(request.environ)

        # Also:
        # logger.debug, logger.info, logger.warning, logger.error, logger.critical

    def doRest(self, url):

        from jug.control.restCtl import RestCtl

        # logger.info("---rest")
        # request_data = request.get_json()
        # logger.info("---ajax POST22")

        rest_obj = RestCtl(url)
        rest_obj.doRest()
        result = rest_obj.getResult()
        try:
            self.response_obj = jsonify(result)
        except Exception as e:
            logger.info(f'---jsonify exception: {e}')


    # def doAjax(self, param):
    def doAjax(self):
        from jug.control.ajaxCtl import AjaxCtl

        logger.info("---ajax")
        request_data = request.get_json()
        logger.info("---ajax 22")

        # ajax_obj = AjaxCtl(self.jug, request_data)
        ajax_obj = AjaxCtl(request_data)
        ajax_obj.doAjax()
        result = ajax_obj.getResult()

        try:
            self.response_obj = jsonify(result)
        except Exception as e:
            logger.info(f'---jsonify exception: {e}')

        # logger.info(f'---response object (2): {self.response_obj}')

    def doPage(self, page):
        page_obj = PageCtl()
        page_obj.doPage(page)
        self.response_obj = page_obj.getHtml()


    def doResponse_obj(self):

        logger.info(f'---response_obj: {G.sys.get("abort")}')

        if not G.sys.get("abort"):
            # logger.debug(f"---self.response_obj type: {type(self.response_obj)}")
              # <class 'flask.wrappers.Response'>
            return self.response_obj

        if G.sys["abort"].get("type") == "redirect":
            logger.info(f'--redirecting: {G.sys["abort"].get("redirect")}')
            return redirect(G.sys["abort"].get("redirect"), code=301)

        if G.sys["abort"].get("type") == "404":
            # do 404 page
            # return make_response("404", 404)
            # return make_response(render_template("404.html"), 404)
            # return make_response(render_template("404Html.jinja"), 404)
            return "404"

        return "404X"


    def doRoute(self):

        @self.jug.before_request
        def before_request_route():
            # logger.info("---doRoute: before_request---")
            G.init() # Reset global variable;
            # self.doBeforeRequest()
            self.init_conf()
            self.doRequestUrl()


        @self.jug.route('/<path:url>/')  # Catchall for anything else
        @self.jug.route("/")
        def home(url=''):
            logger.info("---in home")
            # G.sys["X"] = "hello"
            # logger.info(f"---Showing X: {G.sys.get('X')}")
            self.doPage("home")
            return self.doResponse_obj()

        @self.jug.route('/contact/')
        @self.jug.route('/contact/<path:url>/') # The slash seems to always add a slash to the end, regardless
        def contact(url=''):
            logger.info("---in contact")
            # logger.info(f"---Showing X: {G.sys.get('X')}")
            self.doPage("contact")
            return self.doResponse_obj()

        @self.jug.route('/rank/<path:url>/')
        def rank(url=''):
            logger.info("---in rank")
            self.doPage("rank")
            return self.doResponse_obj()

        # @self.jug.route('/ajax/', methods=['GET', 'POST'])
        @self.jug.route('/ajax/', methods=['POST'])
        def ajax():
            logger.info("---in ajax")
            # self.doAjax(request.method)
            self.doAjax()
            return self.doResponse_obj()

        @self.jug.route('/rest/<path:url>/', methods=['GET', 'POST'])
        @self.jug.route('/rest/', methods=['GET', 'POST'])
        def rest(url=''):
            logger.info("---in rest_call")
            # return jsonify({"res": "ok"})
            # return make_response('', 204)
            self.doRest(url)
            return self.doResponse_obj()






        # @self.jug.route('/favicon.ico')
        # def favicon():
        #     return make_response('', 204)

        # @self.jug.route('/<path:url>/')
        # def locationUrl(url):
        #     logger.info(f"---in path: {url}")
        #     self.doLocationUrl(url)
        #     return self.doResponse_obj()

        # # @self.jug.route('/<path:url>/<path:url2>/')
        # # def locationUrl2(url, url2):
        # #     logger.info("---in path url2")
        # #     self.redirect = [True, f"/{url}/"]
        # #     return self.doResponse_obj()


        # # @self.jug.route('/ajax/', methods=['GET', 'POST'])
        # @self.jug.route('/ajax/', methods=['POST'])
        # def ajaxPost():
        #     logger.info("---in path: ajax")
        #     # self.doAjax(request.method)
        #     self.doAjaxPost()
        #     return self.doResponse_obj()


        # @self.jug.after_request
        # def after_request_route(response_object):
        #     # Reset this!
        #     # self.redirect = ["False", '']
        #     logger.info("---after_request")
        #     # takes a response object and must return a response object; what is a response object?
        #     return response_object

        @self.jug.teardown_request
        def show_teardown(exception):
            G.init()
            logger.info(f'---G Global Vars: [{G.sys}] [{G.db}] [{G.site}] [{G.contact}]')
            logger.info("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
            logger.info("░░░░░░░░░░  teardown  ░░░░░░░░░░░")
            logger.info("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")




    # def doRoutexx(self):

        # @self.jug.before_request
        # def before_request_route():
        #     logger.info("---doRoute: before_request---")
        #     self.doBeforeRequest()

        # @self.jug.route('/')
        # def home():
        #     logger.info("---in home")
        #     self.doHome()
        #     return self.doResponse_obj()


        # @self.jug.route('/contact/')
        # @self.jug.route('/contact/<path:url>')
        # def contact(url=""):
        #     if url:
        #         return redirect("/contact/", code=301)
        #     return "contact"


        # @self.jug.route('/rank/')
        # @self.jug.route('/rank/bestseller/')
        # def rank_bad():
        #     return "rank bad"

        # @self.jug.route('/rank/bestseller/fiction/')
        # @self.jug.route('/rank/alltime/')
        # def rank_good():
        #     return "rank good"


        # @self.jug.route('/<path:url>')
        # def bad_url(url):
        #     return redirect("/", code=301)

        #  # @self.jug.route('/ajax/', methods=['GET', 'POST'])
        # @self.jug.route('/ajax/', methods=['POST'])
        # def ajaxPost():
        #     logger.info("---in path: ajax")
        #     self.doAjaxPost()
        #     return self.doResponse_obj()

        # @self.jug.after_request
        # def after_request_route(response_object):
        #     # Reset this!
        #     # self.redirect = ["False", '']
        #     logger.info("---after_request")
        #     # takes a response object and must return a response object; what is a response object?
        #     return response_object


        # @self.jug.teardown_request
        # def show_teardown(exception):
        #     logger.info("##################################")
        #     logger.info("############ teardown ############")
        #     logger.info("##################################")
        #     # Not sure what teardown does;





      # https://inkonpages.com/rank/bestseller/fiction/

        # @self.jug.route('/<path:url>')
        # def contact(url):

        #     # If return some value, then go to that given url
        #     # If return False, then the url is fine;
        #     result = self.doCheckBadPath(url)
        #     # So a good path will return False; anything else is bad path;
        #     # And we should redirect to the return value;
        #     if result: return redirect(result, code=301)

        #     # If path is good, then proceed normally;
        #     return self.doSomePathUrl(url)

        # https://inkonpages.com/rank/bestseller/fiction/
        # https://inkonpages.com/rank/bestseller/nonfiction/
        # https://inkonpages.com/rank/alltime/
        # https://inkonpages.com/contact/

        # @self.jug.route('/<path:url>')

        # path             /foo/page.html
        # full_path        /foo/page.html?x=y
        # script_root      /myapplication

        # url_root         http://www.example.com/myapplication/
        # base_url         http://www.example.com/myapplication/foo/page.html
        # url              http://www.example.com/myapplication/foo/page.html?x=y



## These below don't work even when it appears to!
# method 1
# obj = Router()
# jug = obj.start()

# method 2
# jug = Router().start()
  # Can just shorten to 1 line like this;

# These 2 may be equivalent and allows for debug mode
# $ flask --app hello run --debug
# app.run(debug=True)

# But how to do this on a running remote server running uwsgi?

