#encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from cupon.models import Promocion

def index(request):
	total = Promocion.objects.count()
	mitad = total // 2
	if mitad == 0:
		mitad = 1
	promociones = Promocion.objects.all()[:mitad]
	promociones1 = Promocion.objects.all()[mitad:total]
	return render_to_response('cupones/index.html', {'promociones': promociones, 'promociones1':promociones1}, context_instance=RequestContext(request))