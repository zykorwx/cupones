# -*- coding: utf-8 *-*
from cupon.models import Promocion, Cupon
from empresa.models import Empresa
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from usuario.models import Perfil


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
admin.site.register(Cupon)

