import socket, logging

class AppFilter(logging.Filter):

    def filter(self, record):
        record.host_name = socket.gethostname()
        return True

    def logformat(self):

        return '%(host_name)s   tools_class   honeypot_scada  message %(message)s'


# def gelflogformat(*args, **kwargs):
#     def handler(func):
#         result = func()
#
#     return '{ "version": "1.1", "host": "%(host_name)s", "message": %(message)s, "level": 5, "tools_class": "honeypot_scada" }'

