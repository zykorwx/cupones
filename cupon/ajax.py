from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax


@dajaxice_register
def generaCupon(request, cupon):
	dajax = Dajax()
	dajax.assign('#cupon', 'innerHTML', cupon)
	return dajax.json()

