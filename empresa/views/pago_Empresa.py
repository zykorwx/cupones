# encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from empresa.models import pagoEmpresa
from empresa.forms import PagoEmpresaForm
from empresa.decorators import login_empresa_required

# El administrador solo puede entrar una empresa logeada, si no lo esta se redirecciona a logearse
# Editar la promocion de la empresa xD
@login_empresa_required(login_url='/empresa/login')
def pago_Empresa(request):
	pago = pagoEmpresa.objects.get(empresa__id=request.session['empresa_id'])
	if request.method == 'POST':
		formulario = PagoEmpresaForm(request.POST) # El instance para instanciar la info que traiga promo
		if formulario.is_valid():
			aux = formulario.save(commit=False)
			aux.empresa = pago
			aux.save()
			return HttpResponseRedirect('/empresa/admin')
	else:
		formulario = PagoEmpresaForm()
	return render_to_response('empresas/pagoEmpresa.html', {'formulario':formulario, 'pago': pago }, context_instance=RequestContext(request))
