from cgitb import html
from multiprocessing import context
from traceback import print_list
from urllib.robotparser import RequestRate
from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from django.utils.html import escapejs
#import geopy  as geo
#from geopy.geocoders import Nominatim
import numpy as np
import pandas as pd
import csv, os
import simplejson as json
#import folium

# VARIABLES GLOBALES


# REDIRECCIONES

def index(request):
    return render(request, 'index.html')

def mapa(request):
    return redirect('/cargarMapa')

def metricas(request):
    return redirect('/prueba')

def graficos(request):
    return render(request, 'graficos.html')

# LÓGICA
#Así se mandan datos de py a html
def prueba(request):
   
   




    template = loader.get_template('metricas.html')
    #context = { 'datos': newData,}
    return HttpResponse(request)

def cargarMapa(request):

    datos = pd.read_excel(r'C:/Users/jorge/Django/EX_1/AppExam/static/data/starbucks_in_california.xlsx')

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