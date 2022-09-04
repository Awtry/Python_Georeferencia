from cgitb import html
from django.shortcuts import render, HttpResponse, redirect
import numpy as np

layout = """
    <h3>Aplicaciones de sistemas geo-referenciados<h3>
    </hr>
    <ul>
        <li>
        <a href="hola-mundo">Hola mundo</a>
        </li>
        <li>
        <a href="matematicas">Matemáticas</a>
        </li>
        <li>
        <a href="calificaciones">Calificaciones</a>
        </li>
        <li>
        <a href="saluda">Say hello!</a>
        </li>
        <li>
        <a href="redire">Regresame!</a>
        </li>
    </ul>
"""

def hola_mundo(request):
    return render(request, 'hola-mundo.html')
    
def index(request):
    return render(request, 'index.html')

def matematicas(request):
    nombres = ["Awtry","Beatrix","Astra"]
    html=""" 
        <h2>Modulo: Matemáticas<h2>
        <ul>
    """
    for i in range(3):
        html += f"<li>{str(i), nombres[i]}<li>"

    html += """ </ul>"""

    return HttpResponse(html)

def calificacion(request):
    nombres = ["Diana", "Alan", "Javier", "Jorge"]
    semestre = 7
    calificaciones = [[8,8,6],[7,6,9],[10,10,10],[0,0,10]] 
    calif = np.array(calificaciones)
    promedio = calif.mean()

    html= """ 
        <h2>Lista de calificaciones</h2>
        <table>
            <tr>
                <th>Nombre</th>
                <th>Semestre</th>
                <th>Calificaciones</th>
                <th>Promedio</th>
            </tr>
            
    """

    for i in range(4):
        
        html += f"<tr><td>{nombres[i]}</td><td>{semestre}</td><td>{calificaciones[1][:]}</td><td>{calif[i][:].mean()}</td> </tr>"
       
    html += f"""
       
        </table>

        <p>Promedio del grupo<p>
        {promedio}
    """
    if promedio <= 5:
        return redirect("/reprobado")

    if promedio >= 6 and promedio <= 8:
        return redirect("/pasable")

    if promedio > 8 and promedio <= 10:
        return redirect("/pasate")
    
    return render(request, 'calificacion.html')

#Parametros en vista
#Parametros admitidos Obligatorios / Opcional / Default
#Obligatorio es solo dejar el nombre del requerimiento / nombre / simplemente
#Opcional es / nombre = "" / así no espera algún valor obligado en la URL
def saluda(request,nombre = "",apellido = ""):
    html= "Oh sweetheart, hello"
    
    if nombre and apellido:
        html += f"""
        <h3> Je m'apelle.. {nombre}, et mon nom de famille {apellido} </h3>
        """
    return HttpResponse(layout + html)

def redireccion(request,a = "0"):
    if a == "1":
        return redirect('index')

    html = "<h2>Redireccionamiento</h2>"

    return render(request, 'redireccion.html')

def repobado(request):
    return render(request, 'reprobado.html')

def pasable(request):
    return render(request, 'pasable.html')

def pasate(request):
    return render(request, 'pasaste.html')

def contacto(request):
    return render(request, 'contacto.html')