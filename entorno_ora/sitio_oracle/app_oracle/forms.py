from django import forms
from django.forms import fields
from app_oracle.models import *

class registroPyme(forms.ModelForm):
    class Meta:
        model = pyme
        fields = ("NomPyme","rutempresa","direccion","rutpersona","nomDueño","categpyme","horario","telefono")

   