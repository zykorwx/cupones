#encoding:utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import Max
from empresa.models import Empresa, pagoEmpresa
from django.contrib.auth.models import User

# Se usa para usarlo en un combo
ESTADO_CHOICES = (
    ('1', _('Publicar')),
    ('0', _('No publicar')),
)

# Confuguracion de las promociones: por ahora solo maneja el precio.
class ConfPromocion(models.Model):
	nombre = models.CharField(max_length=15, verbose_name=_(u'Nombre de configuracion'))
	precio_x_cupon = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_(u'Monto por cupon'))
	
	def __unicode__(self):
		return self.nombre

# Create your models here.
class Promocion(models.Model):
	id_empresa = models.ForeignKey(Empresa, verbose_name=_('Empresa o negocio'))
	fecha_creacion = models.DateTimeField(auto_now=True)
	fecha_publicacion = models.DateField(blank=True, null=True, verbose_name=_('Fecha de publicacion'))
	fecha_termino = models.DateField(blank=True, null=True, verbose_name=_('Fecha limite'))
	num_limite = models.SmallIntegerField(blank=True, null=True, verbose_name=_('Numero limite de cupones'))
	estado = models.CharField(max_length=1, choices=ESTADO_CHOICES, verbose_name=_('Estado'), default='0')
	imagen = models.ImageField(upload_to='promociones', verbose_name='Imagen promocion')
	descripcion = models.TextField(verbose_name=_('Descripcion de la promocion'))
	confPromocion = models.ForeignKey(ConfPromocion, verbose_name=_('Tipo promocion:'))
	def __unicode__(self):
            return u'Empresa: %s - id_promocion: %s - estado: %s' % (self.id_empresa, self.id, self.estado)
	
	# Este metodo cuenta los cupones que hay por promocion
	def cuentaCupones(self):
		return Cupon.objects.filter(id_promocion= self).count()
	cupones = property(cuentaCupones)

	def cuentaCuponesPeriodo(self):
		ultimoPago = pagoEmpresa.objects.filter(empresa=self.id_empresa).aggregate(Max('fecha_pago'))
		if ultimoPago['fecha_pago__max'] == None:
			return Cupon.objects.filter(id_promocion=self.id).count()
		else:
			from dateutil.relativedelta import relativedelta
			siguientePago = ultimoPago['fecha_pago__max'] + relativedelta(months=1)
			return Cupon.objects.filter(fecha_creacion__range=(ultimoPago['fecha_pago__max'],siguientePago), id_promocion=self.id).count()
	cuponesPeriodo = property(cuentaCuponesPeriodo)


# Genera el cupon de la empresa
class Cupon(models.Model):
	id_promocion = models.ForeignKey(Promocion, verbose_name=_('Promocion del cupon'))
	num_cupon = models.CharField(max_length=10, verbose_name=_('Codigo unico del cupon'))
	user = models.ForeignKey(User)
	canjeado = models.BooleanField(default=False) 
	fecha_creacion = models.DateTimeField(auto_now=True)


	# Muestra el id de la promocion junto al numero de cupon generado
	def __unicode__(self):
		return '%s - %s' % (self.id_promocion, self.num_cupon)


