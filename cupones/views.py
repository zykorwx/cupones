#encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from cupon.models import Promocion

def index(request):
	promociones = Promocion.objects.all()
	return render_to_response('cupones/index.html', {'promociones': promociones}, context_instance=RequestContext(request))