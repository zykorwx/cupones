# encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.db.models import Max, Sum
from cupon.models import Cupon, Promocion
from empresa.models import pagoEmpresa
from empresa.decorators import login_empresa_required



# El administrador solo puede entrar una empresa logeada, si no lo esta se redirecciona a logearse
@login_empresa_required(login_url='/empresa/login')
def admin_empresa(request, empresa):
	if str(empresa) == str(request.session.get('empresa_id')):  # protegemos de malos usos de la url xD
		aux = calculaPago(empresa)
		mostrarCupones = cuponesValidos(empresa)
		if aux[3] == False:
			periodo = aux[0]
			pago = aux[1]
			total = aux[2]
			promos = aux[3]
			return render_to_response('empresas/admin.html', {'periodo': periodo, 'pago': pago, 'total': total, 'promos': promos, 'cupones':mostrarCupones}, context_instance=RequestContext(request))
		else:
			periodo = aux[0]
			pago = aux[1]
			total = aux[2]
			promos = aux[3]
			return render_to_response('empresas/admin.html', {'periodo': periodo, 'pago': pago, 'total': total, 'promos':promos, 'cupones':mostrarCupones}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')


def calculaPago(empresa_id):
	ultimoPago = pagoEmpresa.objects.filter(empresa=empresa_id).aggregate(Max('fecha_pago'))
	promos1 = Promocion.objects.filter(id_empresa = empresa_id)
	promos = Cupon.objects.filter(id_promocion__id_empresa=empresa_id)
	precio = 0
	infoPago = []
	if ultimoPago['fecha_pago__max']==None:
		aux = promos.aggregate(Sum('id_promocion__confPromocion__precio_x_cupon'))
		precio = aux['id_promocion__confPromocion__precio_x_cupon__sum']
		infoPago.append(promos1)
		infoPago.append(precio)
		infoPago.append(promos.count())
		infoPago.append(False)
		return infoPago
	else:
		from dateutil.relativedelta import relativedelta
		siguientePago = ultimoPago['fecha_pago__max'] + relativedelta(months=1)
		periodo = Cupon.objects.filter(fecha_creacion__range=(ultimoPago['fecha_pago__max'],siguientePago), id_promocion__id_empresa=empresa_id)
		aux = periodo.aggregate(Sum('id_promocion__confPromocion__precio_x_cupon'))
		precio = aux['id_promocion__confPromocion__precio_x_cupon__sum']
		infoPago.append(periodo)
		infoPago.append(precio)
		infoPago.append(periodo.count())
		infoPago.append(promos1)
		return infoPago


def cuponesValidos(empresa_id):
	from dateutil.relativedelta import relativedelta
	from datetime import datetime
	hoy = datetime.now()
	ayer = hoy - relativedelta(days=1)
	periodo = Cupon.objects.filter(fecha_creacion__range=(ayer,hoy), id_promocion__id_empresa=empresa_id).order_by('-fecha_creacion')	
	return periodo
