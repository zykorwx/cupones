#encoding:utf-8
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from cupon.models import Promocion


def index(request):
	promociones = Promocion.objects.filter(estado = 1)
	return render_to_response('cupones/index.html', {'promociones': promociones}, context_instance=RequestContext(request))


@login_required(login_url='/#iniciaSecion')
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/')