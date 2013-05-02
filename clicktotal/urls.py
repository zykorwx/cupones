#encoding:utf-8
from django.conf.urls import patterns, url, include
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
# Administrador
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
#Url creada para decirle al sistema donde buscar los archivos subidos
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT, }
    ),
# Login Facebook, Twitter
	url(r'', include('social_auth.urls')),
# Urls clicktotal
	url(r'^$', 'clicktotal.views.index'),
# Urls Usuario
    url(r'^cerrar/$', 'usuario.views.cerrar'),
# Urls Empresa
    url(r'^empresas$', 'empresa.views.indexEmpresa'), # agregar nueva empresa
    url(r'^empresa/nueva$', 'empresa.views.nueva_empresa'), # agregar nueva empresa
    url(r'^empresa/pagos/(?P<empresa_id>\d+)$', 'empresa.views.pago_Empresa'), # agregar nueva empresa
    url(r'^empresa/login$', 'empresa.views.login_empresa'), # Login empresa
    url(r'^empresa/admin$', 'empresa.views.login_empresa'), # Admin de la empresa
    url(r'^empresa/admin/(?P<empresa>\d+)$', 'empresa.views.admin_empresa'), # Admin de la empresa
    url(r'^empresa/promo/(?P<promo_id>\d+)$', 'empresa.views.promoEmpresa'), # Mostrar promocion de la empresa
    url(r'^empresa/cupones/(?P<empresa_id>\d+)/(?P<promocion_id>\d+)$', 'empresa.views.mostrar_cupones'), # Mostrar los cupones de la promocion de la empresa
    url(r'^empresa/nueva_promocion/(?P<empresa_id>\d+)$', 'empresa.views.nuevaPromo'), # Nueva promocion
    url(r'^empresa/cerrar$', 'empresa.views.logout_empresa'), # Cerrar sesion de la empresa
    url(r'^empresa/registro/(?P<id_empresa>\d+)$', 'empresa.views.nuevo_user_empresa'), # Agregar nueva empresa
# Ajax
    url(r'^ajax/confPromocion/(?P<id_conf>\d+)$', 'empresa.views.ajaxConfEmpresa'),
# Urls Cupon
    url(r'^cupon/nuevo/(?P<id_promocion>\d+)$', 'cupon.views.nuevo_cupon'),
    url(r'^cupon/mostrar/(?P<id_cupon>\d+)$', 'cupon.views.mostrar_cupon'),
    url(r'^cupon/canjear_cupon$', 'cupon.views.canjear_cupon_inscripcion'),
    
)


# Esta linea hace que en modo produccion o trabajando con el wsgi funcionen
# los static files
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
