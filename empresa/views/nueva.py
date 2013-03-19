# encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from empresa.forms import EmpresaForm, UserEmpresaForm
from empresa.models import UserEmpresa


# Se genera el formulario para agregar una nueva empresa,
# una vez que esta empresa se creo se manda al registro para generar su login.
def nueva_empresa(request):
    if request.method=='POST':
    	formulario = EmpresaForm(request.POST)
    	if formulario.is_valid():
    		aux = formulario.save()
    		return HttpResponseRedirect('/empresa/registro/%s' % aux.id)
    else:
    	formulario = EmpresaForm()
    return render_to_response('empresas/nueva_empresa.html', {'formulario':formulario}, context_instance=RequestContext(request))

# Se genera el formulario para que la empresa tenga un nombre de usuario unico y una contrase«Ða
# para ingresar a su administrador.
def nuevo_user_empresa(request, id_empresa):
	if request.method=='POST':
		formulario = UserEmpresaForm(request.POST)
		if formulario.is_valid():
			if request.POST.get('password','') == request.POST.get('repite_password',''):
				user_empresa = UserEmpresa(empresa_id=id_empresa, user=request.POST.get('user',''), password=request.POST.get('password',''))
				user_empresa.save()
				return HttpResponseRedirect('/')
	else:
		formulario = UserEmpresaForm()
	return render_to_response('empresas/registro.html', {'formulario':formulario}, context_instance=RequestContext(request))