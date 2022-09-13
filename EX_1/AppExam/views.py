from cgitb import html
from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
import pandas as pd
import numpy as np
import simplejson as json
#import folium

# VARIABLES GLOBALES


# REDIRECCIONES

def index(request):
    return render(request, 'index.html')

def mapa(request):
    return redirect('cargarMapa')

def metricas(request):
    return redirect('/listastarbucks')

def graficos(request):
    return render(request, 'graficos.html')

# LÓGICA
#Así se mandan datos de py a html
def prueba(request):
    datos = ['a','b','c','d']
    template = loader.get_template('metricas.html')
    context = { 'datos': datos,}
    return HttpResponse(template.render(context, request))

def listastarbucks(request):

    #NO OLVIDAR CAMBIAR LA RUTA DE MANERA INDIVIDUAL en cada uno de sus
    # equipos, para LA LECTURA DEL ARCHIVO DE STARBUCKS
    df = pd.read_csv('C:/AnacondaPython/Python_Georeferencia/EX_1/AppExam/static/data/starbucks.csv')

    servicioAbierto = df['24_hour_service']
    #siServicioHoras = 0
    noServicioHoras = 0

    for i in servicioAbierto:
        if i != "false": 
            noServicioHoras = noServicioHoras+1 
    

    template = loader.get_template('metricas.html')
    context = {'noServicioHoras':noServicioHoras}

    return HttpResponse(template.render(context, request))

def cargarMapa(request):

    datos = pd.read_excel(r'C:\Users\jorge\Django\EX_1\AppExam\static\data\starbucks_in_california.xlsx')

    lat = datos['Latitude'] #Pos 9 
    lon = datos['Longitude']#Pos 10
    info = datos['name'].tolist()

    LATITUD = lat.tolist()
    LONGITUD = lon.tolist()

    LAT = json.dumps(LATITUD)
    LON = json.dumps(LONGITUD)
    INFOR = json.dumps(info)

    pagina = loader.get_template('mapa.html')
    context = {'LAT': LAT , 'LON': LON, 'INFOR': INFOR}
    return HttpResponse(pagina.render(context, request))
