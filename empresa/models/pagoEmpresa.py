#encoding:utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from empresa import Empresa
from cupon.models import Promocion

CONCEPTOS = (
    ('1', _('Inscripcion')),
    ('0', _('Mensualidad')),
)
FORMASPAGO = (
    ('1', _('Contado')),
    ('0', _('Credito')),
)

class pagoEmpresa(models.Model):
	empresa = models.ForeignKey(Empresa)
	cantidad = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_(u'Monto a pagar $'))
	fecha_pago = models.DateTimeField(auto_now=True)
	concepto = models.CharField(max_length=1, choices=CONCEPTOS, verbose_name=_('Concepto de pago'), default='1')
	formaPago = models.CharField(max_length=1, choices=FORMASPAGO, verbose_name=_('Forma de pago'), default='0')

	def __unicode__(self):
            return u'Empresa: %s - Canitdad: %s - Fecha de pago: %s' % (self.empresa, self.cantidad, self.fecha_pago)

	class Meta:
		app_label = 'empresa'

class HistorialCuponesEmpresa(models.Model):
	promocion = models.ForeignKey(Promocion)
	totalCupones = models.IntegerField(default=0)
	periodo = models.DateTimeField(blank=True, null=True)

	def __unicode__(self):
		return u'Promocion: %s - Numero de cupones: %s - Periodo: %s' % (self.promocion, self.totalCupones, self.periodo)

	class Meta:
		app_label = 'empresa'