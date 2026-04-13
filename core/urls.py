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