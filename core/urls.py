from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('enrutador/', user_views.enrutador_login, name='enrutador'),
    path('caja/', user_views.vista_caja, name='caja'),
    
    # Dashboard
    path('panel/', user_views.panel_admin, name='panel_admin'),
    
    # Rutas Productos
    path('panel/productos/crear/', user_views.crear_producto, name='crear_producto'),
    path('panel/productos/editar/<int:id>/', user_views.editar_producto, name='editar_producto'),
    path('panel/productos/borrar/<int:id>/', user_views.borrar_producto, name='borrar_producto'),
    
    # Rutas Clientes
    path('panel/clientes/crear/', user_views.crear_cliente, name='crear_cliente'),
    path('panel/clientes/editar/<int:id>/', user_views.editar_cliente, name='editar_cliente'),
    path('panel/clientes/borrar/<int:id>/', user_views.borrar_cliente, name='borrar_cliente'),
    
    # Rutas Empleados
    path('panel/empleados/crear/', user_views.crear_empleado, name='crear_empleado'),
    path('panel/empleados/editar/<int:id>/', user_views.editar_empleado, name='editar_empleado'),
    path('panel/empleados/borrar/<int:id>/', user_views.borrar_empleado, name='borrar_empleado'),
]