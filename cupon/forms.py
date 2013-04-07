#encoding:utf-8
from django.forms import ModelForm
from models import Promocion, Cupon
from django import forms


# Se genera el form del cupon y omitimos algunos campos
class CuponForm(ModelForm):
	class Meta:
		model = Cupon
		exclude = ('id_promocion', 'num_cupon', 'fecha_creacion', 'canjeado', 'user')



class PromocionEmpresaForm(ModelForm):
    class Meta:
        model = Promocion
        exclude = ('fecha_creacion', 'id_empresa', 'activo',)

    def clean_fecha_publicacion(self):
    	from dateutil import relativedelta
    	from datetime import datetime
    	hoy = datetime.now()
    	data = self.cleaned_data['fecha_publicacion']
    	diferencia = relativedelta.relativedelta(data, hoy)
    	if abs(diferencia.years) >= 1 and abs(diferencia.days >= 0):    		
    		raise forms.ValidationError("El limite de diferencia para publicar la promocion es de 6 meses")
    	elif abs(diferencia.years) < 1 and abs(diferencia.months) > 6:
    		raise forms.ValidationError("El limite de diferencia para publicar la promocion es de 6 meses")
    	elif diferencia.days < 0:
    		raise forms.ValidationError("No se puede publicar la promocion antes de hoy")
    	return data

    def clean_fecha_termino(self):
    	from dateutil import relativedelta
    	from datetime import datetime
    	hoy = datetime.now()
    	data = self.cleaned_data['fecha_termino']
    	diferencia = relativedelta.relativedelta(data, hoy)
    	if abs(diferencia.years) >= 1 and abs(diferencia.days >= 0):
    		raise forms.ValidationError("El limite de diferencia para finalizar la promocion es de 12 meses")
    	elif diferencia.days < 0:
    		raise forms.ValidationError("No se puede finalizar la promocion antes de hoy")
    	return data