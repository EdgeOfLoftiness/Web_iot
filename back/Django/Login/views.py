from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse,HttpResponse
import requests

def index(request):
    return render(request, 'index.html',{
        'form': UserCreationForm
    })

def home(request):

    urlApi = 'http://127.0.0.1:3000/clientes'

    try:

        response = requests.get(urlApi)#pip install requests

        if(response.status_code == 200):
            data = response.json()

            tabla_html = "<table>"
            tabla_html += "<tr>"
            tabla_html += "<td>RUT</td><td>Nombres</td><td>ApellidoP</td><td>ApellidoM</td></tr>"
            for cliente in data['lista']:
                tabla_html += f"<tr><td>{cliente['rut']}</td><td>{cliente['nombres']}</td><td>{cliente['apellidoP']}</td><td>{cliente['apellidoM']}</td>"

            tabla_html += "</tr>"
            tabla_html += "</table>"

            return render(request, 'home.html', {'tabla_html': tabla_html})
        else:
            return HttpResponse("No hay registro de clientes", status=500)
        
    except Exception as e:
        return HttpResponse(str(e), status = 500)




    #return render(request, 'home.html')