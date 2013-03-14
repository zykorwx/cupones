#encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from cupon.models import Promocion
from endless_pagination.decorators import page_template


# Muestra los cupones. El decorador @page_template, sirve para
# paginar estilo twitter los cupones
@page_template('clicktotal/index_page.html') 
def index(
        request, template='clicktotal/index.html', extra_context=None):
	context = {
    'promociones': Promocion.objects.filter(estado = 1),
    }
        if extra_context is not None:
    	    context.update(extra_context)
    	return render_to_response(
            template, context, context_instance=RequestContext(request))
