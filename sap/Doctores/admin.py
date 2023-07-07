from django.contrib import admin

from Doctores.models import Doctor, Experiencia, TurnoTrabajo, Lugar_Trabajo

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Experiencia)
admin.site.register(TurnoTrabajo)
admin.site.register(Lugar_Trabajo)