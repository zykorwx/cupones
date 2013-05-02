# encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from empresa.models import Empresa
from empresa.forms import PagoEmpresaForm
from django.contrib.admin.views.decorators import staff_member_required


COSTO_INSCRIPCION = 500.00


# El administrador solo puede entrar una empresa logeada, si no lo esta se redirecciona a logearse
# Editar la promocion de la empresa xD
@staff_member_required
def pago_Empresa(request, empresa_id):
	empresa = Empresa.objects.get(pk=empresa_id)
	if request.method == 'POST':
		formulario = PagoEmpresaForm(request.POST) # El instance para instanciar la info que traiga promo
		if formulario.is_valid():
			aux = formulario.save(commit=False)
			aux.empresa = empresa
			aux.cantidad = COSTO_INSCRIPCION
			aux.concepto = 1
			aux.save()
			return HttpResponseRedirect('/empresa/admin')
	else:
		formulario = PagoEmpresaForm()
	return render_to_response('empresas/pagoEmpresa.html', {'formulario':formulario, 'empresa': empresa, 'COSTO_INSCRIPCION': COSTO_INSCRIPCION }, context_instance=RequestContext(request))
