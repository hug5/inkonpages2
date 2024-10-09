## baseConfig setup

# import logging

# # Set up the logging configuration
# logging.basicConfig(
#     filename='etc/log/debug.log',
#     #encoding="utf-8",        # I'm getting a warning message? LSP problem? Think you need python 3.9;
#     filemode="a",            # a is default
#     level=logging.DEBUG,
#     format="{levelname} : {message} | {module}:{lineno} | {asctime}",
#     style="{",
#     datefmt="%Y.%m.%d %H:%M:%S %p",
# )

# # init the logger variable
# logger = logging.getLogger(__name__)
# # In the router.py script, we import logger variable;

# # First logger print
# logger.info('======== logger started ========')

# # It seems that the variable 'logger' needs to be specifically imported to work;


##############################################3

## dictConfig setup

import logging
from logging.config import dictConfig


dictConfig({
    'version': 1,
    'formatters': {

        'formatter1': {
          "format": "{levelname} : {message} | {module}:{lineno} | {asctime}",
          "style": "{"
          # For this style {, must denote the style;
        },
        'formatter2': {
          # 'format': '%(levelname)s : %(message)s | %(module)s:%(lineno)s | %(asctime)s',
          'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
          # "style": "%"
          # For this % format, style appears to be optional
        }
        # The options for style are "%", "$", or "{".

    },

    'handlers': {
        "console": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "formatter1",
        },
        "console2": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "formatter1",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": "etc/log/debug.log",
            "formatter": "formatter1",
        },
    },

    "root": {
        "level": "DEBUG",
        "handlers": [
            "console",
            #"file"
        ]
    },

    "loggers": {
        "logger1": {
            "level": "DEBUG",
            "handlers": [
                # "console",
                "file"
            ],
            "propagate": False,
        },
        "logger2": {
            "level": "DEBUG",
            "handlers": ["console2"],
            "propagate": False,
        }

    },
})

root = logging.getLogger("root")
logger = logging.getLogger("logger1")

root.info('======== root logger started ========')
logger.info('======== logger started ========')

# Console sends to uwsgi log;
# file won't send to uwsgi log;


# logger.info()
# logger.debug()
# logger.warning()
# logger.error()
# logger.critical()

# Special exception logger; shorthand;
# logger.exception(f"config.toml Load Error: {e}")
