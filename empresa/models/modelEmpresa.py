#encoding:utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _



# Create your models here.
class Empresa(models.Model):
	nombre = models.CharField(unique=True, max_length=50, verbose_name=_('Nombre de la empresa'))
	calle  = models.CharField(max_length=50, verbose_name=_('Calle'))
	num_exterior = models.CharField(max_length=8, verbose_name=_('Numero exterior'))
	num_interior = models.CharField(max_length=8, null=True, blank=True, verbose_name=_('Numero interior'))
	colonia = models.CharField(max_length=70, verbose_name=_('Colonia'))
	municipio = models.CharField(max_length=70, verbose_name=_('Municipio'))
	estado = models.CharField(max_length=50, verbose_name=_('Estado'))
	telefono = models.CharField(max_length=15, null=True, blank=True, verbose_name=_('Telefono'))
	email = models.EmailField(null=True, blank=True, verbose_name=_('Correo electronico'))
	pagina_web = models.URLField(null=True, blank=True, verbose_name=_('Pagina web'))
	giro = models.CharField(max_length=10, verbose_name=_('Giro de la empresa'))
	nombre_encargado = models.CharField(max_length=50, null=True, blank=True)

	def __unicode__(self):
		return self.nombre

	def is_ins(self):
		return pagoEmpresa.objects.filter(empresa__id=self.id).count()
	is_insc = property(is_ins)

	class Meta:
		app_label = 'empresa'



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