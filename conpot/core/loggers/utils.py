import socket, logging

VARS = {'client_ip':('addr',
                     'address',
                         ),
            'source':socket.gethostname(),
            }



def create_extra(_locals, *args, **kwargs):
    """
    Use locals variables to get specific values. Use VARS for mapping.
    :param _locals: locals() output
    :param args: for further features
    :param kwargs: for further features
    :return:
    """

    _extra = {}
    _extra['source'] =  VARS['source']

    # build extra for client's address
    if 'client_ip' not in kwargs:
        _extra['client_ip'] = "Undefined"
        for _ in VARS['client_ip']:

            if _ in _locals:
                _extra['client_ip'] =_locals[_]
                break
    else:
        _extra['client_ip'] = kwargs['client_ip']

    return _extra



# Custom formatter
class MyFormatter(logging.Formatter):

    format_VAR = " ".join("{n} %({n})s".format(n = v) for v in VARS.keys())
    # log_format = logging.Formatter('%(asctime)-15s ' + format_VAR + ' shortmessage %(message)s')
    standard = '%(asctime)-15s %(message)s'
    err_fmt, dbg_fmt  = standard, standard
    info_fmt  = '%(asctime)-15s ' + format_VAR + ' shortmessage %(message)s'


    def __init__(self, fmt='%(asctime)-15s %(message)s'):

        logging.Formatter.__init__(self, fmt)


    def format(self, record):

        # Save the original format configured by the user
        # when the logger formatter was instantiated
        format_orig = self._fmt

        # Replace the original format with one customized by logging level
        if record.levelno == logging.DEBUG:
            self._fmt = MyFormatter.dbg_fmt

        elif record.levelno == logging.INFO:
            self._fmt = MyFormatter.info_fmt

        elif record.levelno == logging.ERROR:
            self._fmt = MyFormatter.err_fmt

        # Call the original formatter class to do the grunt work
        result = logging.Formatter.format(self, record)

        # Restore the original format configured by the user
        self._fmt = format_orig

        return result

class AppFilter(logging.Filter):

    def filter(self, record):
        record.host_name = socket.gethostname()
        return True

    def logformat(self):

        return '%(host_name)s   tools_class   honeypot_scada  message %(message)s'
