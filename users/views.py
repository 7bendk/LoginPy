from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Esta etiqueta obliga a que solo usuarios que ya iniciaron sesión puedan pasar por aquí
@login_required
def enrutador_login(request):
    """
    Esta función atrapa al usuario justo después del login y revisa su gafete (rol).
    """
    if request.user.rol == 'admin':
        # Si es el jefe, lo mandamos al panel de control de Django
        return redirect('/admin/')
    else:
        # Si es empleado, lo mandamos a la caja registradora (que crearemos pronto)
        return redirect('/caja/')