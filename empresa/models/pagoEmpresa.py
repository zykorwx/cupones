#encoding:utf-8
from django.db import models
from django.db.models import Max
from django.utils.translation import ugettext_lazy as _
from empresa import Empresa
from cupon.models import Cupon


class pagoEmpresa(models.Model):
	empresa = models.ForeignKey(Empresa)
	cantidad = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_(u'Monto a pagar $'))
	fecha_pago = models.DateTimeField(auto_now=True)

	def _ultimoPago(self):
		return self.objects.all().aggregate(Max('fecha_pago'))
	ultimoPago = property(_ultimoPago)

	def _fechaSiguentePago(self):
		from dateutil.relativedelta import relativedelta
		return self.ultimoPago + relativedelta(months=1)
	fechaSiguientePago = property(_fechaSiguentePago)

	def _cantidadTotalCuponesEmpresa(self):
		return Cupon.objects.filter(id_promocion__id_empresa=self.empresa)
	cantidadTotalCuponesEmpresa = property(_cantidadTotalCuponesEmpresa)

	def _cantidadCuponesPeriodo(self):
		return Cupon.objects.filter(fecha_creacion__range=(self.ultimoPago, self.fechaSiguientePago), id_promocion__id_empresa=self.empresa)
	cantidadCuponesPeriodo = property(_cantidadCuponesPeriodo)
	
	def _esPrimerPago(self):
		return self.objects.filter(empresa=self.empresa).count == 0
	esPrimerPago = property(_esPrimerPago)

	class Meta:
		app_label = 'empresa'