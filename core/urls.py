from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', home, name="home"),
    path('productos', productos, name="productos"),
    path('registro', registro, name="registro"),
    path('login', LoginView.as_view(template_name='core/login.html'), name="login"),
    path('crud', crud, name="crud"),
    path('productoscrud', productoscrud, name="productoscrud"),
    path('crudUsuario', crudUsuario, name="crudUsuario"),
    path('usuario', usuario, name="usuario"),
    path('seguimiento', seguimiento, name="seguimiento"),
    path('historial', historial, name="historial"),
    path('suscripcion', suscripcion, name="suscripcion"),
    path('logout', logout, name="logout"),
    path('addtocar/<id>', addtocar, name="addtocar"),
    path('carro', carro, name="carro"),
    path('clean', clean),
    path('dropitem/<id>', dropitem, name="dropitem"),
    path('comprar', comprar, name="comprar"),
    path('agregarproductos', agregarproductos, name="agregarproductos"),
    path('agregar', agregar, name="agregar"),
    path('search', search, name="search"),

]
