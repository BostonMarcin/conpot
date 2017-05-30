import socket, logging

VARS = {'client_ip':('addr',
                         'sockaddr',
                         ),
            'hostname':socket.gethostname(),
            }


def create_extra(_locals, *args, **kwargs):

    _extra = {}
    _extra['hostname'] =  VARS['hostname']

    #build extra for client's address
    _extra['client_ip'] = "Undefined"
    for _ in VARS['client_ip']:
        if _ in _locals:
            _extra['client_ip'] =_locals[_]
            break

    return _extra




class AppFilter(logging.Filter):

    def filter(self, record):
        record.host_name = socket.gethostname()
        return True

    def logformat(self):

        return '%(host_name)s   tools_class   honeypot_scada  message %(message)s'
