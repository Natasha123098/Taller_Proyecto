from django.contrib import admin

from Doctores.models import Doctor, Experiencia, TurnoTrabajo

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Experiencia)
admin.site.register(TurnoTrabajo)