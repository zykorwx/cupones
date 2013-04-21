#encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext


# Muestra los cupones. El decorador @page_template, sirve para
# paginar estilo twitter los cupones
def indexEmpresa(request):
	return render_to_response('empresas/index.html', context_instance=RequestContext(request))
