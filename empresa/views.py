#encoding:utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import simplejson
from models import Empresa
from forms import EmpresaForm

def nueva_empresa(request):
    if request.method=='POST':
    	formulario = EmpresaForm(request.POST)
    	if formulario.is_valid():
    		formulario.save()
    		return HttpResponseRedirect('/')
    else:
    	formulario = EmpresaForm()
    	return render_to_response('empresas/formulario.html', {'formulario':formulario}, context_instance=RequestContext(request))


