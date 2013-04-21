# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect

class login_empresa_required(object):
    "Un decorador amb fam"
    def __init__(self, login_url='/'):
        self.login_url = login_url

    def __call__(self, f):
        def is_login(request, *args, **kw_args):
        	if request.session.get('empresa_id') == None:
        		return HttpResponseRedirect(self.login_url)
        	else:
        		return f(request, *args, **kw_args)
        is_login.__name__ = f.__name__
        is_login.__doc__ = f.__doc__
        return is_login