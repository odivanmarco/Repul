from django.forms import ModelForm
from .models import Republica

class RepublicaForms(ModelForm):
    class Meta:
        model = Republica
        fields = '__all__'
