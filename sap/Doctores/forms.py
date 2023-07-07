from django.forms import ModelForm, EmailInput

from Doctores.models import Doctor


class DoctorFormulario(ModelForm):

    class Meta:
        model = Doctor
        fields = ('nombre', 'apellido', 'sexo', 'email', 'especialidad', 'activo', 'turno', 'experiencia', 'lugar')
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }
