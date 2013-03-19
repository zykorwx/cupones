# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from models import Empresa, UserEmpresa
from django import forms

class EmpresaForm(ModelForm):
	class Meta:
		model = Empresa

class UserEmpresaForm(ModelForm):
	repite_password = forms.CharField(max_length=20, label=_('Repite password'))
	class Meta:
		password = forms.CharField(widget=forms.PasswordInput)
		model = UserEmpresa
		exclude = ('fecha_creacion', 'empresa',)
		fields = ('user', 'password', 'repite_password')
		widgets = {
            'password': forms.PasswordInput(),
        }

class LoginEmpresaForm(forms.Form):
	user = forms.CharField(max_length=20, label=_('Nombre de usuario'))
	password = forms.CharField(max_length=20, label= _(u'Contraseña'))
