class G():

    db = {}
        # un
        # pw
        # host
        # port
        # database

    api = {}
        # weatherAPI_key

    site = {}
        # name
        # tagline
        # baseUrl
        # keywords

    contact = {}

    debug = False

    # Call at start to reset varables;
    @staticmethod
    def reset():
        G.db.clear()
        G.api.clear()
        G.site.clear()
        G.debug = False
