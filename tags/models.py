#encoding:utf-8
# Este archivo agrega las etiquetas a cada promocion para poder filtrar por relacion.
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cupon.models import Promocion

class Categoria(models.Model):
	nombre = models.CharField(max_length=25, verbose_name=_(u'Nombre de la categoria'))

	def __unicode__(self):
		return self.nombre




class Tag(models.Model):
	nombre = models.CharField(max_length=25, verbose_name=_(u'Nombre de la etiqueta'))
	categoria = models.ForeignKey(Categoria)

	def __unicode__(self):
		return self.nombre


class Tag_promocion(models.Model):
	promocion = models.ForeignKey(Promocion)
	tag = models.ForeignKey(Tag)

	def __unicode__(self):
		return self.tag.nombre
