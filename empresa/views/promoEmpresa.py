# encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from cupon.models import ConfPromocion, Promocion
from empresa.models import Empresa
from cupon.forms import PromocionEmpresaForm
from empresa.decorators import login_empresa_required
from django.core import serializers





# El administrador solo puede entrar una empresa logeada, si no lo esta se redirecciona a logearse
# Editar la promocion de la empresa xD
@login_empresa_required(login_url='/empresa/login')
def promoEmpresa(request, promo_id):
	promo = Promocion.objects.get(pk=promo_id)
	if request.method == 'POST':
		formulario = PromocionEmpresaForm(request.POST, request.FILES, instance=promo) # El instance para instanciar la info que traiga promo
		if formulario.is_valid():
			aux = formulario.save(commit=False)
			aux.save()
			aux.validar_promocion_a_mostrar()
			return HttpResponseRedirect('/empresa/admin')
	else:
		formulario = PromocionEmpresaForm(instance=promo)
	return render_to_response('empresas/promoEmpresa.html', {'formulario':formulario, 'promo': promo }, context_instance=RequestContext(request))




# Agrega una nueva promocion de la  empresa xD
@login_empresa_required(login_url='/empresa/login')
def nuevaPromo(request, empresa_id):
	empresa = Empresa.objects.get(pk=empresa_id)
	if request.method == 'POST':
		formulario = PromocionEmpresaForm(request.POST, request.FILES)
		if formulario.is_valid():
			aux = formulario.save(commit=False)
			aux.id_empresa = empresa
			aux.save()
			aux.validar_promocion_a_mostrar()
			return HttpResponseRedirect('/empresa/admin')
	else:
		formulario = PromocionEmpresaForm()
	return render_to_response('empresas/promoEmpresa.html', {'formulario':formulario }, context_instance=RequestContext(request))



def ajaxConfEmpresa(request, id_conf):
	if request.is_ajax():
		format = 'json'
		mimetype = 'application/json'
		aux = ConfPromocion.objects.get(pk=id_conf)
		aux1 = serializers.serialize(format, [aux], fields=('nombre', 'precio_x_cupon'))
		data = aux1[1:-1]
		return HttpResponse(data, mimetype)

