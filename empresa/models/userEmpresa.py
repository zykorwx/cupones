#encoding:utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from modelEmpresa import Empresa

class UserEmpresa(models.Model):
	empresa = models.OneToOneField(Empresa)
	user = models.CharField(unique=True, max_length=20, verbose_name=_('Nombre de usuario'))
	password = models.CharField(max_length=20, verbose_name=_('Password'))
	fecha_creacion = models.DateTimeField(auto_now=True)

	def __unicode__(self):
    		return self.user

	class Meta:
		app_label = 'empresa'