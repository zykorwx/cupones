# -*- coding: utf-8 *-*
from cupon.models import Promocion, Cupon
from empresa.models import Empresa, UserEmpresa
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from usuario.models import Perfil

# El administrador de django nos ayudara a nosotros a llevar el manejo de los
# clientes y no tener que gastar mucho tiempo en eso.
# Se agrega la relacion 1, 1 al administrador de django
class PerfilInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    verbose_name_plural = 'perfiles'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (PerfilInline, )


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Promocion)
admin.site.register(Empresa)
admin.site.register(UserEmpresa)
admin.site.register(Cupon)

