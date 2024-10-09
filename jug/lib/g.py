class G():

    db = {}
    # db = {
    #   'un' : '',
    #   'pw' : '',
    #   'host' : '',
    #   'port' : '',
    #   'databse' : ''
    # }
    # db_un = ""
    # db_pw = ""
    # db_host = ""
    # db_port = ""
    # db_database = ""
    # weatherAPI_key = None

    api = {}
    site = {}


# Problem with this format is that access is verbose;
# Have to do: G["db]["un"]
# Or worse: G.get("db", {}).get("un")

# G = {
#     "db" : {
#         "un" : None,
#         "pw" : None,
#         "host" : None,
#         "port" : None,
#         "database" : None
#     },

#     "weatherAPI_key" : None
# }