import logging
from logging.config import dictConfig

log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelprefix)s %(asctime)s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",

        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    },
    "loggers": {
        "fapi-logger": {"handlers": ["default"], "level": "DEBUG"},
    },
}


def init_logger():
    dictConfig(log_config)


def retrieve_logger():

    # lazy init the logger
    if 'fapi-logger' not in logging.Logger.manager.loggerDict.keys():
        init_logger()
        logging.getLogger('fapi-logger').info('Logger initialized!')

    return logging.getLogger('fapi-logger')
