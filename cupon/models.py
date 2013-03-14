#encoding:utf-8
from django.db import models
from empresa.models import Empresa
from django.utils.translation import ugettext_lazy as _

# Se usa para usarlo en un combo
ESTADO_CHOICES = (
    ('1', _('Publicar')),
    ('0', _('No publicar')),
)

# Create your models here.
class Promocion(models.Model):
	id_empresa = models.ForeignKey(Empresa, verbose_name=_('Empresa o negocio'))
	fecha_creacion = models.DateTimeField(auto_now=True)
	fecha_publicacion = models.DateField(blank=True, null=True, verbose_name=_('Fecha de publicacion'))
	fecha_termino = models.DateField(blank=True, null=True, verbose_name=_('Fecha limite'))
	num_limite = models.SmallIntegerField(blank=True, null=True, verbose_name=_('Numero limite de cupones'))
	estado = models.CharField(max_length=1, choices=ESTADO_CHOICES, verbose_name=_('Estado'), default='0')
	imagen = models.ImageField(upload_to='promociones', verbose_name='Imagen promocion')
	
	def __unicode__(self):
            return u'Empresa: %s - id_promocion: %s - estado: %s' % (self.id_empresa, self.id, self.estado)

class Cupon(models.Model):
	id_promocion = models.ForeignKey(Promocion, verbose_name=_('Promocion del cupon'))
	num_cupon = models.CharField(max_length=10, verbose_name=_('Codigo unico del cupon'))
	fecha_creacion = models.DateTimeField(auto_now=True)

	def __unicode__(self):
            return '%s - %s' % (self.id_promocion, self.num_cupon)