class G():

    pool = None

    site = dict()
        # name
        # tagline
        # baseUrl
        # keywords

    contact = dict()

    db = dict()
        # un
        # pw
        # host
        # port
        # database

    api = dict()
        # weatherAPI_key

    sys = dict()

        # "debug": False,
        # req_uri = request.environ["REQUEST_URI"]
        # error : redirect, 404
        # redirect_uri
        # remote_ip


    # Call at start to reset varables;
    @staticmethod
    def init():
        # clear() is a method of dictionary;
        # explicitly initialized with dict() above because
        # at times clear doesn't work; it doesn't seem to think
        # it's a dictionary;

        G.site.clear()
        G.contact.clear()
        G.db.clear()
        G.api.clear()
        G.sys.clear()



