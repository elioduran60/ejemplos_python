from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def bienvenidos(request):
    return HttpResponse("Bienvenidos a SAP")

def despedida(request):
    return HttpResponse("Hasta luego")

def contacto(request):
    return HttpResponse("Contacto")