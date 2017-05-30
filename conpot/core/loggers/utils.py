
def extra(_locals, *args, **kwargs):

    VARS = {'client_ip':('addr',
                         'sockaddr',
                         )}

    #return client's address
    for _ in VARS['client_ip']:
        if _ in _locals: return _locals[_]


