Clicktotal
=======
Log martes 19 de marzo 2013
==========================================

Se modificaron y agregaron:
(mod) cupon.models.Promocion # Se agrego la configuracion de la promocion
(add) cupon.models.ConfPromocion  # este es para tener un control de precios dinamicos 
(mod) empresa.models.py # Los modelos se separaron dentro de la carpeta models
(add) empresa.models.pagoEmpresa # Se agrego una tabla para tener control de los pagos
                                  # de nuestros clientes. Ademas a la tabla se la agregaron 
                                  # propiedes para facilitar las consultas.
  @ Propiedades
  (add) empresa.models.pagoEmpresa.ultimoPago # Devuelve el ultimo pago realizado
  (add) empresa.models.pagoEmpresa.fechaSiguientePago # Devuelve la fecha para realizar el siguiente pago
  (add) empresa.models.pagoEmpresa.cantidadTotalCuponesEmpresa # Devuelve la cantidad total de cupones 
                                                               # que ha expedido una empresa
  (add) empresa.models.pagoEmpresa.cantidadCuponesPeriodo # Devuelve la cantidad de cupones expedidos
                                                          # desde el ultimo pago
  (add) empresa.models.pagoEmpresa.esPrimerPago # Devuelve si es el primer pago que realiza la empresa
(add) empresa.forms.LoginEmpresaForm # Para optimizar la seguridad del admin de las empresas
(mod) empresa.views.admin_empresa # Optimizado y corregido el problema de cliclo infinuto, y evita 
                                  # conexiones indevidas
(mod) empresa.views.login_empresa # Mejorada la seguridad, tambien se agrego, una session para almacenar
                                  # nombre de la empresa.
(mod) empresa.views.nueva_empresa # Ahora cuando se terminan de ingresar los datos de la empresa se envia
                                 # al formulario para crearle un nombre de user y password
(mod) empresa.decorators.py # Se modificio para optimizar la validadcion de si la empresa esta logeada
