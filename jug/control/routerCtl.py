from jug.lib.logger import logger

from flask import redirect, request, jsonify, session
#, make_response

from jug.lib.fLib import F
from jug.lib.gLib import G
# from pathlib import Path
# import tomli
# import re
from urllib import parse
from jug.control.pageCtl import PageCtl


class RouterCtl():

    def __init__(self, jug):
        self.jug = jug
        logger.info('==== Begin RouterCtl __init__ ===')


    def router_init(self):
        logger.info('---router_init---')

        self.response_obj = None
        self.redirect = [False, '']
        logger.info(f'---In G BEFORE?: [{G.api}][{G.db}][{G.site}]')
        G.reset()
        logger.info(f'---In G AFTER?: [{G.api}][{G.db}][{G.site}]')

        self.setConfig_toml()


        # This makes the session last as per PERMANENT_SESSION_LIFETIME
        session.permanent = True

        session["user"] = "Phoebe"

        if not session.get("location"):
            session["location"] = []



        # session["location"] = ["los angeles", "fresno"]
        # session.pop('username', None)
        # if "user" in session:                         # user in session
        # user = session["user"]
        # session["user"] = user                      # init session

        G.debug = False
        if self.jug.debug:
            logger.info('---RUNNING DEBUG MODE')
            G.debug = True

    def getResponse_obj(self):
        return self.response_obj

    def setConfig_toml(self):

        try:
            # config_toml_path = Path("jug/conf/config.toml")
            # if not Path(config_toml_path).is_file():
            #     raise FileNotFoundError(f"File Not Found: {config_toml_path}.")

            # with config_toml_path.open(mode='rb') as file_toml:
            #     config_toml = tomli.load(file_toml)
            #     # If bad, should give FileNotFoundError


            config_toml = F.load_config_toml()

            G.api["weatherAPI_key"] = config_toml.get("api", {}).get("weatherAPI_key")
            G.api["weatherAPI_url"] = config_toml.get("api", {}).get("weatherAPI_url")

            G.db["un"] = config_toml["db"]["un"]
            G.db["pw"] = config_toml["db"]["pw"]
            G.db["host"] = config_toml["db"]["host"]
            G.db["port"] = config_toml["db"]["port"]
            G.db["database"] = config_toml["db"]["database"]

            G.site["secret_key"] = config_toml["site"]["secret_key"]
            G.site["name"] = config_toml["site"]["name"]
            G.site["tagline"] = config_toml["site"]["tagline"]
            G.site["keywords"] = config_toml["site"]["keywords"]
            G.site["baseUrl"] = config_toml["site"]["baseUrl"]

        except Exception as e:
            logger.exception(f"setConfig_toml Error: {e}")
        finally:
            pass
            # logger.info(f'weatherAPI_key: {G["weatherAPI_key"]}')
            # logger.info(f'weatherAPI_key: {G.api["weatherAPI_key"]}')
            # logger.info(f'Anything in G AFTER?: [{G.api}][{G.db}][{G.site}]')

    def doCommon(self):
        from jug.control.headerCtl import HeaderCtl
        from jug.control.footerCtl import FooterCtl

        logger.info('doCommon')

        cfDict = {
            "base_url" : request.url_root,
            "bestseller_url" : "/rank/bestseller/fiction/",
            "contact_url" : "/contact/",
            "link" : "https://hmso.inkonpages.com/book/theswines/"
        }

        # do Header
        headerOb = HeaderCtl()
        headerOb.start(cfDict)
        self.header = headerOb.getHtml()

        # do Footer
        footerOb = FooterCtl()
        footerOb.start(cfDict)
        self.footer = footerOb.getHtml()


        # pass


    def doHome(self):
        from jug.control.homeCtl import HomeCtl
        logger.info('DoHome')

        self.doCommon()

        homeOb = HomeCtl()
        homeOb.start()
        self.article = homeOb.getHtml()

        site_title = homeOb.getConfig()["site_title"]

        base_url = request.url_root

        pageHtml = render_template(
            "pageHtml.jinja",
            title = site_title,
            header = self.header,
            article = self.article,
            footer = self.footer,
            base_url = base_url
        )

        # return F.stripJinjaWhiteSpace(pageHtml)
        return pageHtml


    def doRequestUrl(self):
        # Assume this url:
        # https://station.paperdrift.com/something/?a=b

        rpath = request.url_root
        logger.info("---URL url_root: " + rpath)
          # https://station.paperdrift.com/

        rpath = request.base_url
        logger.info("---URL base_url: " + rpath)
            # https://station.paperdrift.com/something/

        rpath = request.url
        logger.info("---URL url: " + rpath)
          # https://station.paperdrift.com/something/?a=b

        rpath = request.full_path
        logger.info("---URL full_path: " + rpath)
          # /something/?a=b
          # /?   # will always have a ? on the index or other page ERRONESOUSLY;

        rpath = request.environ['PATH_INFO']
        logger.info("---URL PATH_INFO: " + rpath)
            # /something/

        rpath = request.environ['QUERY_STRING']
        logger.info("---URL QUERY_STRING: " + rpath)
          # a=b

        # These below give me the same IP address
        # rpath = request.remote_addr
        # logger.info("---Remote Address: " + rpath)
          # 84.239.5.141
        rpath = request.environ['REMOTE_ADDR']
        logger.info("---Remote Address2: " + rpath)
          # 84.239.5.141


        # This gives us the TRUE RAW uri; ? and // are always shown
        rpath = request.environ["REQUEST_URI"]
        logger.info("---uri: " + rpath)
          # /something/?a=b

        # print everything; check uwsgi_log
        # print(request.environ)

        # Also:
        # logger.debug, logger.info, logger.warning, logger.error, logger.critical


    def doRoute(self, sender=True):
        # Using True/False to denote whether we want to return a result to close out; or whether this is just an intermediary check;

        if self.redirect[0] is True:
            logger.info(f'--redirecting: {self.redirect[1]}')
            return redirect(self.redirect[1], code=301)

        if sender is True:
            # resp = make_response(self.response_obj)
            # resp.set_cookie('paper', '1234', samesite='Lax', secure=True)
            # resp.set_cookie('rock', '1234', samesite='Lax', secure=True, max_age=7776000)
            # resp.set_cookie('scissor', '1234')
            resp = self.response_obj
            return resp

            # return self.getResponse_obj()
            # if here, then will implicitly return None

            # const jsonData = { name: "John", age: 32 };
            # document.cookie = "userData=" + encodeURIComponent(JSON.stringify(jsonData));
            # const cookies = document.cookie.split('; ');
            # const userDataCookie = cookies.find(row => row.startsWith('userData='));
            # const userData = userDataCookie ? JSON.parse(decodeURIComponent(userDataCookie.split('=')[1])) : null;


    def doBeforeRequest(self):
        logger.info("---doBeforeRequest: Start")

        self.doRequestUrl()
        self.router_init()
        self.checkUrl()
        logger.info("---doBeforeRequest: Finished")


    def parseRoute(self):

        @self.jug.before_request
        def before_request_route():
            logger.info("---parseRoute: before_request---")
            self.doBeforeRequest()

        @self.jug.route('/')
        def home():
            logger.info("---in home")
            self.doHome()
            return self.doRoute()


        @self.jug.route('/contact/')
        @self.jug.route('/contact/<path:url>')
        def contact(url=""):
            if url:
                return redirect("/contact/", code=301)
            return "contact"


        @self.jug.route('/rank/')
        @self.jug.route('/rank/bestseller/')
        def rank_bad():
            return "rank bad"

        @self.jug.route('/rank/bestseller/fiction/')
        @self.jug.route('/rank/alltime/')
        def rank_good():
            return "rank good"


        @self.jug.route('/<path:url>')
        def bad_url(url):
            return redirect("/", code=301)

         # @self.jug.route('/ajax/', methods=['GET', 'POST'])
        @self.jug.route('/ajax/', methods=['POST'])
        def ajaxPost():
            logger.info("---in path: ajax")
            self.doAjaxPost()
            return self.doRoute()

        @self.jug.after_request
        def after_request_route(response_object):
            # Reset this!
            # self.redirect = ["False", '']
            logger.info("---after_request")
            # takes a response object and must return a response object; what is a response object?
            return response_object


        @self.jug.teardown_request
        def show_teardown(exception):
            logger.info("##################################")
            logger.info("############ teardown ############")
            logger.info("##################################")
            # Not sure what teardown does;





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

