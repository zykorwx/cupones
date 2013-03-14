from django.forms import ModelForm
from models import Empresa, UserEmpresa
from django import forms

class EmpresaForm(ModelForm):
	class Meta:
		model = Empresa

class UserEmpresaForm(ModelForm):
	class Meta:
		password = forms.CharField(widget=forms.PasswordInput)
		model = UserEmpresa
		exclude = ('fecha_creacion', 'empresa',)
		widgets = {
            'password': forms.PasswordInput(),
        }