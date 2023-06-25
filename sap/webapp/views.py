from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from Doctores.models import Doctor


# Create your views here.
def mostrarDoctores(request):

    C_doctores = Doctor.objects.count()
    pagina = loader.get_template('doctores.html')
    nombres_doctores = Doctor.objects.all()
    datos = {'cantidad': C_doctores, 'doctores': nombres_doctores}
    return HttpResponse(pagina.render(datos, request))