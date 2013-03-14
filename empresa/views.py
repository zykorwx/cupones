# encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from forms import EmpresaForm, UserEmpresaForm
from models import UserEmpresa
from cupon.models import Cupon, Promocion
from decorators import login_empresa_required

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

# Se genera el formulario para que la empresa tenga un nombre de usuario unico y una contraseña
# para ingresar a su administrador.
def nuevo_user_empresa(request, id_empresa):
	if request.method=='POST':
		formulario = UserEmpresaForm(request.POST)
		if formulario.is_valid():
			user_empresa = UserEmpresa(empresa_id=id_empresa, user=request.POST.get('user',''), password=request.POST.get('password',''))
			user_empresa.save()
			return HttpResponseRedirect('/')
	else:
		formulario = UserEmpresaForm()
	return render_to_response('empresas/registro.html', {'formulario':formulario}, context_instance=RequestContext(request))

# El administrador solo puede entrar una empresa logeada, si no lo esta se redirecciona a logearse
@login_empresa_required(login_url='/empresa/login')
def admin_empresa(request, id_empresa):
	promos = Promocion.objects.filter(id_empresa=id_empresa)
	cupones = ()
	for i in range(len(promos)):
		cupones[i] = Cupon.objects.filter(id_promocion=promos[i].id).count()
	return render_to_response('empresas/admin.html', {'promos': promos, 'cupones': cupones}, context_instance=RequestContext(request))


# login de una empresa
# no se hace uso del decorador login_empresa_required dado que envia un error desconocido
def login_empresa(request):
	if request.session.get('empresa_id') == None:
		if request.method=='POST' and request.POST.get('user','') != "" :
			user1 = UserEmpresa.objects.get(user=request.POST.get('user',''))
			if user1.password == request.POST.get('password'):
					request.session['empresa_id'] = user1.id
					return HttpResponseRedirect('/empresa/admin/%s' % request.session.get('empresa_id'))
		else:
			formulario = UserEmpresaForm()
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
