from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax

#ejemplo de como funciona dajax, y dajaxice no se usa en la aplicacion
@dajaxice_register
def mensaje(request):
	dajax = Dajax()
	dajax.assign('p #mensaje', 'innerHTML', 'Debes logearte')
	return dajax.json()

