
import socket

def extra(_locals, *args, **kwargs):

    _extra_str = []

    VARS = {'client_ip':('addr',
                         'sockaddr',
                         ),
            'hostname':socket.gethostname(),
            }

    _extra_str.append('hostname : {n}'.format(n = VARS['hostname']))

    #build extra for client's address
    for _ in VARS['client_ip']:
        _str = "client_ip : Undefined"
        if _ in _locals:
            _str = "client_ip : {n}".format(n=_locals['client_ip'])
            break
    _extra_str.append(_str)

    return ' '.join(_extra_str)




