from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Cliente, Producto

# --- 1. EL SEMÁFORO ---
@login_required
def enrutador_login(request):
    if request.user.rol == 'admin':
        return redirect('/panel/') 
    else:
        return redirect('/caja/')

# --- 2. VISTA DE LA CAJA (EMPLEADOS) ---
@login_required
def vista_caja(request):
    """Esta es la pantalla principal de la caja para los empleados"""
    return render(request, 'users/caja.html', {'empleado': request.user})

# --- 3. VISTAS DEL PANEL PERSONALIZADO (ADMIN) ---
@login_required
def panel_admin(request):
    if request.user.rol != 'admin':
        return redirect('/caja/')
    
    productos = Producto.objects.all()
    clientes = Cliente.objects.all()
    empleados = CustomUser.objects.filter(rol='empleado') 
    
    return render(request, 'users/panel_admin.html', {
        'productos': productos,
        'clientes': clientes,
        'empleados': empleados
    })

@login_required
def crear_producto(request):
    if request.user.rol != 'admin': return redirect('/caja/')
    if request.method == 'POST':
        Producto.objects.create(
            nombre=request.POST.get('nombre'), 
            precio=request.POST.get('precio'), 
            stock=request.POST.get('stock')
        )
        return redirect('panel_admin')
    return render(request, 'users/crear_producto.html')

@login_required
def crear_cliente(request):
    if request.user.rol != 'admin': return redirect('/caja/')
    if request.method == 'POST':
        Cliente.objects.create(
            nombre=request.POST.get('nombre'),
            telefono=request.POST.get('telefono'),
            email=request.POST.get('email')
        )
        return redirect('panel_admin')
    return render(request, 'users/crear_cliente.html')

@login_required
def crear_empleado(request):
    if request.user.rol != 'admin': return redirect('/caja/')
    if request.method == 'POST':
        CustomUser.objects.create_user(
            username=request.POST.get('username'),
            password=request.POST.get('password'),
            rol='empleado'
        )
        return redirect('panel_admin')
    return render(request, 'users/crear_empleado.html')