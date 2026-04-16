from django.shortcuts import render, redirect, get_object_or_404
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
    return render(request, 'users/caja.html', {'empleado': request.user})

# --- 3. DASHBOARD DEL ADMIN (LEER) ---
@login_required
def panel_admin(request):
    if request.user.rol != 'admin': return redirect('/caja/')
    
    productos = Producto.objects.all()
    clientes = Cliente.objects.all()
    empleados = CustomUser.objects.filter(rol='empleado') 
    
    return render(request, 'users/panel_admin.html', {
        'productos': productos, 'clientes': clientes, 'empleados': empleados
    })

# ==========================================
#        CRUD DE PRODUCTOS
# ==========================================
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
def editar_producto(request, id):
    if request.user.rol != 'admin': return redirect('/caja/')
    producto = get_object_or_404(Producto, id=id)

    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.precio = request.POST.get('precio')
        producto.stock = request.POST.get('stock')
        producto.save()
        return redirect('panel_admin')
    return render(request, 'users/editar_producto.html', {'producto': producto})

@login_required
def borrar_producto(request, id):
    if request.user.rol != 'admin': return redirect('/caja/')
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('panel_admin')


# ==========================================
#        CRUD DE CLIENTES
# ==========================================
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
def editar_cliente(request, id):
    if request.user.rol != 'admin': return redirect('/caja/')
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.telefono = request.POST.get('telefono')
        cliente.email = request.POST.get('email')
        cliente.save()
        return redirect('panel_admin')
    return render(request, 'users/editar_cliente.html', {'cliente': cliente})

@login_required
def borrar_cliente(request, id):
    if request.user.rol != 'admin': return redirect('/caja/')
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    return redirect('panel_admin')


# ==========================================
#        CRUD DE EMPLEADOS
# ==========================================
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

@login_required
def editar_empleado(request, id):
    if request.user.rol != 'admin': return redirect('/caja/')
    # Filtramos para asegurarnos de que el Admin no se modifique a sí mismo por accidente
    empleado = get_object_or_404(CustomUser, id=id, rol='empleado')

    if request.method == 'POST':
        empleado.username = request.POST.get('username')
        
        # Si escribió una nueva contraseña, la encriptamos y la guardamos
        nueva_pass = request.POST.get('password')
        if nueva_pass:
            empleado.set_password(nueva_pass)
            
        empleado.save()
        return redirect('panel_admin')
    return render(request, 'users/editar_empleado.html', {'empleado': empleado})

@login_required
def borrar_empleado(request, id):
    if request.user.rol != 'admin': return redirect('/caja/')
    empleado = get_object_or_404(CustomUser, id=id, rol='empleado')
    empleado.delete()
    return redirect('panel_admin')