from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.views import logout_then_login
from .forms import *
from django.contrib import messages
import requests


# Create your views here.

def home(request):
    products = Product.objects.filter(if_offer=True)[:4]
    context = {}
    suscrito(request, context)
    return render(request, 'core/index2.html', {'products': products, "context": context})



def suscrito(request,context):
    if request.user.is_authenticated:
        email = request.user.email
        resp = requests.get(f"http://127.0.0.1:8000/api/suscrito/{email}")
        context["suscrito"] = resp.json()["suscrito"]

def productos(request):
    products = Product.objects.all()
    return render(request, 'core/productos.html', {'products': products})





def registro(request):
    if request.method == 'POST':
        registro = Registro(request.POST)
        if registro.is_valid():
            registro.save()
            return redirect(to='login')
    else:
        registro = Registro()
    return render(request, 'core/registro.html', {'form': registro})


def login(request):
    return render(request, 'core/login.html')


def crud(request):
    return render(request, 'core/crud.html')


def productoscrud(request):
    products = Product.objects.all()
    return render(request, 'core/productoscrud.html', {'products': products})


def crudUsuario(request):
    return render(request, 'core/crudUsuario.html')


def usuario(request):
    return render(request, 'core/usuario.html')


def seguimiento(request):
    return render(request, 'core/seguimiento.html')


def historial(request):
    id_usuario = request.user.id
    ventas = Sale.objects.filter(client_id=id_usuario).prefetch_related('detail_set__product', 'following_set')

    return render(request, 'core/historial.html', {'ventas':ventas})


def suscripcion(request):
    context = {}
    suscrito(request, context)
    if request.method == 'POST':
        if request.user.is_authenticated:
            resp = requests.get(f"http://127.0.0.1:8000/api/suscribir/{request.user.email}")
            suscrito(request, context)
            context["mensaje"] = resp.json()["mensaje"]
            return render(request, 'core/suscripcion.html', context)

    else:
        suscrito(request, context)
        return render(request, 'core/suscripcion.html', context)


def logout(request):
    return logout_then_login(request, login_url='home')


def addtocar(request, id):
    producto = Product.objects.get(id=id)
    precio = int(producto.price)
    if producto.if_offer:
        precio = int(producto.get_discount_price())

    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == id:
            item[3] += 1
            item[4] = item[2] * item[3]
            break
    else:
        carro.append([id, producto.name, precio, 1, precio, producto.image])

    request.session["carro"] = carro
    return redirect(to="productos")


def clean(request):
    request.session.flush()
    return redirect(to="productos")


def carro(request):
    context = {}
    suscrito(request, context)
    carro = request.session.get("carro", [])
    total = 0
    for i in carro:
        total = total + i[4]

    resp = requests.get(f"http://127.0.0.1:8000/api/suscrito/{request.user.email}")
    esta_suscrito = resp.json()["suscrito"]

    if esta_suscrito:
        total = total - (total * 0.05)
    return render(request, 'core/carro.html', {"carro": carro, 'total':total, "context": context})


def dropitem(request, id):
    producto = Product.objects.get(id=id)
    precio = int(producto.price)
    if producto.if_offer:
        precio = int(producto.get_discount_price())

    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == id:
            if item[3] > 1:
                item[3] -= 1
                item[4] = item[2] * item[3]
                break
            else:
                carro.remove(item)

    request.session["carro"] = carro
    return redirect(to="carro")

def comprar(request):

    if  not request.user.is_authenticated:
        return  redirect(to='login')
    carro = request.session.get("carro", [])
    total = 0



    for item in carro:
        total += item[4]

    resp = requests.get(f"http://127.0.0.1:8000/api/suscrito/{request.user.email}")
    esta_suscrito = resp.json()["suscrito"]
    if esta_suscrito:
        total = total - (total * 0.05)
        
    venta = Sale()
    venta.client = request.user
    venta.total = total
    venta.save()

    follow = Following()
    follow.sale = venta
    follow.status="En preparacion"
    follow.save()


    for item in carro:
        detalle = Detail()
        detalle.product = Product.objects.get(id = item[0])
        detalle.price = item[4]
        detalle.amount = item[3]
        detalle.sale = venta
        detalle.save()

    for item in carro:
        producto = Product.objects.get(id = item[0])
        cantidad = item[3]
        stock = producto.stock
        producto.stock = stock - cantidad
        producto.save()
        request.session["carro"] = [ ]


    return redirect(to="carro")

def agregarproductos(request):
    return  render(request, 'core/agregar.html')

def agregar(request):
    datos = request.POST
    producto = Product()
    producto.name = datos["name"]
    producto.price = datos["price"]
    producto.description = datos["description"]
    producto.stock = datos["stock"]
    producto.discount_percent = datos["discount_percent"]
    producto.image = "https://www.funpets.cl/1680-large_default/natural-food-gatos-adultos-premium-75kg.jpg"

    if datos.get("if_offer") == 'on':
        producto.if_offer = True
    else:
        producto.if_offer = False
    producto.save()

    return render(request, 'core/agregar.html')

def search(request):
    id = request.POST["id"]
    seguimiento = Following.objects.filter(id=id).first()
    print(seguimiento)
    return render(request, 'core/seguimiento.html', {'seguimiento': seguimiento})


