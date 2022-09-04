from cgitb import html
from django.shortcuts import render, HttpResponse, redirect
import numpy as np
#import folium

# VARIABLES GLOBALES


# REDIRECCIONES

def index(request):
    return render(request, 'index.html')

def mapa(request):
    return render(request, 'mapa.html')

def metricas(request):
    return render(request, 'metricas.html')

def graficos(request):
    return render(request, 'graficos.html')

# LÓGICA
