from django.forms import ModelForm
from models import Empresa

class EmpresaForm(ModelForm):
	class Meta:
		model = Empresa