from cgitb import html
from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import simplejson as json
import collections
import os

#Parte SVM
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import datasets
from sklearn import metrics

#Parte KMeans
from sklearn.cluster import KMeans
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
    return redirect('/listastarbucksgraf')

def mapsvmred(request):
    return redirect('/mapasvm')

# LÓGICA
#Así se mandan datos de py a html
def prueba(request):
    datos = ['a','b','c','d']
    template = loader.get_template('metricas.html')
    context = { 'datos': datos,}
    return HttpResponse(template.render(context, request))

def listastarbucks(request):
    #NO OLVIDAR CAMBIAR LA RUTA DE MANERA INDIVIDUAL en cada uno de sus
    # equipos, para LA LECTURA DEL ARCHIVO DE STARBUCKS.csv
    df = pd.read_csv(f'{os.path.dirname(os.path.abspath(__file__))}/static/data/starbucks.csv')

    servicioAbierto = df['24_hour_service']
    siHoras = 0
    noHoras = 0
    for i in servicioAbierto:
        if i == 1:
            siHoras = siHoras+1
        elif i == 0:
            noHoras = noHoras+1
   

    servicioClover = df['starbucks_reserve_clover_brewed']
    siClover = 0
    noClover = 0
    for i in servicioClover:
        if i == 1:
            siClover = siClover+1
        elif i == 0:
            noClover = noClover+1



    servicioFood = df['oven_warmed_food']
    siFood = 0
    noFood = 0
    for i in servicioFood:
        if i == 1:
            siFood = siFood+1
        elif i == 0:
            noFood = noFood+1



    servicioWiFi = df['free_wi_fi']
    siWifi = 0
    noWifi = 0
    for i in servicioWiFi:
        if i == 1:
            siWifi = siWifi+1
        elif i == 0:
            noWifi = noWifi+1



    servicioVerismo= df['verismo_system']
    siVerismo = 0
    noVerismo = 0
    for i in servicioVerismo:
        if i == 1:
            siVerismo = siVerismo+1
        elif i == 0:
            noVerismo = noVerismo+1


    servicioMobilePay= df['mobile_payment']
    siMobilePay = 0
    noMobilePay = 0
    for i in servicioMobilePay:
        if i == 1:
            siMobilePay = siMobilePay+1
        elif i == 0:
            noMobilePay = noMobilePay+1



    servicioDigitalReds= df['digital_rewards']
    siDigitalReds = 0
    noDigitalReds = 0
    for i in servicioDigitalReds:
        if i == 1:
            siDigitalReds = siDigitalReds+1
        elif i == 0:
            noDigitalReds = noDigitalReds+1



    servicioBoulange= df['la_boulange']
    siBoulange = 0
    noBoulange = 0
    for i in servicioBoulange:
        if i == 1:
            siBoulange = siBoulange+1
        elif i == 0:
            noBoulange = noBoulange+1
            



    servicioSodas= df['fizzio_handcrafted_sodas']
    siSodas = 0
    noSodas = 0
    for i in servicioSodas:
        if i == 1:
            siSodas = siSodas+1
        elif i == 0:
            noSodas = noSodas+1




    servicioDriveThru= df['drive_thru']
    siDriveThru = 0
    noDriveThru = 0
    for i in servicioDriveThru:
        if i == 1:
            siDriveThru = siDriveThru+1
        elif i == 0:
            noDriveThru = noDriveThru+1


    
    


    template = loader.get_template('metricas.html')
    context = {
        'siHoras':siHoras, 
        'noHoras':noHoras,
        'siClover':siClover,
        'noClover':noClover,
        'siFood':siFood, 
        'noFood': noFood,
        'siWifi':siWifi, 
        'noWifi':noWifi ,
        'siVerismo': siVerismo,
        'noVerismo': noVerismo,
        'siMobilePay': siMobilePay,
        'noMobilePay': noMobilePay,
        'siDigitalReds': siDigitalReds,
        'noDigitalReds': noDigitalReds,
        'siBoulange': siBoulange,
        'noBoulange': noBoulange,
        'siSodas': siSodas,
        'noSodas': noSodas,
        'siDriveThru': siDriveThru,
        'noDriveThru': noDriveThru  }

    return HttpResponse(template.render(context, request))

def listastarbucksgraf(request):
        #NO OLVIDAR CAMBIAR LA RUTA DE MANERA INDIVIDUAL en cada uno de sus
    # equipos, para LA LECTURA DEL ARCHIVO DE STARBUCKS.csv
    df = pd.read_csv(f'{os.path.dirname(os.path.abspath(__file__))}/static/data/starbucks.csv')

    servicioAbierto = df['24_hour_service']
    siHoras = 0
    noHoras = 0
    for i in servicioAbierto:
        if i == 1:
            siHoras = siHoras+1
        elif i == 0:
            noHoras = noHoras+1
   
    servicioClover = df['starbucks_reserve_clover_brewed']
    siClover = 0
    noClover = 0
    for i in servicioClover:
        if i == 1:
            siClover = siClover+1
        elif i == 0:
            noClover = noClover+1

    servicioFood = df['oven_warmed_food']
    siFood = 0
    noFood = 0
    for i in servicioFood:
        if i == 1:
            siFood = siFood+1
        elif i == 0:
            noFood = noFood+1

    servicioWiFi = df['free_wi_fi']
    siWifi = 0
    noWifi = 0
    for i in servicioWiFi:
        if i == 1:
            siWifi = siWifi+1
        elif i == 0:
            noWifi = noWifi+1

    servicioVerismo= df['verismo_system']
    siVerismo = 0
    noVerismo = 0
    for i in servicioVerismo:
        if i == 1:
            siVerismo = siVerismo+1
        elif i == 0:
            noVerismo = noVerismo+1

    servicioMobilePay= df['mobile_payment']
    siMobilePay = 0
    noMobilePay = 0
    for i in servicioMobilePay:
        if i == 1:
            siMobilePay = siMobilePay+1
        elif i == 0:
            noMobilePay = noMobilePay+1

    servicioDigitalReds= df['digital_rewards']
    siDigitalReds = 0
    noDigitalReds = 0
    for i in servicioDigitalReds:
        if i == 1:
            siDigitalReds = siDigitalReds+1
        elif i == 0:
            noDigitalReds = noDigitalReds+1

    servicioBoulange= df['la_boulange']
    siBoulange = 0
    noBoulange = 0
    for i in servicioBoulange:
        if i == 1:
            siBoulange = siBoulange+1
        elif i == 0:
            noBoulange = noBoulange+1
            
    servicioSodas= df['fizzio_handcrafted_sodas']
    siSodas = 0
    noSodas = 0
    for i in servicioSodas:
        if i == 1:
            siSodas = siSodas+1
        elif i == 0:
            noSodas = noSodas+1

    servicioDriveThru= df['drive_thru']
    siDriveThru = 0
    noDriveThru = 0
    for i in servicioDriveThru:
        if i == 1:
            siDriveThru = siDriveThru+1
        elif i == 0:
            noDriveThru = noDriveThru+1

    template = loader.get_template('graficos.html')
    context = {
        'siHoras':siHoras, 
        'noHoras':noHoras,
        'siClover':siClover,
        'noClover':noClover,
        'siFood':siFood, 
        'noFood': noFood,
        'siWifi':siWifi, 
        'noWifi':noWifi ,
        'siVerismo': siVerismo,
        'noVerismo': noVerismo,
        'siMobilePay': siMobilePay,
        'noMobilePay': noMobilePay,
        'siDigitalReds': siDigitalReds,
        'noDigitalReds': noDigitalReds,
        'siBoulange': siBoulange,
        'noBoulange': noBoulange,
        'siSodas': siSodas,
        'noSodas': noSodas,
        'siDriveThru': siDriveThru,
        'noDriveThru': noDriveThru  }

    return HttpResponse(template.render(context, request))

def mapasvm(request):

    bc = datasets.load_breast_cancer()
    X = bc.data
    y = bc.target
 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)

    Vx = "Mi"
    Vy = "Miko"

    pagina = loader.get_template('mapaSVM.html')
    context = {'Vx': Vx , 'Vy': Vy}

    return HttpResponse(pagina.render(context, request))

def cargarMapa(request):

     #NO OLVIDAR CAMBIAR LA RUTA DE MANERA INDIVIDUAL en cada uno de sus
    # equipos, para LA LECTURA DEL ARCHIVO DE STARBUCKS_IN_CALIFORNIA.xlsx
    datos = pd.read_excel(f'{os.path.dirname(os.path.abspath(__file__))}/static/data/starbucks_in_california.xlsx')

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
