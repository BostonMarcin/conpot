from pygelf import GelfUdpHandler
import logging; from conpot.core.loggers.utils import create_extra, MyFormatter
import socket

# from utils import AppFilter


class GelfLogger(object):
    def __init__(self, host, port,debug):

        logger = logging.getLogger()
        formatter = MyFormatter()
        # format_VAR = " ".join("{n} %({n})s".format(n=v) for v in VARS.keys())
        # log_format = logging.Formatter('%(asctime)-15s ' + format_VAR + ' short_message %(message)s')
        # app_filter = AppFilter()
        # log_format = AppFilter().logformat()
        # formatter = logging.Formatter(log_format)


        handler = GelfUdpHandler(host=host,port = port,debug = debug, include_extra_fields=True)



        # handler.addFilter(app_filter)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    def log(self, data):
        # stub function since the additional handler has been added to the root loggers instance.
        pass
