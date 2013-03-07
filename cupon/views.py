#encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from forms import CuponForm, PromocionForm
from models import Promocion, Cupon
import string
import random


def nueva_promocion(request):
    if request.method == 'POST':
    	formulario = PromocionForm(request.POST, request.FILES)
    	if formulario.is_valid():
    		formulario.save()
    		return HttpResponseRedirect('')
    else:
    	formulario = PromocionForm()
    	return render_to_response('cupon/form_promocion.html', {'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/#iniciaSecion')
def nuevo_cupon(request, id_promocion):
	promociones = Promocion.objects.get(pk=id_promocion)
	if request.method == 'POST':
		formulario = CuponForm(request.POST)
		if formulario.is_valid():
			cupon = Cupon(id_promocion=promociones, num_cupon=id_generator())			
			cupon.save()
			return HttpResponseRedirect('/cupon/mostrar/%s' % cupon.id)
	else:
		formulario = CuponForm()
		return render_to_response('cupon/form_cupon.html', {'formulario':formulario, 'promociones': promociones}, context_instance=RequestContext(request))

def mostrar_cupon(request, id_cupon):
	cupon = Cupon.objects.get(pk=id_cupon)
	return render_to_response('cupon/mostrarCupon.html', {'cupon': cupon}, context_instance=RequestContext(request))


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for x in range(size))