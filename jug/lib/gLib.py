class G():

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


    # Call at start to reset varables;
    @staticmethod
    def reset():
        G.site.clear()
        G.contact.clear()
        G.db.clear()
        G.api.clear()
        G.sys.clear()
