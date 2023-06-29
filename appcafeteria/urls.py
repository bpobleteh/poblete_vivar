from django.urls import path
from .views import Principal
from .views import Segunda
from .views import Tercera
from .views import Cuarta
from .views import Quinta
from .views import Sexta
from .views import Septima
from .views import Octava
from .views import agregar
from .views import logout_view
from .views import eliminar
from .views import actualizar
from .views import actualizarrec
from .views import agregarrec





urlpatterns =[
    path('Principal.html',Principal, name='Principal'),
    path('Segunda.html',Segunda, name='Segunda'),
    path('Tercera.html',Tercera, name='Tercera'),
    path('Cuarta.html',Cuarta, name='Cuarta'),
    path('Quinta.html',Quinta, name='Quinta'),    
    path('Sexta.html',Sexta, name='Sexta'), 
    path('Septima.html',Septima, name='Septima'), 
    path('Octava.html',Octava, name='Octava'), 
    path('logout',logout_view, name='logout'),
    path('agregar', agregar,name='agregar'),
    path('eliminar/<int:id>/',eliminar,name='eliminar'),
    path('actualizar/<int:id>/',actualizar,name='actualizar'),
    path('agregarrec/',agregarrec, name='agregarrec'),
    path('actualizar/actualizarrec/<int:id>/',actualizarrec,name='actualizarrec'),
 
]





