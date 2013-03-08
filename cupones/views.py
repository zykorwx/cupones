#encoding:utf-8
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from cupon.models import Promocion
from endless_pagination.decorators import page_template


@login_required(login_url='/#iniciaSecion')
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/')


@page_template('cupones/index_page.html') 
def index(
        request, template='cupones/index.html', extra_context=None):
	context = {
    'promociones': Promocion.objects.filter(estado = 1),
    }
        if extra_context is not None:
    	    context.update(extra_context)
    	return render_to_response(
            template, context, context_instance=RequestContext(request))
