from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect

# La parte de inicio de sesion la maneja totalmente django-social-auth

# Cierra la sesion del usuario logeado
@login_required(login_url='/#iniciaSecion')
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/')