from django.db import models

class Lugar_Trabajo(models.Model):
    lugar = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'{self.lugar}'

class TurnoTrabajo(models.Model):
    turno = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'{self.turno}'

class Experiencia(models.Model):
    edad = models.IntegerField(null=True)
    años_experiencia = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.años_experiencia}'

# Create your models here.
class Doctor(models.Model):
    SEXO = [
        ("M", "Masculino"),
        ("F", "Femenino"),
    ]
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1, choices=SEXO, null=True)
    email = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)
    turno = models.ForeignKey(TurnoTrabajo, on_delete=models.SET_NULL, null=True)
    experiencia= models.ForeignKey(Experiencia, on_delete=models.SET_NULL, null=True)
    lugar = models.ForeignKey(Lugar_Trabajo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'id: {self.id} - {self.nombre} {self.apellido}'

