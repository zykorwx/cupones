#encoding:utf-8
from django.conf.urls import patterns, url, include
from django.conf import settings
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()
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
#dajaxice
	url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
#social
	url(r'', include('social_auth.urls')),
#Urls
	url(r'^$', 'cupones.views.index'),
    url(r'^empresa/nueva$', 'empresa.views.nueva_empresa'),
    url(r'^promocion/nueva/$', 'cupon.views.nueva_promocion'),
    url(r'^cupon/nuevo/(?P<id_promocion>\d+)$', 'cupon.views.nuevo_cupon'),
    url(r'^cupon/mostrar/(?P<id_cupon>\d+)$', 'cupon.views.mostrar_cupon'),
    url(r'^cerrar/$', 'cupones.views.cerrar'),
)





# Esta linea hace que en modo produccion o trabajando con el wsgi funcionen
# los static files
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
