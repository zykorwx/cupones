#encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
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


