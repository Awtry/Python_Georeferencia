"""mylovelypage URL Configuration

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
from apptest import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hola-mundo/", views.hola_mundo, name='Miau'),
    path("", views.index, name='index'),
    path("matematicas/", views.matematicas, name='matematicas'),
    path("calificaciones/", views.calificacion, name="calificaciones"),
    path("saluda/", views.saluda, name='saluda'),
    path("saluda/<str:nombre>", views.saluda, name='saluda'),
    path("saluda/<str:nombre>/<str:apellido>", views.saluda, name='saluda'),
    path("redire/", views.redireccion, name='redire'),
    path("redire/<str:a>", views.redireccion, name='Redireccion'),
    path("reprobado/", views.repobado, name='reprobado'),
    path("pasable/", views.pasable, name='pasable'),
    path("pasate/", views.pasate, name='pasate'),
    path("contacto/", views.contacto, name='contacto'),
    
]
