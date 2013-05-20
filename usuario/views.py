from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from cupon.models import Cupon

# La parte de inicio de sesion la maneja totalmente django-social-auth

# Cierra la sesion del usuario logeado
@login_required(login_url='/#iniciaSecion')
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/')


@login_required(login_url='/#iniciaSecion')
def mis_cupones(request):
	cupones = Cupon.objects.filter(user = request.user)
	return render_to_response('usuarios/miscupones.html', {'cupones': cupones}, context_instance=RequestContext(request))
