from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Producto
from django.core.files.storage import default_storage
from .forms import CustomUserCreationForm

def home(request):
    return render(request,'home.html')
def Segunda(request):
    return render(request,'Segunda.html')
def Tercera(request):
    return render(request,'Tercera.html')
def Cuarta(request):
    return render(request,'Cuarta.html')
def Quinta(request):
    return render(request,'Quinta.html')
def Septima(request):
    pro=Producto.objects.all()
    return render(request,'Septima.html',{'pro':pro})

@login_required
def products(request):
    return render(request, 'products.html')
def login(request):
    return render(request, 'registration/login.html')
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if len(first_name) < 3 or len(last_name) < 3:
            messages.error(request, 'El nombre y el apellido deben tener al menos 3 letras.')
            return redirect('registration/register')

        if password != confirm_password:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('registration/register')

        if len(password) < 8 or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
            messages.error(request, 'La contraseña debe tener al menos 8 caracteres, 1 letra y 1 número.')
            return redirect('registration/register')

        personal_info = [first_name, last_name, username]
        if any(info.lower() in password.lower() for info in personal_info):
            messages.error(request, 'La contraseña no puede contener información personal.')
            return redirect('registration/register')

        user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
        user.save()

        messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
        return redirect('registration/login')
    else:
        return render(request, 'registration/register.html')

def agregar(request):
    if request.method == 'POST':
        form = Producto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = Producto()
    return render(request, 'agregar.html', {'form': form})

def agregarrec(request):
    x = request.POST['nombre']
    y = request.POST['descripcion']
    z = request.POST['valor']
    fotografia = request.FILES['fotografia']
    nombre_archivo = default_storage.save('fotografia' + fotografia.name, fotografia)
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
def products(request):
    productos = Producto.objects.all()
    return render(request, 'products.html', {'productos': productos})


