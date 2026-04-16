from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Esta es la línea mágica que reemplaza el cohete por tu diseño
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    
    # La ruta invisible que creamos para el semáforo (Admin vs Empleado)
    path('enrutador/', user_views.enrutador_login, name='enrutador'),
]

urlpatterns = [
    path('admin/', admin.site.urls), # (Este es el de Django, lo dejamos por si acaso)
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('enrutador/', user_views.enrutador_login, name='enrutador'),
    path('caja/', user_views.vista_caja, name='caja'),
    
    # --- NUEVAS RUTAS DEL PANEL CRUD ---
    path('panel/', user_views.panel_admin, name='panel_admin'),
    path('panel/productos/crear/', user_views.crear_producto, name='crear_producto'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('enrutador/', user_views.enrutador_login, name='enrutador'),
    path('caja/', user_views.vista_caja, name='caja'),
    
    # Rutas del Panel CRUD
    path('panel/', user_views.panel_admin, name='panel_admin'),
    path('panel/productos/crear/', user_views.crear_producto, name='crear_producto'),
    path('panel/clientes/crear/', user_views.crear_cliente, name='crear_cliente'),   # <--- NUEVA
    path('panel/empleados/crear/', user_views.crear_empleado, name='crear_empleado'), # <--- NUEVA
]