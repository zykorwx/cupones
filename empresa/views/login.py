# encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from empresa.forms import LoginEmpresaForm
from empresa.models import UserEmpresa

# login de una empresa
# no se hace uso del decorador login_empresa_required dado que envia un error desconocido
def login_empresa(request):
	if request.session.get('empresa_id') == None:
		if request.method=='POST':
			formulario = LoginEmpresaForm(request.POST)
			if formulario.is_valid():
				user1 = UserEmpresa.objects.get(user=request.POST.get('user',''))
				if user1.password == request.POST.get('password'):
						request.session['empresa_id'] = user1.empresa.id
						request.session['empresa_nombre'] = user1.empresa
						return HttpResponseRedirect('/empresa/admin/%s' % request.session.get('empresa_id'))
		else:
			formulario = LoginEmpresaForm()
			return render_to_response('empresas/login_empresa.html', {'formulario':formulario}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/empresa/admin/%s' % request.session.get('empresa_id'))


#cerrar sesion de una empresa
def logout_empresa(request):
    try:
        del request.session['empresa_id']
    except KeyError:
        pass
    return HttpResponseRedirect('/')