#encoding:utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import Max
from empresa.models import Empresa, pagoEmpresa
from django.contrib.auth.models import User
import os



# Se usa para usarlo en un combo
ESTADO_CHOICES = (
    ('1', _('Publicar')),
    ('0', _('No publicar')),
)





# Configuracion de las promociones: por ahora solo maneja el precio.
class ConfPromocion(models.Model):
	nombre = models.CharField(max_length=15, verbose_name=_(u'Nombre de configuracion'))
	precio_x_cupon = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_(u'Monto por cupon'))
	
	def __unicode__(self):
		return self.nombre

	class Meta:
		app_label = 'cupon'

def get_image_path(promocion, filename):
    return os.path.join('imagenes/empresas/emp_'+str(promocion.id_empresa), 'promociones', filename)

# Create your models here.
class Promocion(models.Model):
	id_empresa = models.ForeignKey(Empresa, verbose_name=_('Empresa o negocio'))
	fecha_creacion = models.DateTimeField(auto_now=True)
	fecha_publicacion = models.DateField(blank=True, null=True, verbose_name=_('Fecha de publicacion'))
	fecha_termino = models.DateField(blank=True, null=True, verbose_name=_('Fecha limite'))
	num_limite = models.SmallIntegerField(blank=True, null=True, verbose_name=_('Numero limite de cupones'))
	estado = models.CharField(max_length=1, choices=ESTADO_CHOICES, verbose_name=_('Estado'), default='0')
	activo = models.CharField(max_length=1,  default='0')
	imagen = models.ImageField(upload_to=get_image_path, verbose_name='Imagen promocion')
	descripcion = models.TextField(verbose_name=_('Descripcion de la promocion'))
	confPromocion = models.ForeignKey(ConfPromocion, verbose_name=_('Tipo promocion:'))

	def __unicode__(self):
		return u'Empresa: %s - id_promocion: %s - estado: %s' % (self.id_empresa, self.id, self.estado)

	class Meta:
		app_label = 'cupon'
	
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


	# Este metodo valida que la fecha del cupon cumpla con lo establecido por el usuario
	# True = Esta dentro de las condiciones y se puede mostrar
	# None = No tiene esta condicion asi que se puede mostrar
	# False = No cumple las conducion
	# -1 = Indica que no se debe hacer nada
	def validar_promocion_a_mostrar(self):
		from datetime import datetime
		actual = self.cuentaCupones()
		hoy = datetime.now()
		if self.valida_fecha_publicacion(hoy) == True or self.valida_fecha_publicacion(hoy) == None:
			if self.valida_fecha_termino(hoy) == True or self.valida_fecha_termino(hoy) == None:
				if self.valida_num_limite(actual) == True or self.valida_num_limite(actual) == None:
					return self.publicarPromocion() # devuelve True : publicar
				elif self.valida_num_limite(actual) == False:
					return self.ocultarPromocion() # Devuelve False : No publicar
			elif self.valida_fecha_termino(hoy) == False:
				return self.ocultarPromocion()
		else:
			return self.ocultarPromocion()


	# Valida si el campo trae None, o si cumple con la condicion que el usuario indico
	def valida_num_limite(self, actual):
		if self.num_limite != None: # Si la promocion tiene numero limite
			if  actual < self.num_limite:  # Si aun hay cupones disponibles
				return True # True si la promocion aun tiene cupones disponibles
			else:
				return False # Si es que ya no tiene cupones disponibles
		else:
			return None # Si es que no tiene algun valor asignado

	# Valida si el campo trae None, o si cumple con la condicion que el usuario indico
	def valida_fecha_termino(self, hoy):
		if self.fecha_termino != None: # Si la promocion tiene una fecha limite
			if self.fecha_termino >= hoy.date():  # Si la promocion esta dentro de la fecha limite
				return True # True si la promocion aun esta dentro de la fecha limite
			else:
				return False # Si es que ya no esta dentro de la fecha limite
		else:
			return None # Si es que no tiene algun valor asignado

	# Valida si el campo trae None, o si cumple con la condicion que el usuario indico
	def valida_fecha_publicacion(self, hoy):
		if self.fecha_publicacion != None: # Si la promocion tiene una fecha de publicacion
			if self.fecha_publicacion <= hoy.date():  # Si la promocion esta dentro de la fecha de publicacion
				return True # True si la promocion aun esta dentro de la fecha de publicacion
			else:
				return False # Si es que ya no esta dentro de la fecha de publicacion
		else:
			return None # Si es que no tiene algun valor asignado

	# Cambia el estado de la promocion a publicada
	def publicarPromocion(self):
		if self.activo == "0": # Si la promocion no esta publicada, hay que publicarla
			self.activo = 1
			self.save()
		return True # True es mostrar la promocion

	# Cambia el estado de la promocion a Oculta
	def ocultarPromocion(self):
		if self.activo == "1": # 1 es publicado
			self.activo = 0  # 0 es no publicado
			self.save()
		return False # False es ocultar la promocion


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

	class Meta:
		app_label = 'cupon'
