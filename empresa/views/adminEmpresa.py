# encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from cupon.models import Promocion
from empresa.decorators import login_empresa_required



# El administrador solo puede entrar una empresa logeada, si no lo esta se redirecciona a logearse
@login_empresa_required(login_url='/empresa/login')
def admin_empresa(request, empresa):
	if str(empresa) == str(request.session.get('empresa_id')):  # protegemos de malos usos de la url xD
		promos = Promocion.objects.filter(id_empresa=empresa)
		return render_to_response('empresas/admin.html', {'promos': promos}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')