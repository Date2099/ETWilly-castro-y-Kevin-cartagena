from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Suscripcion
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def suscrito(request, email):
    try:
        suscrito = Suscripcion.objects.get(user_email=email)
        return Response({"suscrito": suscrito.status},status.HTTP_200_OK )
    except Suscripcion.DoesNotExist:
        return Response({"suscrito": False}, status.HTTP_200_OK)

@api_view(['GET'])
def suscribir(request, email):

    try:
        #suscribe al usuario cambiando el estado a True
        suscrito = Suscripcion.objects.get(user_email=email)
        suscrito.status = True
        suscrito.save()
        return Response({"mensaje": "suscrito Exitosamente"}, status.HTTP_200_OK)
    except Suscripcion.DoesNotExist:
        #crea un objeto y guarda la suscripcion en la base de datos y lo da True
        suscrito = Suscripcion()
        suscrito.user_email = email
        suscrito.status = True
        suscrito.save()
        return Response({"mensaje": "suscrito Exitosamente"}, status.HTTP_200_OK)


@api_view(['GET'])
def cancelar_suscripcion(request, email):
    try:
        suscrito = Suscripcion.objects.get(user_email=email)
        suscrito.status = False
        suscrito.save()
        return Response({"mensaje": "suscripcion cancelada"}, status.HTTP_200_OK)
    except Suscripcion.DoesNotExist:
        return Response({"mensaje": "correo invalido"}, status.HTTP_200_OK)