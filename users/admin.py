from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Esto habilita el CRUD visual en el panel de control
admin.site.register(CustomUser, UserAdmin)