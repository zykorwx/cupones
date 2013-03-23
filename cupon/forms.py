#encoding:utf-8
from django.forms import ModelForm
from django import forms
from models import Promocion, Cupon


# Se genera el form del cupon y omitimos algunos campos
class CuponForm(ModelForm):
	class Meta:
		model = Cupon
		exclude = ('id_promocion', 'num_cupon', 'fecha_creacion',)

# Se genera el form para crear una nueva promocion
class PromocionForm(ModelForm):
    class Meta:
        model = Promocion
        exclude = ('fecha_creacion',)


class PromocionEmpresaForm(ModelForm):
    class Meta:
        model = Promocion
        exclude = ('fecha_creacion', 'id_empresa',)

