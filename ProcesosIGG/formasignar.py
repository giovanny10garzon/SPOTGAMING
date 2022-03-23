from django import forms

import ProcesosIGG


class FormularioAsignar(forms.ModelForm):
    class Meta:
        model = ProcesosIGG

        fields = 'numero', 'clientes', 'fecha', 'fecha_asignacion', 'modelo', 'contacto', 'id_status'
        widgets = {'fecha': forms.DateInput(attrs={'type': 'date'})}
        widgets = {'fecha_asignacion': forms.DateInput(attrs={'type': 'date'})}

