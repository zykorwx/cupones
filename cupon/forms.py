#encoding:utf-8
from django.forms import ModelForm, DateInput, FileInput
from models import Promocion, Cupon



class CuponForm(ModelForm):
	class Meta:
		model = Cupon
		exclude = ('id_promocion', 'num_cupon',)


class PromocionForm(ModelForm):
    class Meta:
        model = Promocion
        exclude = ('fecha_creacion',)
        widgets= {'fecha_publicacion': DateInput(), 'fecha_termino': DateInput(),'imagen': FileInput(), }
