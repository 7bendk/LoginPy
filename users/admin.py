from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Cliente, Producto

# 1. Títulos del panel
admin.site.site_header = "Administración de Sports POS"
admin.site.site_title = "Sports POS"
admin.site.index_title = "Panel de Control Principal"

# --- NUEVO: Le decimos a Django que muestre el campo 'rol' ---
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Información de Acceso (Sports POS)', {'fields': ('rol',)}),
    )

# 2. Registramos a los usuarios usando nuestra nueva configuración
admin.site.register(CustomUser, CustomUserAdmin)

# 3. Registramos clientes y productos
admin.site.register(Cliente)
admin.site.register(Producto)