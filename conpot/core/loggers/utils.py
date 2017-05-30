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



class AppFilter(logging.Filter):

    def filter(self, record):
        record.host_name = socket.gethostname()
        return True

    def logformat(self):

        return '%(host_name)s   tools_class   honeypot_scada  message %(message)s'
