from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Definimos las opciones de roles (Lo que se guarda en la BD, Lo que ve el usuario)
    ROLES = (
        ('admin', 'Administrador'),
        ('empleado', 'Empleado de Mostrador'),
    )
    
    # Creamos el campo para el rol, por defecto será empleado
    rol = models.CharField(max_length=20, choices=ROLES, default='empleado')

    def __str__(self):
        # Ahora al ver un usuario en el panel, dirá: "juan - Empleado de Mostrador"
        return f"{self.username} - {self.get_rol_display()}"
    # ... tu código anterior de CustomUser se queda igual ...

class Cliente(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre Completo")
    telefono = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre del Producto")
    # max_digits=10 significa hasta 99,999,999.99
    precio = models.DecimalField(max_digits=10, decimal_places=2) 
    stock = models.IntegerField(default=0, verbose_name="Cantidad en Inventario")
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio}"