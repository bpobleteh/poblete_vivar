from django.urls import path
from .views import home
from .views import Segunda
from .views import Tercera
from .views import Cuarta
from .views import Quinta
from .views import Sexta
from .views import Septima
from .views import login
from .views import agregar
from .views import eliminar
from .views import actualizar
from .views import actualizarrec
from .views import agregarrec
from .views import products
from .views import home, products, register
from django.conf import settings
from django.conf.urls.static import static






urlpatterns =[
    path('home.html',home, name='home'),
    path('Segunda.html',Segunda, name='Segunda'),
    path('Tercera.html',Tercera, name='Tercera'),
    path('Cuarta.html',Cuarta, name='Cuarta'),
    path('Quinta.html',Quinta, name='Quinta'),    
    path('Sexta.html',Sexta, name='Sexta'), 
    path('Septima.html',Septima, name='Septima'), 
    path('login.html',login, name='login'), 
    path('agregar', agregar,name='agregar'),
    path('eliminar/<int:id>/',eliminar,name='eliminar'),
    path('actualizar/<int:id>/',actualizar,name='actualizar'),
    path('agregarrec/',agregarrec, name='agregarrec'),
    path('actualizar/actualizarrec/<int:id>/',actualizarrec,name='actualizarrec'),
    path('products.html', products, name='products'),
    path('', home, name='home'),
    path('products/', products,name='products'),
    path('register/', register, name='register'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




