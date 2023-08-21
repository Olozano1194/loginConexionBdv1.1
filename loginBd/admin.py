from django.contrib import admin
from .models import RegistrarUsuario

# Register your models here.

# admin.site.register(RegistrarUsuario)

@admin.register(RegistrarUsuario)
class RegisterUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lastname', 'user', 'email', 'roles', 'password')
    list_editable = ('name', 'lastname', 'user', 'email', 'roles', 'password')
