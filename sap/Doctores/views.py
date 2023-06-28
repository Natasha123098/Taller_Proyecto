from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader

from Doctores.forms import DoctorFormulario
from Doctores.models import Doctor

#DoctorFormulario=modelform_factory(Doctor, exclude=[])

# Create your views here.
def Nuevo_Doctor(request):
    pagina = loader.get_template('Nuevo_Doctor.html')
    if request.method == 'GET':
        formulario= DoctorFormulario
    elif request.method == 'POST':
        formulario= DoctorFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    datos = {'formulario': formulario}
    return HttpResponse(pagina.render(datos, request))

def Editar_Doctor(request, idDoctor):
    pagina= loader.get_template('Editar_Doctor.html')
    #Doctor= Doctor.objects.get(pk=idDoctor)
    doctor= get_object_or_404(Doctor, pk=idDoctor)
    if request.method == 'GET':
        formulario= DoctorFormulario(instance=doctor)
    elif request.method == 'POST':
        formulario= DoctorFormulario(request.POST, instance=doctor)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    mensaje= {'formulario': formulario}
    return HttpResponse(pagina.render(mensaje, request))

def Ver_Doctor(request, idDoctor):
    pagina = loader.get_template('Ver_Doctor.html')
    #doctor = Doctor.objects.get(pk=idDoctor)
    doctor = get_object_or_404(Doctor, pk=idDoctor)
    if request.method == 'GET':
        formulario= DoctorFormulario(instance=doctor)
    elif request.method == 'POST':
        formulario= DoctorFormulario(request.POST, instance=doctor)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    mensaje = {'formulario': formulario}
    return HttpResponse(pagina.render(mensaje, request))

def Eliminar_Doctor(request, idDoctor):

    doctor = get_object_or_404(Doctor, pk=idDoctor)
    if doctor:
        doctor.delete()
        return redirect('inicio')
