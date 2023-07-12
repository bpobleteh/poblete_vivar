from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Producto
from django.core.files.storage import default_storage


def Principal(request):
    return render(request,'Principal.html')
def Segunda(request):
    return render(request,'Segunda.html')
def Tercera(request):
    return render(request,'Tercera.html')
def Cuarta(request):
    return render(request,'Cuarta.html')
def Quinta(request):
    return render(request,'Quinta.html')
def Sexta(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if len(first_name) < 3 or len(last_name) < 3:
            messages.error(request, 'El nombre y el apellido deben tener al menos 3 letras.')
            return redirect('Sexta')

        if password != confirm_password:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('Sexta')

        if len(password) < 8 or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
            messages.error(request, 'La contraseña debe tener al menos 8 caracteres, 1 letra y 1 número.')
            return redirect('Sexta')

        personal_info = [first_name, last_name, username]
        if any(info.lower() in password.lower() for info in personal_info):
            messages.error(request, 'La contraseña no puede contener información personal.')
            return redirect('Sexta')

        user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
        user.save()

        messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
        return redirect('Octava')
    else:
        return render(request, 'Sexta.html')
def Septima(request):
    pro=Producto.objects.all()
    return render(request,'Septima.html',{'pro':pro})

def Octava(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('agregar')
            else:
                return redirect('lista_productos')
        else:
            # El usuario no existe o las credenciales son inválidas
            return render(request, 'Octava.html', {'error': 'Credenciales inválidas'})
    else:
        return render(request, 'Octava.html')

def logout(request):
    logout(request)
    return redirect('Principal')

@login_required(login_url='Octava')
def agregar(request):
    if not request.user.is_superuser:
        return redirect('Prinicipal')
    # Lógica para agregar productos a la base de datos
    return render(request, 'agregar.html')

@login_required(login_url='Octava')
def lista_productos(request):
    # Lógica para mostrar la lista de productos y permitir compras
    return render(request, 'lista_productos.html')

def agregar(request):
    if request.method == 'POST':
        form = Producto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = Producto()
    return render(request, 'agregar.html', {'form': form})
def agregarrec(request):
    x = request.POST['nombre']
    y = request.POST['descripcion']
    z = request.POST['valor']
    fotografia = request.FILES['fotografia']  
    nombre_archivo = default_storage.save('agregar' + fotografia.name, fotografia)
    pro = Producto(nombre=x, descripcion=y, valor=z, fotografia=nombre_archivo)  
    pro.save()
    return redirect('Septima')

def eliminar(request,id):
    pro=Producto.objects.get(id=id)
    pro.delete()
    return redirect("Septima")

def actualizar(request,id):
    pro=Producto.objects.get(id=id)
    return render(request,'actualizar.html',{'pro':pro})

def actualizarrec(request,id):
    x=request.POST['nombre']
    y=request.POST['descripcion']
    z=request.POST['valor']
    pro=Producto.objects.get(id=id)
    pro.nombre=x
    pro.descripcion=y
    pro.valor=z
    pro.save()
    return redirect(to="Septima")
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})


