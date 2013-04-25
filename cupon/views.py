#encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from forms import CuponForm
from models import Promocion, Cupon
from django.contrib.auth.models import User
import string
import random


# Para generar un nuevo cupon los usuarios deben estar conectados
# se usua un link interno solo para mover a los usuarios a la parte de login.
# Si los cupones se agotaron y el usuario llega a ver este cupon vacio se le manda a al template no hay
@login_required(login_url='/#iniciaSecion')
def nuevo_cupon(request, id_promocion):
	promociones = Promocion.objects.get(pk=id_promocion)
	cupones = Cupon.objects.filter(id_promocion=id_promocion).count()
	if  promociones.validar_promocion_a_mostrar() == True:
		if request.method == 'POST':
			formulario = CuponForm(request.POST)
			if formulario.is_valid():
				user_id = User.objects.get(pk=request.user.id) 
				cupon = Cupon(id_promocion=promociones, num_cupon=id_generator(), user = user_id)			
				cupon.save()
				return HttpResponseRedirect('/cupon/mostrar/%s' % cupon.id)
		else:
			formulario = CuponForm()
			return render_to_response('cupon/form_cupon.html', {'formulario':formulario, 'promociones': promociones, 'cupones':cupones}, context_instance=RequestContext(request))
	else:
		return render_to_response('mensajes/noHay.html', {'promociones': promociones, 'cupones':cupones}, context_instance=RequestContext(request))

# Una vez generado el cupon se muestra el cupon de la siguiente forma, el id_cupon 
# se recibe una vez que nuevo cupon es usado o creado
def mostrar_cupon(request, id_cupon):
	cupon = Cupon.objects.get(pk=id_cupon)
	return render_to_response('cupon/mostrarCupon.html', {'cupon': cupon}, context_instance=RequestContext(request))

def canjear_cupon_inscripcion(request):
	return render_to_response('cupon/inscripcion.html',  context_instance=RequestContext(request))



# Este metodo lo unico que hace es generar un alfanumerico aleatorio de 6 digitos.
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for x in range(size))

