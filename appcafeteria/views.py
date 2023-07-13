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
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
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


