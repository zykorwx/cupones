# encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Max
from cupon.models import Cupon
from empresa.models import pagoEmpresa



# Se genera el formulario para agregar una nueva empresa,
# una vez que esta empresa se creo se manda al registro para generar su login.

def mostrar_cupones(request, empresa_id, promocion_id):
	ultimoPago = pagoEmpresa.objects.filter(empresa=empresa_id).aggregate(Max('fecha_pago'))
	if ultimoPago['fecha_pago__max'] == None:
		cupones = Cupon.objects.filter(id_promocion=promocion_id)
		return render_to_response('empresas/mostrar_cupones.html', {'cupones':cupones}, context_instance=RequestContext(request))
	else:
		from dateutil.relativedelta import relativedelta
		siguientePago = ultimoPago['fecha_pago__max'] + relativedelta(months=1)
		cupones = Cupon.objects.filter(fecha_creacion__range=(ultimoPago['fecha_pago__max'],siguientePago), id_promocion=promocion_id)
		return render_to_response('empresas/mostrar_cupones.html', {'cupones':cupones, 'promocion': promocion_id}, context_instance=RequestContext(request))