Clicktotal
=======
Log viernes 22 de marzo 2013
==========================================
# Novedades #

- Ya se calcula el pago.
- Se muestra el numero de cupones por periodo.
- Se muestra el numero de cupones por promoción dentro del periodo.
- Se muestra el numero total de cupones por promoción.
- Se agrego un tab dentro del admin de empresas
- Se agrego un menu provisional para navegar de forma mas sencilla dentro de la app
- Se eliminaron las propiedades de la versión anterior, generaban muchas consultas a la bd

Log martes 19 de marzo 2013
==========================================

## Se modificaron y agregaron: ##

**(mod) cupon.models.Promocion** *# Se agrego la configuracion de la promocion*

**(add) cupon.models.ConfPromocion**  *# este es para tener un control de precios dinamicos* 

**(mod) empresa.models.py** *# Los modelos se separaron dentro de la carpeta models*

**(add) empresa.models.pagoEmpresa** *# Se agrego una tabla para tener control de los pagos de nuestros clientes. Ademas a la tabla se la agregaron 
propiedades para facilitar las consultas.*

## Propiedades de pagoEmpresa ##

----------

**(add) empresa.models.pagoEmpresa.ultimoPago** *# Devuelve el ultimo pago realizado*

**(add) empresa.models.pagoEmpresa.fechaSiguientePago** *# Devuelve la fecha para realizar el siguiente pago*
  
**(add) empresa.models.pagoEmpresa.cantidadTotalCuponesEmpresa** *# Devuelve la cantidad total de cupones que ha expedido una empresa*

**(add) empresa.models.pagoEmpresa.cantidadCuponesPeriodo*** # Devuelve la cantidad de cupones expedidos desde el ultimo pago*

**(add) empresa.models.pagoEmpresa.esPrimerPago** *# Devuelve si es el primer pago que realiza la empresa*

----------

**(add) empresa.forms.LoginEmpresaForm** *# Para optimizar la seguridad del admin de las empresas*

**(mod) empresa.views.admin_empresa** *# Optimizado y corregido el problema de cliclo infinuto, y evita conexiones indevidas*

**(mod) empresa.views.login_empresa** *# Mejorada la seguridad, también se agrego, una session para almacenar nombre de la empresa.*

**(mod) empresa.views.nueva_empresa** *# Ahora cuando se terminan de ingresar los datos de la empresa se envia al formulario para crearle un nombre de user y password*

**(mod) empresa.decorators.py** *# Se modificio para optimizar la validadcion de si la empresa esta logeada*
