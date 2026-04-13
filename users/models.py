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