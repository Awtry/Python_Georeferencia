"""EX_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppExam import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #URL'S DEL PROYECTO
    path('', views.index, name='index'),
    path('mapa/', views.mapa, name='mapa'),
    path('prueba/', views.prueba, name='prueba'),
    path('listastarbucks/', views.listastarbucks, name='listastarbucks'),
    path('listastarbucksgraf/', views.listastarbucksgraf, name='listastarbucksgraf'),
    path('cargarMapa/', views.cargarMapa, name='cargarMapa'),
    path('mapasvm/', views.mapasvm, name='mapasvm'),
    path('mapsvmred/', views.mapsvmred, name='mapsvmred'),
    
    
    
    #URL'S STYLE DEL PROYECTO


]
