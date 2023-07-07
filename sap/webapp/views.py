from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from Doctores.models import Doctor


# Create your views here.
def mostrar_Doctores(request):
    cantidad_Doctores = Doctor.objects.count()
    pagina= loader.get_template('doctores.html')
    #lista_Doctores = Doctor.objects.all()
    lista_Doctores = Doctor.objects.order_by('apellido', 'nombre')
    datos = {'cantidad': cantidad_Doctores,'doctores': lista_Doctores}
    return HttpResponse(pagina.render(datos, request))