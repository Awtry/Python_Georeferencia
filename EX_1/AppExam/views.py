from cgitb import html
from multiprocessing import context
from urllib.robotparser import RequestRate
from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from django.utils.html import escapejs
import simplejson as json
#import geopy  as geo
#from geopy.geocoders import Nominatim
import numpy as np
import pandas as pd
import csv, os
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
    #nombres = []
    #with open('Personas.csv') as File:
    #    reader = csv.reader(File, delimiter=';')
    #    for x in reader: 
    #        nombres.append(x)
            
    script_dir = os.path.dirname(__file__)
    rel_path = r"C:\Users\jorge\Django\EX_1\AppExam\static\data\Personas.csv"
    abs_file_path = os.path.join(script_dir, rel_path)
    #current_file ="Personas.csv"
    #file = open(abs_file_path+current_file,'r')
    columns=['Nombre','Edad']
    datos = pd.read_csv(rel_path , sep=';')
    newData = pd.DataFrame(datos, columns)
    newData.head(2)
    newData.columns(2)

    #Experimental
    #COLUMNS = ['age','workclass', 'fnlwgt', 'education', 'education_num', 'marital',
    #       'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss',
    #       'hours_week', 'native_country', 'label']
    #PATH = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
    #df_train = pd.read_csv(PATH,
    #                   skipinitialspace=True,
    #                   names = COLUMNS,
    #                   index_col=False)

    template = loader.get_template('metricas.html')
    context = { 'datos': newData,}
    return HttpResponse(template.render(context, request))

def cargarMapa(request):

    listaCoordenadas = [[42.51,1.53],[25.42,55.47],[24.4,54.49],[24.48,54.38]]

    listaJson = json.dumps(listaCoordenadas)



    


    print(listaJson)

    pagina = loader.get_template('mapa.html')
    context = {'listaJson': listaJson}
    return HttpResponse(pagina.render(context, request))