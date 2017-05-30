import socket

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




